import os
import json
import re
import subprocess
import time
import traceback
import requests
import pandas as pd
import shutil
from typing import Dict, List, Tuple, Any, Optional
from collections import defaultdict
from datetime import datetime
from yaspin import yaspin
from dotenv import load_dotenv

load_dotenv()

# ── Configuration ──────────────────────────────────────────────────────────────
OLLAMA_TIMEOUT   = 180
MAX_RETRIES      = 2
REQUEST_TIMEOUT  = 180
DATASET_PATH     = "prompts_final.csv"

REPAIR_STRATEGIES = ["direct_fix", "chain_of_thought", "role_based"]

# Copied from compile_and_analyze.py – kept in sync intentionally
VULNERABILITY_SEVERITY = {
    "storage-abiencoderv2-array": "High",
    "arbitrary-from-in-transferfrom": "High",
    "modifying-storage-array-by-value": "High",
    "abi-encodePacked-collision": "High",
    "incorrect-shift-in-assembly": "High",
    "multiple-constructor-schemes": "High",
    "name-reused": "High",
    "protected-variables": "High",
    "public-mappings-with-nested-variables": "High",
    "right-to-left-override-character": "High",
    "state-variable-shadowing": "High",
    "suicidal": "High",
    "uninitialized-state-variables": "High",
    "uninitialized-storage-variables": "High",
    "unprotected-upgradeable-contract": "High",
    "codex": "High",
    "arbitrary-from-in-transferfrom-used-with-permit": "High",
    "functions-that-send-ether-to-arbitrary-destinations": "High",
    "array-length-assignment": "High",
    "controlled-delegatecall": "High",
    "payable-functions-using-delegatecall-inside-a-loop": "High",
    "incorrect-exponentiation": "High",
    "incorrect-return-in-assembly": "High",
    "msgvalue-inside-a-loop": "High",
    "reentrancy-vulnerabilities": "High",
    "return-instead-of-leave-in-assembly": "High",
    "storage-signed-integer-array": "High",
    "unchecked-transfer": "High",
    "weak-PRNG": "High",
    "domain-separator-collision": "Medium",
    "dangerous-enum-conversion": "Medium",
    "incorrect-erc20-interface": "Medium",
    "incorrect-erc721-interface": "Medium",
    "dangerous-strict-equalities": "Medium",
    "contracts-that-lock-ether": "Medium",
    "deletion-on-mapping-containing-a-structure": "Medium",
    "state-variable-shadowing-from-abstract-contracts": "Medium",
    "tautological-compare": "Medium",
    "tautology-or-contradiction": "Medium",
    "write-after-write": "Medium",
    "misuse-of-a-boolean-constant": "Medium",
    "constant-functions-using-assembly-code": "Medium",
    "constant-functions-changing-the-state": "Medium",
    "divide-before-multiply": "Medium",
    "out-of-order-retryable-transactions": "Medium",
    "reentrancy-vulnerabilities-1": "Medium",
    "reused-base-constructors": "Medium",
    "dangerous-usage-of-txorigin": "Medium",
    "unchecked-low-level-calls": "Medium",
    "unchecked-send": "Medium",
    "uninitialized-local-variables": "Medium",
    "unused-return": "Medium",
    "incorrect-modifier": "Low",
    "builtin-symbol-shadowing": "Low",
    "local-variable-shadowing": "Low",
    "uninitialized-function-pointers-in-constructors": "Low",
    "pre-declaration-usage-of-local-variables": "Low",
    "void-constructor": "Low",
    "calls-inside-a-loop": "Low",
    "missing-events-access-control": "Low",
    "missing-events-arithmetic": "Low",
    "dangerous-unary-expressions": "Low",
    "missing-zero-address-validation": "Low",
    "reentrancy-vulnerabilities-2": "Low",
    "reentrancy-vulnerabilities-3": "Low",
    "return-bomb": "Low",
    "block-timestamp": "Low",
    "assembly-usage": "Informational",
    "assert-state-change": "Informational",
    "boolean-equality": "Informational",
    "cyclomatic-complexity": "Informational",
    "deprecated-standards": "Informational",
    "unindexed-erc20-event-parameters": "Informational",
    "function-initializing-state": "Informational",
    "incorrect-using-for-usage": "Informational",
    "low-level-calls": "Informational",
    "missing-inheritance": "Informational",
    "conformance-to-solidity-naming-conventions": "Informational",
    "different-pragma-directives-are-used": "Informational",
    "redundant-statements": "Informational",
    "incorrect-versions-of-solidity": "Informational",
    "unimplemented-functions": "Informational",
    "unused-imports": "Informational",
    "unused-state-variable": "Informational",
    "costly-operations-inside-a-loop": "Informational",
    "dead-code": "Informational",
    "reentrancy-vulnerabilities-4": "Informational",
    "too-many-digits": "Informational",
    "cache-array-length": "Optimization",
    "state-variables-that-could-be-declared-constant": "Optimization",
    "public-function-that-could-be-declared-external": "Optimization",
    "state-variables-that-could-be-declared-immutable": "Optimization",
    "public-variable-read-in-external-context": "Optimization",
}

