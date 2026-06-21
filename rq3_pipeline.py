#!/usr/bin/env python3
"""
RQ3/RQ4 Pipeline: Functional Correctness and Gas Efficiency
Run inside WSL. Requirements: pip install openai

Usage:
    python3 rq3_pipeline.py --output_dir /path/to/output --openai_key sk-...
"""

import argparse
import csv
import json
import os
import re
import shutil
import subprocess
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

# ── Configuration ─────────────────────────────────────────────────────────────

REQUIREMENT_COUNTS = {
    "Ownership and Access Control": 5,
    "Time-Locked Wallet": 6,
    "Simple Voting System": 7,
    "ERC20-Like Token": 6,
    "Escrow Contract": 8,
    "Multi-Signature Wallet": 8,
    "Auction Contract": 7,
    "Subscription Payment System": 8,
    "Crowdfunding Contract": 8,
    "Role-Based Access Control": 7,
}

SPECIFICATIONS = {
    "Ownership and Access Control": """
Create a smart contract with single owner access control using the Ownable pattern.
Requirements:
- The deployer becomes the initial owner
- Implement a modifier to restrict functions to owner-only access
- Include a function to transfer ownership to a new address with validation (non-zero address)
- Emit an OwnershipTransferred event with old and new owner addresses
- Prevent transferring ownership to the current owner
Security: Validate new owner address is not zero address""",

    "Time-Locked Wallet": """
Create a time-locked wallet contract with withdrawal restrictions.
Requirements:
- Accept Ether deposits from any address
- Store beneficiary address and unlock timestamp (both immutable, set at deployment)
- Implement withdrawal function restricted to beneficiary only
- Reject withdrawal attempts before unlock time with clear error message
- Emit events for deposits and withdrawals
- Use block.timestamp for time checks
Security: Ensure beneficiary cannot be zero address, validate unlock time is in the future""",

    "Simple Voting System": """
Create a single-winner voting contract with admin controls.
Requirements:
- Admin can register candidates with unique IDs
- Implement voter registration or allow any address to vote once
- Track vote counts per candidate using mapping
- Admin can end voting period (one-time action)
- Reject votes after voting ends or duplicate votes from same address
- Emit events for candidate registration, votes cast, and voting end
- Return winning candidate after voting ends
Security: Prevent admin from voting or manipulating results, validate candidate exists before voting""",

    "ERC20-Like Token": """
Create a simplified ERC20-compatible token contract.
Requirements:
- Define token name, symbol, and decimals (18 recommended)
- Mint fixed total supply to deployer at deployment
- Implement transfer function with balance validation
- Use mapping for balances (address => uint256)
- Emit Transfer events on all transfers (including minting)
- Revert transfers with insufficient balance or to zero address
Security: Use Solidity 0.8+ overflow protection, validate recipient addresses""",

    "Escrow Contract": """
Create a three-party escrow contract with dispute resolution.
Requirements:
- Initialize with buyer, seller, and arbiter addresses at deployment
- Buyer deposits exact Ether amount during contract creation (payable constructor)
- Seller can mark item as delivered
- Buyer can release payment to seller if satisfied
- Arbiter can resolve disputes and allocate funds to buyer or seller
- Track contract state (Created, Delivered, Released, Refunded, Disputed)
- Emit events for all state changes
- Ensure funds can only be released once using state checks
Security: Use Checks-Effects-Interactions pattern, prevent reentrancy, validate all addresses are unique and non-zero""",

    "Multi-Signature Wallet": """
Create a multi-signature wallet requiring multiple approvals.
Requirements:
- Initialize with array of owner addresses and required approval threshold
- Validate threshold <= number of owners and > 0
- Implement transaction proposal (target address, value, data)
- Track approvals per transaction using nested mappings
- Allow owners to approve transactions
- Execute transaction only when threshold met
- Prevent double-approvals from same owner
- Emit events for submissions, approvals, and executions
Security: Use call instead of transfer for execution, handle failed transactions, prevent reentrancy on execution""",

    "Auction Contract": """
Create a highest-bid auction with automatic refunds.
Requirements:
- Set auction start time, end time, and minimum bid at deployment
- Accept bids only during auction period (between start and end time)
- Track highest bidder and highest bid amount
- Automatically refund previous highest bidder when outbid
- Implement manual withdrawal pattern for failed automatic refunds
- Allow auction creator to withdraw winning bid after auction ends
- Emit events for new bids, auction end, and withdrawals
Security: Use pull payment pattern for refunds to prevent DOS attacks, validate bid is higher than current highest bid""",

    "Subscription Payment System": """
Create a time-based subscription management system.
Requirements:
- Define subscription fee and duration (e.g., 30 days) as constants
- Implement subscribe function accepting payment
- Calculate and store expiration timestamp per user
- Implement modifier to check active subscription status
- Allow subscription renewal before or after expiration
- Track total subscribers and revenue
- Emit events for new subscriptions and renewals
- Implement view function to check if user has active subscription
Security: Validate payment amount matches subscription fee, handle expired subscriptions gracefully""",

    "Crowdfunding Contract": """
Create a goal-based crowdfunding campaign with refund mechanism.
Requirements:
- Set campaign creator, funding goal, and deadline at deployment
- Accept contributions only before deadline
- Track contributions per address using mapping
- Implement goal check (total contributions >= goal)
- Creator can withdraw funds only if goal reached after deadline
- Contributors can claim refunds only if goal not reached after deadline
- Prevent double refunds using state tracking
- Emit events for contributions, withdrawals, and refunds
Security: Use Checks-Effects-Interactions pattern, prevent reentrancy on refunds, validate deadline is in the future""",

    "Role-Based Access Control": """
Create a flexible role-based access control (RBAC) system.
Requirements:
- Define multiple roles as bytes32 constants (ADMIN_ROLE, MANAGER_ROLE, USER_ROLE)
- Admin (deployer) can grant and revoke roles
- Implement modifier to check if caller has specific role
- Track roles using nested mapping (role => address => bool)
- Create sample functions demonstrating different role requirements
- Admin can renounce their own role
- Emit RoleGranted and RoleRevoked events
Security: Validate addresses are not zero, ensure at least one admin exists, prevent role escalation""",
}

