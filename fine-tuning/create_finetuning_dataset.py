import os
import sys
import json
import re
from typing import Dict, List, Any, Tuple
from collections import defaultdict
from datetime import datetime
import pandas as pd

# Add the parent directory to sys.path
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

from constant import VULNERABILITY_SEVERITY_MAPPING

# ── Configuration ──────────────────────────────────────────────────────────────
OUTPUT_DIR = "output"
DATASET_DIR = "FT_dataset"

# Quality thresholds
MIN_QUALITY_SCORE = 0.7  # 0.0 to 1.0
MAX_VULNERABILITIES_ALLOWED = 0  # For generation task
MAX_VULNERABILITIES_AFTER_REPAIR = 1  # For repair tasks

# Vulnerability severity weights (for quality scoring)
SEVERITY_WEIGHTS = {
    "High": 1.0,
    "Medium": 0.5,
    "Low": 0.2,
    "Informational": 0.0,
    "Optimization": 0.0
}
MALIGN_SEVERITIES = ["High", "Medium", "Low"]


class DatasetBuilder:
    def __init__(self, output_dir: str = OUTPUT_DIR):
        self.output_dir = output_dir
        self.dataset_dir = DATASET_DIR
        
        # Loaded data
        self.compilation_results = {}
        self.generation_summary = {}
        self.repair_compilation_results = {}
        self.repair_vulnerability_results = {}
        
        # Spec lookup
        self.spec_lookup = {}
        
        # Collected examples
        self.examples = []
        
        # Statistics
        self.stats = {
            "generation": {"total": 0, "high_quality": 0, "used": 0},
            "compilation_repair": {"total": 0, "high_quality": 0, "used": 0},
            "vulnerability_repair": {"total": 0, "high_quality": 0, "used": 0}
        }

    # ── Data Loading ────────────────────────────────────────────────────────────

    def load_all_data(self) -> None:
        """Load all experiment results."""
        print("[LOAD] Reading experiment results...")
        
        # Compilation results (required)
        comp_path = os.path.join(self.output_dir, "compilation_results.json")
        if not os.path.exists(comp_path):
            raise FileNotFoundError(f"Required file not found: {comp_path}")
        with open(comp_path, 'r', encoding='utf-8') as f:
            self.compilation_results = json.load(f)
        print(f"  ✓ Loaded compilation_results.json")
        
        # Generation summary (required for specs and folder mapping)
        summary_path = os.path.join(self.output_dir, "generation_summary.json")
        if not os.path.exists(summary_path):
            raise FileNotFoundError(f"Required file not found: {summary_path}")
        with open(summary_path, 'r', encoding='utf-8') as f:
            self.generation_summary = json.load(f)
        print(f"  ✓ Loaded generation_summary.json")
        
        # Compilation repair results (optional)
        repair_comp_path = os.path.join(self.output_dir, "repair_cp_results.json")
        if os.path.exists(repair_comp_path):
            with open(repair_comp_path, 'r', encoding='utf-8') as f:
                self.repair_compilation_results = json.load(f)
            print(f"  ✓ Loaded repair_cp_results.json")
        else:
            print(f"  ⚠ repair_cp_results.json not found (skipping compilation repair examples)")
        
        # Vulnerability repair results (optional)
        repair_vuln_path = os.path.join(self.output_dir, "repair_vul_results.json")
        if os.path.exists(repair_vuln_path):
            with open(repair_vuln_path, 'r', encoding='utf-8') as f:
                self.repair_vulnerability_results = json.load(f)
            print(f"  ✓ Loaded repair_vul_results.json")
        else:
            print(f"  ⚠ repair_vul_results.json not found (skipping vulnerability repair examples)")
        print()


    def load_specifications(self, dataset_path: str) -> None:
        """Load specifications from CSV."""
        print(f"[LOAD] Reading specifications from {dataset_path}...")
        if not os.path.exists(dataset_path):
            raise FileNotFoundError(f"Dataset CSV not found: {dataset_path}")
        
        df = pd.read_csv(dataset_path, encoding='latin1')
        for i in range(df.shape[0]):
            task = df.iat[i, 0]
            spec = df.iat[i, 1]
            self.spec_lookup[task] = spec
        print(f"  ✓ Loaded {len(self.spec_lookup)} specifications\n")

    # ── Vulnerability Extraction ────────────────────────────────────────────────

    def extract_vulnerabilities(self, slither_stderr: str) -> List[str]:
        """Extract vulnerability types from Slither stderr."""
        vulnerabilities = []
        base_url = "https://github.com/crytic/slither/wiki/detector-documentation#"
        
        stderr_lower = slither_stderr.lower()
        
        for vuln_type in VULNERABILITY_SEVERITY_MAPPING.keys():
            vuln_url = f"{base_url}{vuln_type}\n"
            count = stderr_lower.count(vuln_url.lower())
            if count > 0:
                vulnerabilities.extend([vuln_type] * count)
        return vulnerabilities

    def count_malign_vulnerabilities(self, vulnerabilities: List[str]) -> int:
        """Count High/Medium/Low severity vulnerabilities."""
        count = 0
        for vuln in vulnerabilities:
            severity = VULNERABILITY_SEVERITY_MAPPING.get(vuln, "Unknown")
            if severity in MALIGN_SEVERITIES:
                count += 1
        return count

    def calculate_vulnerability_score(self, vulnerabilities: List[str]) -> float:
        """Calculate quality score based on vulnerabilities (0 = worst, 1 = best)."""
        if not vulnerabilities:
            return 1.0
        
        total_penalty = 0.0
        for vuln in vulnerabilities:
            severity = VULNERABILITY_SEVERITY_MAPPING.get(vuln, "Unknown")
            weight = SEVERITY_WEIGHTS.get(severity, 0.5)
            total_penalty += weight
        
        # Normalize: more vulnerabilities = lower score
        # Max penalty of 10 vulnerabilities before score hits 0
        score = max(0.0, 1.0 - (total_penalty / 10.0))
        return score


    # ── Example Collection ──────────────────────────────────────────────────────

    def collect_generation_examples(self) -> None:
        """Collect high-quality examples from initial generation."""
        print("[COLLECT] Extracting generation examples...")
        
        for model_name, model_data in self.compilation_results.items():
            for prompt_name, iterations in model_data.items():
                spec = self.spec_lookup.get(prompt_name, "")
                
                for iteration_key, iteration_data in iterations.items():
                    self.stats["generation"]["total"] += 1
                    
                    # Check if generation was successful
                    generation = iteration_data.get("generation", {})
                    if generation.get("error"):
                        continue
                    
                    # Check if compilation was successful
                    compilation = iteration_data.get("compilation", {})
                    if not compilation.get("success"):
                        continue
                    
                    # Extract vulnerabilities
                    slither_data = iteration_data.get("slither", {})
                    slither_stderr = slither_data.get("stderr", "")
                    vulnerabilities = self.extract_vulnerabilities(slither_stderr)
                    malign_count = self.count_malign_vulnerabilities(vulnerabilities)
                    
                    # Quality check: compiled + clean (or very few vulnerabilities)
                    if malign_count > MAX_VULNERABILITIES_ALLOWED:
                        continue
                    
                    self.stats["generation"]["high_quality"] += 1
                    
                    # Calculate quality score
                    vuln_score = self.calculate_vulnerability_score(vulnerabilities)
                    quality_score = vuln_score  # Could combine other factors
                    
                    if quality_score < MIN_QUALITY_SCORE:
                        continue
                    
                    # Get the generated code
                    code = generation.get("solidity_code", "")
                    if not code.strip():
                        continue
                    
                    # Create training example
                    example = {
                        "task_type": "generation",
                        "instruction": (
                            "You are an expert Solidity developer. Generate a complete, "
                            "production-ready smart contract based on the following specification."
                        ),
                        "input": f"Task: {prompt_name}\n\nSpecification: {spec}",
                        "output": code,
                        "metadata": {
                            "model_source": model_name,
                            "prompt_name": prompt_name,
                            "iteration": iteration_key,
                            "quality_score": round(quality_score, 3),
                            "compiled": True,
                            "malign_vulnerabilities": malign_count,
                            "total_vulnerabilities": len(vulnerabilities)
                        }
                    }
                    
                    self.examples.append(example)
                    self.stats["generation"]["used"] += 1
        
        print(f"  ✓ Collected {self.stats['generation']['used']} generation examples "
              f"({self.stats['generation']['high_quality']} high-quality / "
              f"{self.stats['generation']['total']} total)\n")


    def collect_compilation_repair_examples(self) -> None:
        """Collect successful compilation repair examples."""
        if not self.repair_compilation_results:
            print("[COLLECT] Skipping compilation repair examples (no data)\n")
            return
        
        print("[COLLECT] Extracting compilation repair examples...")
        
        for model_name, model_data in self.repair_compilation_results.items():
            for prompt_name, prompt_data in model_data.items():
                spec = self.spec_lookup.get(prompt_name, "")
                
                for iteration_key, iteration_data in prompt_data.items():
                    # Try each strategy and pick the best one
                    best_example = None
                    best_score = -1.0

                    # faulty_code and compile_error live at the contract level,
                    # not inside individual strategy results
                    faulty_code   = ""
                    original_sol_path = iteration_data.get("original_sol_path", "")
                    if original_sol_path and not os.path.isabs(original_sol_path):
                        original_sol_path = os.path.join(ROOT_DIR, original_sol_path)
                    if original_sol_path and os.path.exists(original_sol_path):
                        with open(original_sol_path, 'r', encoding='utf-8') as f:
                            faulty_code = f.read()
                    compile_error = iteration_data.get("original_compile_error", "")

                    # strategies are nested under "repairs", not at the top level
                    repairs = iteration_data.get("repairs", {})

                    for strategy in ["direct_fix", "chain_of_thought", "role_based"]:
                        if strategy not in repairs:
                            continue
                        
                        self.stats["compilation_repair"]["total"] += 1
                        result = repairs[strategy]
                        
                        # Must have compiled successfully after repair
                        compilation = result.get("compilation", {})
                        if not compilation.get("success"):
                            continue
                        
                        # Extract vulnerabilities from repaired contract
                        slither_data = result.get("slither", {})
                        slither_stderr = slither_data.get("stderr", "")
                        vulnerabilities = self.extract_vulnerabilities(slither_stderr)
                        malign_count = self.count_malign_vulnerabilities(vulnerabilities)
                        
                        # Quality check
                        if malign_count > MAX_VULNERABILITIES_AFTER_REPAIR:
                            continue
                        
                        self.stats["compilation_repair"]["high_quality"] += 1
                        
                        # Calculate quality score
                        vuln_score = self.calculate_vulnerability_score(vulnerabilities)
                        quality_score = vuln_score
                        
                        if quality_score > best_score:
                            best_score = quality_score

                            # repaired_code lives on disk; path is in the strategy result
                            repaired_code = ""
                            repaired_sol_path = result.get("repaired_sol_path", "")
                            if repaired_sol_path and not os.path.isabs(repaired_sol_path):
                                repaired_sol_path = os.path.join(ROOT_DIR, repaired_sol_path)
                            if repaired_sol_path and os.path.exists(repaired_sol_path):
                                with open(repaired_sol_path, 'r', encoding='utf-8') as f:
                                    repaired_code = f.read()
                            
                            if not repaired_code.strip():
                                continue
                            
                            best_example = {
                                "task_type": "compilation_repair",
                                "instruction": (
                                    "You are an expert Solidity developer. Fix the compilation errors "
                                    "in the following smart contract while preserving its functionality."
                                ),
                                "input": (
                                    f"Task: {prompt_name}\n\n"
                                    f"Specification: {spec}\n\n"
                                    f"Faulty Contract:\n{faulty_code}\n\n"
                                    f"Compilation Errors:\n{compile_error}"
                                ),
                                "output": repaired_code,
                                "metadata": {
                                    "model_source": model_name,
                                    "prompt_name": prompt_name,
                                    "iteration": iteration_key,
                                    "strategy": strategy,
                                    "quality_score": round(quality_score, 3),
                                    "compiled": True,
                                    "malign_vulnerabilities": malign_count,
                                    "total_vulnerabilities": len(vulnerabilities)
                                }
                            }
                    
                    # Add the best example for this contract
                    if best_example and best_score >= MIN_QUALITY_SCORE:
                        self.examples.append(best_example)
                        self.stats["compilation_repair"]["used"] += 1
        
        print(f"  ✓ Collected {self.stats['compilation_repair']['used']} compilation repair examples "
              f"({self.stats['compilation_repair']['high_quality']} high-quality / "
              f"{self.stats['compilation_repair']['total']} total)\n")


    def collect_vulnerability_repair_examples(self) -> None:
        """Collect successful vulnerability repair examples."""
        if not self.repair_vulnerability_results:
            print("[COLLECT] Skipping vulnerability repair examples (no data)\n")
            return
        
        print("[COLLECT] Extracting vulnerability repair examples...")
        
        for model_name, model_data in self.repair_vulnerability_results.items():
            for prompt_name, prompt_data in model_data.items():
                # spec = self.spec_lookup.get(prompt_name, "")
                
                for iteration_key, iteration_data in prompt_data.items():
                    # Try each strategy and pick the best one
                    best_example = None
                    best_score = -1.0
                    
                    for strategy in ["direct_fix", "chain_of_thought", "role_based"]:
                        if strategy not in iteration_data:
                            continue
                        
                        self.stats["vulnerability_repair"]["total"] += 1
                        result = iteration_data[strategy]
                        
                        # Must have compiled successfully
                        compilation = result.get("compilation", {})
                        if not compilation.get("success"):
                            continue
                        
                        # Check vulnerability reduction
                        original_malign = result.get("original_total_malign", 0)
                        repaired_malign = result.get("repaired_total_malign", 0)
                        
                        # Must have improvement
                        if repaired_malign >= original_malign:
                            continue
                        
                        # Quality check
                        if repaired_malign > MAX_VULNERABILITIES_AFTER_REPAIR:
                            continue
                        
                        self.stats["vulnerability_repair"]["high_quality"] += 1
                        
                        # Calculate quality score based on vulnerability reduction
                        repaired_vulns = result.get("repaired_vulnerabilities", [])
                        vuln_score = self.calculate_vulnerability_score(repaired_vulns)
                        
                        # Bonus for complete fix
                        reduction_ratio = 1.0 - (repaired_malign / max(original_malign, 1))
                        quality_score = (vuln_score + reduction_ratio) / 2.0
                        
                        if quality_score > best_score:
                            best_score = quality_score
                            
                            # Get codes and vulnerabilities
                            original_code = result.get("original_code", "")
                            # If original_code not in result, we need to construct it
                            # This might need adjustment based on actual data structure
                            
                            original_vulns = result.get("original_vulnerabilities", [])
                            repaired_code = result.get("repaired_code", "")
                            
                            if not repaired_code.strip():
                                continue
                            
                            # Format vulnerability list
                            vuln_list = []
                            for vuln in set(original_vulns):
                                count = original_vulns.count(vuln)
                                severity = VULNERABILITY_SEVERITY_MAPPING.get(vuln, "Unknown")
                                vuln_list.append(f"  - [{severity}] {vuln} ({count}x)")
                            vuln_text = "\n".join(vuln_list)
                            
                            best_example = {
                                "task_type": "vulnerability_repair",
                                "instruction": (
                                    "You are a senior smart contract security auditor. Fix all security "
                                    "vulnerabilities in the following contract while preserving its functionality."
                                ),
                                "input": (
                                    f"Task: {prompt_name}\n\n"
                                    # f"Specification: {spec}\n\n"
                                    f"Vulnerabilities Detected:\n{vuln_text}\n\n"
                                    f"Vulnerable Contract:\n{original_code if original_code else '[code would be here]'}"
                                ),
                                "output": repaired_code,
                                "metadata": {
                                    "model_source": model_name,
                                    "prompt_name": prompt_name,
                                    "iteration": iteration_key,
                                    "strategy": strategy,
                                    "quality_score": round(quality_score, 3),
                                    "compiled": True,
                                    "original_malign_vulnerabilities": original_malign,
                                    "repaired_malign_vulnerabilities": repaired_malign,
                                    "reduction_ratio": round(reduction_ratio, 3)
                                }
                            }
                    
                    # Add the best example for this contract
                    if best_example and best_score >= MIN_QUALITY_SCORE:
                        self.examples.append(best_example)
                        self.stats["vulnerability_repair"]["used"] += 1
        
        print(f"  ✓ Collected {self.stats['vulnerability_repair']['used']} vulnerability repair examples "
              f"({self.stats['vulnerability_repair']['high_quality']} high-quality / "
              f"{self.stats['vulnerability_repair']['total']} total)\n")

    # ── Dataset Export ──────────────────────────────────────────────────────────

    def export_dataset(self, formats: List[str] = ["jsonl"]) -> None:
        """Export dataset in multiple formats."""
        os.makedirs(self.dataset_dir, exist_ok=True)
        
        print(f"[EXPORT] Saving dataset to {self.dataset_dir}/")        
        # 1. JSONL format (one example per line)
        if "jsonl" in formats:
            jsonl_path = os.path.join(self.dataset_dir, "dataset.jsonl")
            with open(jsonl_path, 'w', encoding='utf-8') as f:
                for example in self.examples:
                    f.write(json.dumps(example, ensure_ascii=False) + "\n")
            print(f"  ✓ Saved JSONL format: {jsonl_path}")

        # 2. Split by task type
        task_splits = defaultdict(list)
        for example in self.examples:
            task_splits[example["task_type"]].append(example)
        
        for task_type, examples in task_splits.items():
            task_path = os.path.join(self.dataset_dir, f"dataset_{task_type}.jsonl")
            with open(task_path, 'w', encoding='utf-8') as f:
                for example in examples:
                    f.write(json.dumps(example, ensure_ascii=False) + "\n")
            print(f"  ✓ Saved {task_type} split: {task_path} ({len(examples)} examples)")  
        print()


    def export_statistics(self) -> None:
        """Export dataset statistics and quality report."""
        stats_path = os.path.join(self.dataset_dir, "dataset_statistics.json")
        
        # Compute distribution statistics
        task_distribution = defaultdict(int)
        model_distribution = defaultdict(int)
        quality_scores = []
        
        for example in self.examples:
            task_distribution[example["task_type"]] += 1
            model_distribution[example["metadata"]["model_source"]] += 1
            quality_scores.append(example["metadata"]["quality_score"])
        
        statistics = {
            "timestamp": datetime.now().isoformat(),
            "total_examples": len(self.examples),
            "task_distribution": dict(task_distribution),
            "model_distribution": dict(model_distribution),
            "collection_stats": self.stats,
            "quality_statistics": {
                "mean_quality_score": round(sum(quality_scores) / len(quality_scores), 3) if quality_scores else 0,
                "min_quality_score": round(min(quality_scores), 3) if quality_scores else 0,
                "max_quality_score": round(max(quality_scores), 3) if quality_scores else 0,
            },
            "configuration": {
                "min_quality_score": MIN_QUALITY_SCORE,
                "max_vulnerabilities_allowed": MAX_VULNERABILITIES_ALLOWED,
                "max_vulnerabilities_after_repair": MAX_VULNERABILITIES_AFTER_REPAIR
            }
        }
        
        with open(stats_path, 'w', encoding='utf-8') as f:
            json.dump(statistics, f, indent=2, ensure_ascii=False)        
        print(f"[EXPORT] Statistics saved to {stats_path}\n")
        
        # Print summary to console
        print("=" * 80)
        print(" " * 25 + "DATASET STATISTICS")
        print("=" * 80)
        print(f"\nTotal Examples: {statistics['total_examples']}")
        print(f"\nTask Distribution:")
        for task, count in statistics['task_distribution'].items():
            pct = (count / statistics['total_examples']) * 100
            print(f"  {task:25} {count:5} ({pct:5.1f}%)")
        
        print(f"\nModel Distribution:")
        for model, count in sorted(statistics['model_distribution'].items()):
            pct = (count / statistics['total_examples']) * 100
            print(f"  {model:25} {count:5} ({pct:5.1f}%)")
        
        print(f"\nQuality Statistics:")
        print(f"  Mean Quality Score: {statistics['quality_statistics']['mean_quality_score']}")
        print(f"  Min Quality Score:  {statistics['quality_statistics']['min_quality_score']}")
        print(f"  Max Quality Score:  {statistics['quality_statistics']['max_quality_score']}")
        
        print(f"\nCollection Efficiency:")
        for task_type, counts in self.stats.items():
            if counts['total'] > 0:
                efficiency = (counts['used'] / counts['total']) * 100
                print(f"  {task_type:25} {counts['used']:4}/{counts['total']:4} used ({efficiency:5.1f}%)")        
        print("=" * 80 + "\n")

    # ── Main Pipeline ───────────────────────────────────────────────────────────

    def build_dataset(self) -> None:
        """Main dataset building pipeline."""
        print("=" * 80)
        print(" " * 20 + "FINE-TUNING DATASET BUILDER")
        print("=" * 80 + "\n")
        
        # Load all data
        self.load_all_data()
        self.load_specifications(dataset_path="../prompts_final.csv")
        
        # Collect examples from each source
        self.collect_generation_examples()
        self.collect_compilation_repair_examples()
        self.collect_vulnerability_repair_examples()
        
        if not self.examples:
            print("[WARNING] No examples collected! Check quality thresholds.\n")
            return
        
        self.export_dataset(formats=["jsonl"])
        self.export_statistics()
        
        print("=" * 80)
        print("[SUCCESS] Dataset building complete!")
        print(f"          Total examples: {len(self.examples)}")
        print(f"          Output directory: {self.dataset_dir}/")
        print("=" * 80)


def main():
    builder = DatasetBuilder(output_dir="../output")
    
    try:
        builder.build_dataset()
    except FileNotFoundError as e:
        print(f"\n[ERROR] {e}")
        print("Make sure you have run the previous pipeline steps.")
    except Exception as e:
        print(f"\n[ERROR] Dataset building failed: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()