SEVERITY_ORDER   = ["High", "Medium", "Low", "Informational", "Optimization"]
MALIGN_SEVERITIES = ["High", "Medium", "Low"]


# ── Helper dataclass-like dict keys ────────────────────────────────────────────
# failed_contract entry:
# {
#   "model_name":     str,
#   "model_folder":   str,
#   "prompt_name":    str,
#   "prompt_folder":  str,
#   "iteration_key":  str,          e.g. "iteration_0"
#   "iteration_num":  str,          e.g. "0"
#   "sol_path":       str,
#   "faulty_code":    str,
#   "compile_error":  str,
#   "specification":  str,
# }


class RepairMechanism:
    def __init__(self, output_dir: str = "output"):
        self.output_dir   = output_dir
        self.repair_dir   = os.path.join(output_dir, "repairs")

        # Paths from previous pipeline stages
        self.compilation_results_path  = os.path.join(output_dir, "compilation_results.json")
        self.generation_summary_path   = os.path.join(output_dir, "generation_summary.json")

        # Loaded data
        self.compilation_results: Dict = {}
        self.folder_mapping:      Dict = {}
        self.spec_lookup:         Dict = {}   # prompt_name -> specification string

        # Results produced by this script
        self.repair_results:  Dict = {}   # full per-contract per-strategy results
        self.repair_summary:  Dict = {}   # aggregated statistics

        self.failed_contracts: List[Dict] = []

    # ── Data loading ────────────────────────────────────────────────────────────

    def load_data(self) -> None:
        """Load all prerequisite data files."""
        print("[LOAD] Reading compilation_results.json ...")
        if not os.path.exists(self.compilation_results_path):
            raise FileNotFoundError(
                f"Not found: {self.compilation_results_path}\n"
                "Run compile_and_analyze.py first."
            )
        with open(self.compilation_results_path, 'r', encoding='utf-8') as f:
            self.compilation_results = json.load(f)

        print("[LOAD] Reading generation_summary.json ...")
        if not os.path.exists(self.generation_summary_path):
            raise FileNotFoundError(
                f"Not found: {self.generation_summary_path}\n"
                "Run generate_contracts.py first."
            )
        with open(self.generation_summary_path, 'r', encoding='utf-8') as f:
            summary = json.load(f)
            self.folder_mapping = summary.get("folder_mapping", {})

        print("[LOAD] Reading prompts CSV ...")
        if not os.path.exists(DATASET_PATH):
            raise FileNotFoundError(f"Prompts CSV not found: {DATASET_PATH}")
        df = pd.read_csv(DATASET_PATH, encoding='latin1')
        for i in range(df.shape[0]):
            task = df.iat[i, 0]
            spec = df.iat[i, 1]
            self.spec_lookup[task] = spec

        print(f"[LOAD] {len(self.spec_lookup)} specifications loaded from CSV")
        print(f"[LOAD] {len(self.compilation_results)} model(s) found in compilation results\n")

    def identify_failed_contracts(self) -> None:
        """
        Walk through compilation_results.json and collect every contract whose compilation.success == False (and that had a successful generation).
        Populates self.failed_contracts.
        """
        self.failed_contracts = []

        for model_name, prompts in self.compilation_results.items():
            model_folder = self.folder_mapping.get(model_name, {}).get(
                "folder_name", self._sanitize(model_name)
            )

            for prompt_name, iterations in prompts.items():
                prompt_folder = (
                    self.folder_mapping
                    .get(model_name, {})
                    .get("prompts", {})
                    .get(prompt_name, {})
                    .get("folder_name", self._sanitize(prompt_name))
                )
                specification = self.spec_lookup.get(prompt_name, "")

                for iteration_key, iter_data in iterations.items():
                    # Skip contracts that failed at generation stage
                    if iter_data.get("generation", {}).get("error"):
                        continue

                    compilation = iter_data.get("compilation", {})
                    if compilation.get("success", True):
                        continue  # compiled fine – nothing to repair

                    iteration_num = iteration_key.replace("iteration_", "")
                    sol_path = os.path.join(
                        self.output_dir, model_folder, prompt_folder,
                        f"{iteration_num}.sol"
                    )

                    # Read faulty code from disk
                    faulty_code = ""
                    if os.path.exists(sol_path):
                        with open(sol_path, 'r', encoding='utf-8') as f:
                            faulty_code = f.read()
                    else:
                        # Nothing to repair if file is missing
                        continue

                    compile_error = compilation.get("stderr", "").strip()

                    self.failed_contracts.append({
                        "model_name":    model_name,
                        "model_folder":  model_folder,
                        "prompt_name":   prompt_name,
                        "prompt_folder": prompt_folder,
                        "iteration_key": iteration_key,
                        "iteration_num": iteration_num,
                        "sol_path":      sol_path,
                        "faulty_code":   faulty_code,
                        "compile_error": compile_error,
                        "specification": specification,
                    })

        total = len(self.failed_contracts)
        print(f"[IDENTIFY] {total} failed contract(s) found that need repair\n")

        # Print breakdown by model
        model_counts: Dict[str, int] = defaultdict(int)
        for fc in self.failed_contracts:
            model_counts[fc["model_name"]] += 1
        for model, count in model_counts.items():
            print(f"  {model}: {count} failed contract(s)")
        print()

    # ── Prompt builders ─────────────────────────────────────────────────────────

    def _build_prompt(self, strategy: str, prompt_name: str, specification: str,
                      faulty_code: str, compile_error: str) -> str:
        """Return a repair prompt for the given strategy."""

        if strategy == "direct_fix":
            return (
                f"The following Solidity smart contract failed to compile.\n"
                f"Fix ALL compilation errors and return the corrected, complete contract.\n\n"
                f"TASK: {prompt_name}\n"
                f"SPECIFICATION: {specification}\n\n"
                f"FAULTY CONTRACT:\n"
                f"```solidity\n{faulty_code}\n```\n\n"
                f"COMPILATION ERRORS:\n"
                f"{compile_error}\n\n"
                f"OUTPUT FORMAT:\n"
                f"- Provide ONLY the corrected Solidity code\n"
                f"- NO explanations, NO markdown formatting outside code blocks\n"
                f"- Ensure the contract fully matches the original specification\n"
                f"- Start with the SPDX license or pragma statement\n"
            )

        elif strategy == "chain_of_thought":
            return (
                f"A Solidity smart contract failed to compile. "
                f"Work through each error methodically before writing the fix.\n\n"
                f"TASK: {prompt_name}\n"
                f"SPECIFICATION: {specification}\n\n"
                f"FAULTY CONTRACT:\n"
                f"```solidity\n{faulty_code}\n```\n\n"
                f"COMPILATION ERRORS:\n"
                f"{compile_error}\n\n"
                f"INSTRUCTIONS – follow these steps in order:\n"
                f"Step 1. List each compilation error and identify its root cause.\n"
                f"Step 2. For each error, describe the exact code change required.\n"
                f"Step 3. Verify the planned changes satisfy the original specification.\n"
                f"Step 4. Output the complete corrected Solidity contract.\n\n"
                f"OUTPUT FORMAT:\n"
                f"- After your reasoning, wrap the final contract in ```solidity ... ``` fences\n"
                f"- The contract must be complete – no placeholders or partial code\n"
                f"- Start the contract with the SPDX license or pragma statement\n"
            )

        elif strategy == "role_based":
            return (
                f"You are a senior Solidity security engineer with 10+ years of experience "
                f"auditing and fixing production smart contracts on Ethereum mainnet.\n"
                f"A junior developer submitted the contract below and the compiler rejected it. "
                f"Your job is to produce a corrected, production-ready version that compiles "
                f"cleanly and faithfully implements the original specification.\n\n"
                f"TASK: {prompt_name}\n"
                f"SPECIFICATION: {specification}\n\n"
                f"SUBMITTED CONTRACT (FAULTY):\n"
                f"```solidity\n{faulty_code}\n```\n\n"
                f"COMPILER FEEDBACK:\n"
                f"{compile_error}\n\n"
                f"REQUIREMENTS:\n"
                f"- Resolve every compiler error – the contract MUST compile with solc ^0.8.x\n"
                f"- Preserve all intended functionality described in the specification\n"
                f"- Apply Solidity security best practices (reentrancy guards, access control, etc.)\n"
                f"- Optimise for gas where possible without sacrificing correctness\n\n"
                f"OUTPUT FORMAT:\n"
                f"- Return ONLY the corrected Solidity code inside ```solidity ... ``` fences\n"
                f"- No prose outside the code block\n"
                f"- Start with the SPDX license or pragma statement\n"
            )

        else:
            raise ValueError(f"Unknown repair strategy: {strategy}")

    # ── Ollama API ───────────────────────────────────────────────────────────────

    def _call_ollama(self, model: str, prompt: str, temperature: float = 0.2,
                     retry_count: int = 0) -> Dict[str, Any]:
        """POST to local Ollama /api/generate with timeout + retry."""
        url     = "http://localhost:11434/api/generate"
        headers = {'Content-Type': 'application/json'}
        payload = {
            "model":      model,
            "prompt":     prompt,
            "stream":     False,
            "keep_alive": "30m",
            "options":    {"temperature": temperature}
        }
        try:
            response = requests.post(
                url, headers=headers, json=payload, timeout=REQUEST_TIMEOUT
            )
            if response.status_code == 200:
                return response.json()
            response.raise_for_status()
        except requests.exceptions.Timeout:
            if retry_count < MAX_RETRIES:
                print(f"\n[WARN] Timeout – retrying ({retry_count+1}/{MAX_RETRIES})...")
                time.sleep(2)
                return self._call_ollama(model, prompt, temperature, retry_count + 1)
            raise TimeoutError(f"Request timed out after {REQUEST_TIMEOUT}s")
        except Exception as e:
            if retry_count < MAX_RETRIES:
                print(f"\n[WARN] Request failed: {e} – retrying ({retry_count+1}/{MAX_RETRIES})...")
                time.sleep(2)
                return self._call_ollama(model, prompt, temperature, retry_count + 1)
            raise

    # ── Solidity extraction (mirrors generate_contracts.py) ─────────────────────

    def _extract_solidity(self, text: str) -> str:
        """Pull Solidity from markdown fences; fall back to raw text."""
        pattern = re.compile(r'```(.*?)```', re.DOTALL)
        matches = pattern.findall(text)

        extracted = []
        for match in matches:
            match = match.strip()
            lines = match.split('\n')
            if lines and lines[0].strip().lower() == "solidity":
                lines = lines[1:]
            if not lines:
                continue
            code = '\n'.join(lines)
            if not code.strip().startswith('// SPDX-License-Identifier:'):
                code = '// SPDX-License-Identifier: UNLICENSED\n' + code
            extracted.append(code)

        return '\n\n'.join(extracted) if extracted else text

    # ── Compilation (mirrors compile_and_analyze.py) ─────────────────────────────

    def _compile(self, sol_path: str) -> Dict[str, Any]:
        """Compile with solc + OpenZeppelin support."""
        try:
            cmd = [
                "solc",
                "--gas", "--bin",
                "--base-path", ".",
                "--include-path", "node_modules",
                "@openzeppelin/contracts/=node_modules/@openzeppelin/contracts/",
                sol_path
            ]
            result = subprocess.run(
                cmd, capture_output=True, text=True,
                timeout=30, cwd=os.getcwd()
            )
            return {
                "success":     result.returncode == 0,
                "returnCode":  result.returncode,
                "stdout":      result.stdout,
                "stderr":      result.stderr,
            }
        except subprocess.TimeoutExpired:
            return {"success": False, "returnCode": -1,
                    "stdout": "", "stderr": "Compilation timeout (30s)"}
        except Exception as e:
            return {"success": False, "returnCode": -1,
                    "stdout": "", "stderr": f"Compilation error: {e}"}

    def _run_slither(self, sol_path: str) -> Dict[str, Any]:
        """Run Slither static analysis."""
        try:
            cmd = [
                "slither", sol_path,
                "--solc-remaps",
                "@openzeppelin/contracts/=node_modules/@openzeppelin/contracts/",
                "--solc-args",
                "--base-path . --include-path node_modules"
            ]
            result = subprocess.run(
                cmd, capture_output=True, text=True,
                timeout=60, cwd=os.getcwd()
            )
            return {
                "returnCode": result.returncode,
                "stdout":     result.stdout,
                "stderr":     result.stderr,
            }
        except subprocess.TimeoutExpired:
            return {"returnCode": -1, "stdout": "", "stderr": "Slither timeout (60s)"}
        except FileNotFoundError:
            return {"returnCode": -1, "stdout": "",
                    "stderr": "Slither not found. Install: pip install slither-analyzer"}
        except Exception as e:
            return {"returnCode": -1, "stdout": "", "stderr": str(e)}

    # ── Vulnerability helpers (mirrors compile_and_analyze.py) ───────────────────

    def _extract_vulnerabilities(self, slither_stderr: str) -> List[str]:
        pattern = re.compile(
            r'Reference: https://github\.com/crytic/slither/wiki/Detector-Documentation#([\w-]+)'
        )
        return list(set(pattern.findall(slither_stderr)))

    def _has_only_benign_vulns(self, vulns: List[str]) -> bool:
        for v in vulns:
            if VULNERABILITY_SEVERITY.get(v, "Unknown") not in ["Optimization", "Informational"]:
                return False
        return True

    def _init_severity_dict(self) -> Dict[str, int]:
        return {s: 0 for s in SEVERITY_ORDER}

    # ── Utilities ────────────────────────────────────────────────────────────────

    def _sanitize(self, name: str) -> str:
        return re.sub(r'[<>:"/\\|?*]', '_', name)

    # ── Core repair loop ─────────────────────────────────────────────────────────

    def repair_all(self) -> None:
        """
        Main loop: for every failed contract, call the LLM once per strategy,
        save the repaired .sol file, compile it, run Slither if it compiles.
        """
        os.makedirs(self.repair_dir, exist_ok=True)

        print("=" * 80)
        print(" " * 22 + "SMART CONTRACT REPAIR MECHANISM")
        print("=" * 80)
        print(f"[CONFIG] Strategies : {REPAIR_STRATEGIES}")
        print(f"[CONFIG] Contracts  : {len(self.failed_contracts)}")
        print(f"[CONFIG] LLM calls  : {len(self.failed_contracts) * len(REPAIR_STRATEGIES)}")
        print("=" * 80 + "\n")

        start_time = time.time()

        # Group by model so we can show progress per model
        models_seen = []
        for fc in self.failed_contracts:
            if fc["model_name"] not in models_seen:
                models_seen.append(fc["model_name"])

        for model_name in models_seen:
            model_contracts = [fc for fc in self.failed_contracts
                               if fc["model_name"] == model_name]

            print(f"\n{'='*80}")
            print(f"[MODEL] {model_name}  ({len(model_contracts)} contract(s) to repair)")
            print(f"{'='*80}\n")

            if model_name not in self.repair_results:
                self.repair_results[model_name] = {}

            with yaspin(text="Starting repairs...") as spinner:
                for fc_idx, fc in enumerate(model_contracts, 1):
                    prompt_name  = fc["prompt_name"]
                    iteration_key = fc["iteration_key"]
                    iteration_num = fc["iteration_num"]

                    # Build output directory for this contract's repairs
                    contract_repair_dir = os.path.join(
                        self.repair_dir,
                        fc["model_folder"],
                        fc["prompt_folder"]
                    )
                    os.makedirs(contract_repair_dir, exist_ok=True)

                    # Initialise result structure
                    if prompt_name not in self.repair_results[model_name]:
                        self.repair_results[model_name][prompt_name] = {}

                    contract_result = {
                        "original_sol_path":    fc["sol_path"],
                        "original_compile_error": fc["compile_error"],
                        "repairs": {}
                    }

                    for strategy in REPAIR_STRATEGIES:
                        spinner.text = (
                            f"[{fc_idx}/{len(model_contracts)}] "
                            f"{prompt_name} | {iteration_key} | {strategy}"
                        )

                        strategy_result = {
                            "prompt_strategy":  strategy,
                            "response":         "",
                            "repaired_sol_path": "",
                            "compilation":      {},
                            "slither":          {},
                            "timing":           {},
                            "error":            None
                        }

                        step_start = time.time()

                        try:
                            # ── 1. Build prompt ────────────────────────────
                            repair_prompt = self._build_prompt(
                                strategy,
                                prompt_name,
                                fc["specification"],
                                fc["faulty_code"],
                                fc["compile_error"]
                            )

                            # ── 2. Call LLM ───────────────────────────────
                            llm_start = time.time()
                            api_resp  = self._call_ollama(model_name, repair_prompt)
                            llm_time  = round(time.time() - llm_start, 2)

                            raw_response = api_resp.get("response", "")
                            strategy_result["response"] = raw_response
                            strategy_result["timing"]["llm_seconds"] = llm_time

                            # ── 3. Save raw .txt response ─────────────────
                            txt_path = os.path.join(
                                contract_repair_dir,
                                f"{iteration_num}_{strategy}.txt"
                            )
                            with open(txt_path, 'w', encoding='utf-8') as f:
                                f.write(raw_response)

                            # ── 4. Extract & save .sol ────────────────────
                            repaired_code = self._extract_solidity(raw_response)
                            sol_path = os.path.join(
                                contract_repair_dir,
                                f"{iteration_num}_{strategy}.sol"
                            )
                            with open(sol_path, 'w', encoding='utf-8') as f:
                                f.write(repaired_code)
                            strategy_result["repaired_sol_path"] = sol_path

                            # ── 5. Compile ────────────────────────────────
                            comp_start = time.time()
                            compilation = self._compile(sol_path)
                            strategy_result["compilation"] = compilation
                            strategy_result["timing"]["compilation_seconds"] = round(
                                time.time() - comp_start, 2
                            )

                            # ── 6. Slither (only if compiled) ─────────────
                            if compilation["success"]:
                                slither_start = time.time()
                                slither = self._run_slither(sol_path)
                                strategy_result["slither"] = slither
                                strategy_result["timing"]["slither_seconds"] = round(
                                    time.time() - slither_start, 2
                                )
                                status_icon = "✓"
                            else:
                                status_icon = "✗"

                        except Exception as e:
                            strategy_result["error"] = str(e)
                            strategy_result["traceback"] = traceback.format_exc()
                            status_icon = "✗"

                        strategy_result["timing"]["total_seconds"] = round(
                            time.time() - step_start, 2
                        )
                        contract_result["repairs"][strategy] = strategy_result

                        comp_ok = strategy_result["compilation"].get("success", False)
                        spinner.write(
                            f"  {status_icon} [{fc_idx}/{len(model_contracts)}] "
                            f"{prompt_name} | {iteration_key} | {strategy:16} | "
                            f"compiled={'YES' if comp_ok else 'NO':3} | "
                            f"{strategy_result['timing']['total_seconds']:.1f}s"
                        )

                    self.repair_results[model_name][prompt_name][iteration_key] = contract_result

                spinner.ok(f"✓ Finished repairs for {model_name}")

        total_time = round(time.time() - start_time, 2)
        print(f"\n[TIMING] Total repair time: {total_time:.1f}s ({total_time/60:.1f} min)\n")

    # ── Aggregation ──────────────────────────────────────────────────────────────

    def aggregate_results(self) -> None:
        """
        Build self.repair_summary with per-model, per-strategy, per-prompt statistics.
        Structure mirrors the analysis_statistics in compile_and_analyze.py.
        """
        print("[AGGREGATE] Computing repair statistics...\n")

        for model_name, prompts in self.repair_results.items():
            model_stats: Dict[str, Any] = {
                "strategies": {
                    s: {
                        "repaired":              0,
                        "still_failed":          0,
                        "repair_rate":           0.0,
                        "clean_contracts":       0,
                        "vulnerabilities":       self._init_severity_dict(),
                        "total_llm_time":        0.0,
                        "avg_llm_time":          0.0,
                        "errors":                0,
                    }
                    for s in REPAIR_STRATEGIES
                },
                "total_contracts_attempted": 0,
                "prompt_details": {}
            }

            for prompt_name, iterations in prompts.items():
                prompt_stats: Dict[str, Any] = {
                    s: {
                        "repaired":        0,
                        "still_failed":    0,
                        "repair_rate":     0.0,
                        "clean_contracts": 0,
                        "vulnerabilities": self._init_severity_dict(),
                    }
                    for s in REPAIR_STRATEGIES
                }

                for iteration_key, contract_data in iterations.items():
                    model_stats["total_contracts_attempted"] += 1

                    for strategy, s_result in contract_data.get("repairs", {}).items():
                        ms  = model_stats["strategies"][strategy]
                        ps  = prompt_stats[strategy]

                        # Error during repair call itself
                        if s_result.get("error"):
                            ms["errors"]       += 1
                            ms["still_failed"] += 1
                            ps["still_failed"] += 1
                            continue

                        llm_time = s_result.get("timing", {}).get("llm_seconds", 0)
                        ms["total_llm_time"] += llm_time

                        compiled = s_result.get("compilation", {}).get("success", False)
                        if compiled:
                            ms["repaired"] += 1
                            ps["repaired"] += 1

                            # Vulnerability analysis
                            slither_stderr = s_result.get("slither", {}).get("stderr", "")
                            vulns = self._extract_vulnerabilities(slither_stderr)
                            for v in vulns:
                                sev = VULNERABILITY_SEVERITY.get(v, "Unknown")
                                if sev in ms["vulnerabilities"]:
                                    ms["vulnerabilities"][sev] += 1
                                    ps["vulnerabilities"][sev] += 1

                            if self._has_only_benign_vulns(vulns):
                                ms["clean_contracts"] += 1
                                ps["clean_contracts"]  += 1
                        else:
                            ms["still_failed"] += 1
                            ps["still_failed"] += 1

                # Compute per-strategy repair rates at prompt level
                for strategy in REPAIR_STRATEGIES:
                    ps  = prompt_stats[strategy]
                    total = ps["repaired"] + ps["still_failed"]
                    ps["repair_rate"] = round(
                        ps["repaired"] / total * 100, 2
                    ) if total > 0 else 0.0

                model_stats["prompt_details"][prompt_name] = prompt_stats

            # Compute model-level rates and averages
            total_contracts = model_stats["total_contracts_attempted"]
            for strategy in REPAIR_STRATEGIES:
                ms    = model_stats["strategies"][strategy]
                total = ms["repaired"] + ms["still_failed"]
                ms["repair_rate"] = round(
                    ms["repaired"] / total * 100, 2
                ) if total > 0 else 0.0
                ms["avg_llm_time"] = round(
                    ms["total_llm_time"] / total_contracts, 2
                ) if total_contracts > 0 else 0.0

            self.repair_summary[model_name] = model_stats

        print("[AGGREGATE] Done.\n")

    # ── Persistence ──────────────────────────────────────────────────────────────

    def save_results(self) -> None:
        """Write repair_results.json and repair_summary.json to the output directory."""
        results_path = os.path.join(self.output_dir, "repair_results.json")
        with open(results_path, 'w', encoding='utf-8') as f:
            json.dump(self.repair_results, f, indent=2)
        print(f"[SAVED] {results_path}")

        summary_path = os.path.join(self.output_dir, "repair_summary.json")
        with open(summary_path, 'w', encoding='utf-8') as f:
            json.dump({
                "timestamp":      datetime.now().isoformat(),
                "strategies":     REPAIR_STRATEGIES,
                "repair_summary": self.repair_summary,
            }, f, indent=2)
        print(f"[SAVED] {summary_path}")

    # ── Human-readable report ────────────────────────────────────────────────────

    def generate_report(self) -> None:
        """Write repair_report.txt and print a quick summary to console."""

        # ── Detailed report ──────────────────────────────────────────────────────
        report_path = os.path.join(self.output_dir, "repair_report.txt")
        with open(report_path, 'w', encoding='utf-8') as f:

            f.write("=" * 80 + "\n")
            f.write(" " * 22 + "REPAIR MECHANISM – ANALYSIS REPORT\n")
            f.write("=" * 80 + "\n")
            f.write(f"Generated : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Strategies: {', '.join(REPAIR_STRATEGIES)}\n\n")

            for model_name, model_stats in self.repair_summary.items():
                f.write("\n" + "=" * 80 + "\n")
                f.write(f"MODEL: {model_name}\n")
                f.write("=" * 80 + "\n")
                f.write(f"  Total failed contracts attempted: "
                        f"{model_stats['total_contracts_attempted']}\n\n")

                # Per-strategy summary table
                f.write(f"  {'STRATEGY':<20} {'REPAIRED':>8} {'FAILED':>8} "
                        f"{'RATE':>8} {'CLEAN':>8} {'HIGH':>6} {'MED':>6} "
                        f"{'LOW':>6} {'AVG_LLM':>9}\n")
                f.write("  " + "-" * 78 + "\n")

                for strategy in REPAIR_STRATEGIES:
                    ms = model_stats["strategies"][strategy]
                    f.write(
                        f"  {strategy:<20} "
                        f"{ms['repaired']:>8} "
                        f"{ms['still_failed']:>8} "
                        f"{ms['repair_rate']:>7.1f}% "
                        f"{ms['clean_contracts']:>8} "
                        f"{ms['vulnerabilities']['High']:>6} "
                        f"{ms['vulnerabilities']['Medium']:>6} "
                        f"{ms['vulnerabilities']['Low']:>6} "
                        f"{ms['avg_llm_time']:>8.1f}s\n"
                    )
                f.write("\n")

                # Per-prompt breakdown
                f.write("  PER-PROMPT BREAKDOWN:\n")
                f.write("  " + "-" * 78 + "\n")

                for prompt_name, prompt_stats in model_stats["prompt_details"].items():
                    f.write(f"\n  [{prompt_name}]\n")
                    for strategy in REPAIR_STRATEGIES:
                        ps = prompt_stats[strategy]
                        total = ps["repaired"] + ps["still_failed"]
                        f.write(
                            f"    {strategy:<20} "
                            f"{ps['repaired']}/{total} repaired "
                            f"({ps['repair_rate']:.1f}%)  "
                            f"clean={ps['clean_contracts']}  "
                            f"H={ps['vulnerabilities']['High']} "
                            f"M={ps['vulnerabilities']['Medium']} "
                            f"L={ps['vulnerabilities']['Low']}\n"
                        )

            f.write("\n" + "=" * 80 + "\n")
            f.write("NOTE: Vulnerabilities counted only for successfully compiled repairs.\n")
            f.write("      Informational and Optimization issues excluded from 'clean' check.\n")
            f.write("=" * 80 + "\n")

        print(f"[SAVED] {report_path}")

        # ── Quick console summary ────────────────────────────────────────────────
        print("\n" + "=" * 80)
        print(" " * 25 + "REPAIR QUICK SUMMARY")
        print("=" * 80)
        for model_name, model_stats in self.repair_summary.items():
            print(f"\n[{model_name}]")
            print(f"  Failed contracts attempted : {model_stats['total_contracts_attempted']}")
            for strategy in REPAIR_STRATEGIES:
                ms = model_stats["strategies"][strategy]
                print(
                    f"  {strategy:<20}: "
                    f"{ms['repaired']} repaired / "
                    f"{ms['repaired'] + ms['still_failed']} "
                    f"({ms['repair_rate']:.1f}%)  "
                    f"clean={ms['clean_contracts']}  "
                    f"H={ms['vulnerabilities']['High']} "
                    f"M={ms['vulnerabilities']['Medium']} "
                    f"L={ms['vulnerabilities']['Low']}"
                )
        print("=" * 80 + "\n")