# ── Foundry helpers ───────────────────────────────────────────────────────────

def run(cmd, cwd, timeout=180):
    """Run a command, return (returncode, stdout, stderr)."""
    try:
        r = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True, timeout=timeout)
        return r.returncode, r.stdout, r.stderr
    except subprocess.TimeoutExpired:
        return -1, "", "TIMEOUT"
    except Exception as e:
        return -1, "", str(e)


def setup_foundry(foundry_dir: Path):
    """Create a Foundry project if one does not exist."""
    if (foundry_dir / "foundry.toml").exists():
        return
    foundry_dir.mkdir(parents=True, exist_ok=True)
    rc, _, err = run(["forge", "init", "--no-git", "--force", "--empty", str(foundry_dir)], cwd=foundry_dir.parent, timeout=60)
    if rc != 0:
        raise RuntimeError(f"forge init failed: {err}")
    if not (foundry_dir / "foundry.toml").exists():
        raise RuntimeError(
            f"forge init reported success (rc=0) but no foundry.toml was created at {foundry_dir}. "
            f"The directory is likely in a broken state — delete it and retry: rm -rf {foundry_dir}"
        )
    # Belt-and-suspenders: remove any leftover example files (src/, test/, script/)
    # in case --empty isn't honored by a given forge version.
    for sub in ("src", "test", "script"):
        for f in (foundry_dir / sub).glob("*.sol"):
            f.unlink()
    print("[foundry] Project initialized.")


def get_contract_name(sol_path: Path) -> str:
    """Extract first contract name from a .sol file."""
    try:
        m = re.search(r"contract\s+(\w+)", sol_path.read_text(encoding="utf-8", errors="ignore"))
        if m:
            return m.group(1)
    except Exception:
        pass
    return sol_path.stem.replace(" ", "_").replace("-", "_")