# ── Entry point ─────────────────────────────────────────────────────────────────

def main():
    print("=" * 80)
    print(" " * 18 + "SMART CONTRACT REPAIR MECHANISM PIPELINE")
    print("=" * 80 + "\n")

    repairer = RepairMechanism(output_dir="output")

    try:
        # Stage 1 – load all prerequisite data
        repairer.load_data()

        # Stage 2 – identify which contracts need repair
        repairer.identify_failed_contracts()

        if not repairer.failed_contracts:
            print("[INFO] No failed contracts found – nothing to repair. Exiting.")
            return

        # Stage 3 – repair loop (LLM call → save → compile → Slither)
        repairer.repair_all()

        # Stage 4 – aggregate statistics
        repairer.aggregate_results()

        # Stage 5 – persist results
        repairer.save_results()

        # Stage 6 – human-readable report
        repairer.generate_report()

        print("=" * 80)
        print("[SUCCESS] Repair mechanism pipeline complete!")
        print(f"          Results in: output/repair_results.json")
        print(f"          Summary in: output/repair_summary.json")
        print(f"          Report  in: output/repair_report.txt")
        print(f"          Repaired .sol files in: output/repairs/")
        print("=" * 80)

    except FileNotFoundError as e:
        print(f"\n[ERROR] {e}")
    except KeyboardInterrupt:
        print("\n\n[INTERRUPTED] Repair stopped by user.")
        if repairer.repair_results:
            print("[INFO] Saving partial results...")
            repairer.save_results()
    except Exception as e:
        print(f"\n[ERROR] Repair pipeline failed: {e}")
        traceback.print_exc()


if __name__ == "__main__":
    main()