def place_files(foundry_dir: Path, sol_path: Path, contract_name: str, test_code: str):
    """Copy contract and test into Foundry src/ and test/."""
    src_dir = foundry_dir / "src"
    test_dir = foundry_dir / "test"
    # Ensure directories exist
    src_dir.mkdir(parents=True, exist_ok=True)
    test_dir.mkdir(parents=True, exist_ok=True)
    # Clear previous files
    for f in src_dir.glob("*.sol"):
        f.unlink()
    for f in test_dir.glob("*.sol"):
        f.unlink()
    shutil.copy2(sol_path, src_dir / f"{contract_name}.sol")
    (test_dir / f"{contract_name}Test.t.sol").write_text(test_code, encoding="utf-8")


def parse_test_results(stdout: str) -> dict:
    """
    Parse forge test --json output into {test_name: bool}.
    Forge 1.5.x mixes compilation text with JSON stdout — extract JSON robustly.
    """
    results = {}
    if not stdout.strip():
        return results

    # Extract only the JSON portion — skip any leading text like "Nothing to compile"
    json_start = stdout.find("{")
    if json_start == -1:
        return results
    json_str = stdout[json_start:]

    # Find matching closing brace for the top-level object
    depth, end = 0, 0
    for i, ch in enumerate(json_str):
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                end = i + 1
                break
    json_str = json_str[:end]

    try:
        data = json.loads(json_str)
        for suite in data.values():
            if not isinstance(suite, dict):
                continue
            # Forge 1.5.x uses "test_results" key; older forge uses suite directly
            inner = suite.get("test_results", suite)
            if isinstance(inner, dict):
                for name, info in inner.items():
                    if not isinstance(info, dict):
                        continue
                    status = info.get("status", "")
                    # Forge 1.5.x: "Success"/"Failure"; older: "pass"/"fail"
                    results[name] = status in ("Success", "pass")
    except Exception as e:
        print(f"  [warn] JSON parse error: {e} | snippet: {json_str[:200]}")

    return results


def parse_gas_report(output: str) -> dict:
    """Parse forge --gas-report text into {fn_name: avg_gas}."""
    results = {}
    # Matches table rows: | FunctionName | calls | min | avg | median | max |
    pattern = re.compile(r"\|\s*(\w+)\s*\|\s*\d+\s*\|\s*\d+\s*\|\s*(\d+)\s*\|\s*\d+\s*\|\s*\d+\s*\|")
    for line in output.splitlines():
        m = pattern.match(line.strip())
        if m:
            results[m.group(1)] = int(m.group(2))  # avg gas
    return results


# ── GPT-4o test generation ────────────────────────────────────────────────────

def generate_test(client: OpenAI, exercise: str, contract_source: str, contract_name: str) -> tuple:
    """Call GPT-4o to produce a Foundry test file. Returns (code, error)."""
    req_count = REQUIREMENT_COUNTS.get(exercise, 5)
    spec = SPECIFICATIONS.get(exercise, "")
    req_list = "\n".join(f"- test_req_{i+1}()" for i in range(req_count))

    prompt = f"""EXERCISE: {exercise}

SPECIFICATION:
{spec.strip()}

CONTRACT NAME: {contract_name}
CONTRACT SOURCE:
{contract_source.strip()}

TASK:
Write a Foundry test contract named {contract_name}Test that tests each requirement.

RULES:
1. Write exactly {req_count} test functions named:
{req_list}
2. Import: import "../src/{contract_name}.sol";
3. Use setUp() to deploy a fresh instance before each test.
4. Use vm.prank(), vm.warp(), vm.deal(), vm.expectRevert() as needed.
5. If a requirement cannot be tested because the contract is missing the needed
   functionality, call a non-existent function so the file fails to compile.
6. Output ONLY valid Solidity. No markdown, no explanations.
7. Start with: // SPDX-License-Identifier: MIT"""

    try:
        resp = client.chat.completions.create(
            model="gpt-4o",
            temperature=0,
            max_tokens=3000,
            messages=[
                {"role": "system", "content": "You are an expert Solidity Foundry test engineer. Output only valid Solidity code, no markdown."},
                {"role": "user", "content": prompt},
            ],
        )
        code = resp.choices[0].message.content.strip()
        code = re.sub(r"^```[a-zA-Z]*\n?", "", code)
        code = re.sub(r"\n?```$", "", code).strip()
        return code, None
    except Exception as e:
        return None, str(e)


# ── Main pipeline ─────────────────────────────────────────────────────────────

def run_pipeline(output_dir: Path, openai_key: str):
    output_dir = output_dir.resolve()  # absolute path — avoids relative-path bugs when combined with subprocess cwd
    client = OpenAI(api_key=openai_key)

    # Load inputs
    compilation = json.loads((output_dir / "compilation_results.json").read_text())
    summary     = json.loads((output_dir / "generation_summary.json").read_text())
    folder_map  = summary.get("folder_mapping", {})

    # Setup output folders
    rq3_dir     = output_dir / "rq3_results"
    tests_dir   = rq3_dir / "generated_tests"
    foundry_dir = rq3_dir / "foundry_project"
    for d in [rq3_dir, tests_dir]:
        d.mkdir(exist_ok=True)
    setup_foundry(foundry_dir)

    scores_rows = []
    gas_rows    = []
    failures    = []

    total = compiled_count = processed = 0

    # ── TEMP: limit to N contracts for a quick test run ────────────────────
    TEST_LIMIT = None   # set to None (or delete this block) to process everything
    # ─────────────────────────────────────────────────────────────────────────

    for model_name, prompts in compilation.items():
        model_folder  = folder_map.get(model_name, {}).get("folder_name", model_name)
        prompt_map    = folder_map.get(model_name, {}).get("prompts", {})

        for exercise, iterations in prompts.items():
            prompt_folder = prompt_map.get(exercise, {}).get("folder_name", exercise)

            for iter_key, iter_data in iterations.items():
                total += 1
                iter_num = iter_key.replace("iteration_", "")

                if not iter_data.get("compilation", {}).get("success", False):
                    continue
                compiled_count += 1

                sol_path = output_dir / model_folder / prompt_folder / f"{iter_num}.sol"
                if not sol_path.exists():
                    print(f"  [warn] missing: {sol_path}")
                    failures.append({"model": model_name, "exercise": exercise, "iter": iter_num, "reason": "sol_missing"})
                    continue

                contract_name   = get_contract_name(sol_path)
                contract_source = sol_path.read_text(encoding="utf-8", errors="ignore")
                label = f"[{compiled_count}] {model_name} | {exercise} | iter {iter_num}"
                print(f"\n{label}")

                # ── Generate test ─────────────────────────────────────────────
                test_code, gen_err = generate_test(client, exercise, contract_source, contract_name)

                # Save test file regardless of outcome
                save_dir = tests_dir / model_folder / prompt_folder
                save_dir.mkdir(parents=True, exist_ok=True)
                if test_code:
                    (save_dir / f"{iter_num}_test.sol").write_text(test_code, encoding="utf-8")

                if not test_code:
                    print(f"  [fail] test generation: {gen_err}")
                    failures.append({"model": model_name, "exercise": exercise, "iter": iter_num, "reason": "test_gen_failed", "error": gen_err})
                    scores_rows.append(_failure_row(model_name, exercise, iter_num, contract_name, "test_gen_failed"))
                    continue

                # ── Place in Foundry and build ─────────────────────────────────
                place_files(foundry_dir, sol_path, contract_name, test_code)

                # # DEBUG — remove after fixing
                # print(f"  [debug] foundry_dir = {foundry_dir.resolve()}")
                # print(f"  [debug] src/  -> {[p.name for p in (foundry_dir / 'src').glob('*.sol')]}")
                # print(f"  [debug] test/ -> {[p.name for p in (foundry_dir / 'test').glob('*.sol')]}")

                rc, build_stdout, build_err = run(["forge", "build", "--force"], cwd=foundry_dir)
                # print(f"  [debug] forge build rc={rc}")
                # print(f"  [debug] build stdout (first 500 chars):\n{build_stdout[:500]}")
                if rc != 0:
                    print(f"  [fail] forge build")
                    failures.append({"model": model_name, "exercise": exercise, "iter": iter_num, "reason": "build_failed", "error": build_err[:300]})
                    scores_rows.append(_failure_row(model_name, exercise, iter_num, contract_name, "build_failed"))
                    continue

                # ── Run tests ─────────────────────────────────────────────────
                # rc, test_stdout, _ = run(["forge", "test", "--json", "-vv"], cwd=foundry_dir)
                # test_results = parse_test_results(test_stdout)

                rc, test_stdout, test_stderr = run(["forge", "test", "--json", "-vv", "--force"], cwd=foundry_dir)

                # # DEBUG — remove after fixing
                # print(f"  [debug] forge test rc={rc}")
                # print(f"  [debug] stdout (first 1000 chars):\n{test_stdout[:1000]}")
                # print(f"  [debug] stderr (first 500 chars):\n{test_stderr[:500]}")

                test_results = parse_test_results(test_stdout)
                # print(f"  [debug] parsed test_results: {test_results}")

                req_count  = REQUIREMENT_COUNTS.get(exercise, 1)
                # Normalize test names: forge JSON keys are typically "test_req_1()" —
                # strip the "()" / signature suffix so they match "test_req_N" exactly.
                req_tests = {}
                for k, v in test_results.items():
                    m = re.match(r"(test_req_\d+)", k)
                    if m:
                        req_tests[m.group(1)] = v
                passed     = sum(req_tests.values())
                score      = round(passed / req_count, 4)
                fully_ok   = passed == req_count

                print(f"  score={score:.2f} ({passed}/{req_count}) fully_correct={fully_ok}")

                row = {
                    "model":          model_name,
                    "exercise":       exercise,
                    "iteration":      iter_num,
                    "contract_name":  contract_name,
                    "status":         "ok",
                    "passed":         passed,
                    "total_required": req_count,
                    "score":          score,
                    "fully_correct":  fully_ok,
                }
                for i in range(req_count):
                    row[f"test_req_{i+1}"] = req_tests.get(f"test_req_{i+1}", None)
                scores_rows.append(row)

                # ── Gas report (only if tests passed at least partially) ───────
                if passed > 0:
                    _, gas_stdout, _ = run(["forge", "test", "--gas-report"], cwd=foundry_dir)
                    for fn, avg_gas in parse_gas_report(gas_stdout).items():
                        gas_rows.append({
                            "model":         model_name,
                            "exercise":      exercise,
                            "iteration":     iter_num,
                            "contract_name": contract_name,
                            "function":      fn,
                            "gas_avg":       avg_gas,
                        })

                processed += 1
                # break

            if TEST_LIMIT and processed >= TEST_LIMIT:
                break
        if TEST_LIMIT and processed >= TEST_LIMIT:
            break

    # ── Write outputs ─────────────────────────────────────────────────────────
    _write_csv(scores_rows, rq3_dir / "rq3_scores.csv")
    _write_csv(gas_rows,    rq3_dir / "rq3_gas.csv")
    (rq3_dir / "rq3_failures.json").write_text(json.dumps(failures, indent=2))

    print("\n" + "=" * 50)
    print(f"Total iterations:        {total}")
    print(f"Compiled (eligible):     {compiled_count}")
    print(f"Successfully processed:  {processed}")
    print(f"Failures logged:         {len(failures)}")
    print(f"Scores  → {rq3_dir / 'rq3_scores.csv'}")
    print(f"Gas     → {rq3_dir / 'rq3_gas.csv'}")
    print(f"Failures→ {rq3_dir / 'rq3_failures.json'}")


# ── Helpers ───────────────────────────────────────────────────────────────────

def _failure_row(model, exercise, iteration, contract_name, reason):
    return {
        "model": model, "exercise": exercise, "iteration": iteration,
        "contract_name": contract_name, "status": reason,
        "passed": None, "total_required": None, "score": None, "fully_correct": None,
    }


def _write_csv(rows, path):
    if not rows:
        return
    all_keys = list(dict.fromkeys(k for row in rows for k in row))
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=all_keys, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    print(f"[csv] {path.name} — {len(rows)} rows")


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output_dir", default="output", help="Path to output/ directory")
    # parser.add_argument("--openai_key", required=True, help="OpenAI API key")
    args = parser.parse_args()
    run_pipeline(Path(args.output_dir), os.getenv("OPENAI_API_KEY"))