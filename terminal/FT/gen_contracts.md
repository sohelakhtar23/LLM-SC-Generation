(.venv) PS C:\sohel\LLM-SC-Generation> python .\generate_contracts.py
================================================================================
                    SOLIDITY CONTRACT GENERATION
================================================================================

[INFO] Output directory cleaned and created: fine-tuning/compare-results

[DATASET] Loading: fine-tuning/new_exercises.csv
[DATASET] Total prompts: 5

[PROMPTS]
  [1] Simple Lottery: 778 chars
  [2] Whitelist Registry: 638 chars
  [3] Dead Man Switch: 796 chars
  [4] Split Payment: 838 chars
  [5] Donation Tracker: 808 chars

[MODELS] ['granite4:1b', 'llama3.2:1b', 'qwen2.5-coder:0.5b', 'FT-Granite-4.0-1B:latest', 'FT-Llama-3.2-1B:latest', 'FT-Qwen2.5-Coder-0.5B:latest']
[CONFIG] Iterations per prompt: 5
[CONFIG] LLM timeout: 180s (3 minutes)
[CONFIG] Max retries: 2


================================================================================
[MODEL] Processing: granite4:1b
================================================================================

  ✓ [1/5] Simple Lottery [Iter 1] - 7.7s (gen: 7.73s)
  ✓ [1/5] Simple Lottery [Iter 2] - 5.7s (gen: 5.67s)
  ✓ [1/5] Simple Lottery [Iter 3] - 4.8s (gen: 4.83s)
  ✓ [1/5] Simple Lottery [Iter 4] - 5.7s (gen: 5.68s)
  ✓ [1/5] Simple Lottery [Iter 5] - 6.5s (gen: 6.47s)
  ✓ [2/5] Whitelist Registry [Iter 1] - 4.6s (gen: 4.64s)
  ✓ [2/5] Whitelist Registry [Iter 2] - 4.7s (gen: 4.66s)
  ✓ [2/5] Whitelist Registry [Iter 3] - 4.6s (gen: 4.57s)
  ✓ [2/5] Whitelist Registry [Iter 4] - 4.7s (gen: 4.65s)
  ✓ [2/5] Whitelist Registry [Iter 5] - 4.7s (gen: 4.68s)
  ✓ [3/5] Dead Man Switch [Iter 1] - 5.6s (gen: 5.56s)
  ✓ [3/5] Dead Man Switch [Iter 2] - 6.3s (gen: 6.31s)
  ✓ [3/5] Dead Man Switch [Iter 3] - 5.2s (gen: 5.21s)
  ✓ [3/5] Dead Man Switch [Iter 4] - 6.4s (gen: 6.36s)
  ✓ [3/5] Dead Man Switch [Iter 5] - 6.3s (gen: 6.34s)
  ✓ [4/5] Split Payment [Iter 1] - 6.0s (gen: 5.98s)
  ✓ [4/5] Split Payment [Iter 2] - 6.6s (gen: 6.55s)
  ✓ [4/5] Split Payment [Iter 3] - 6.5s (gen: 6.53s)
  ✓ [4/5] Split Payment [Iter 4] - 6.4s (gen: 6.44s)
  ✓ [4/5] Split Payment [Iter 5] - 6.0s (gen: 6.02s)
  ✓ [5/5] Donation Tracker [Iter 1] - 5.9s (gen: 5.86s)
  ✓ [5/5] Donation Tracker [Iter 2] - 5.8s (gen: 5.83s)
  ✓ [5/5] Donation Tracker [Iter 3] - 5.9s (gen: 5.88s)
  ✓ [5/5] Donation Tracker [Iter 4] - 5.8s (gen: 5.81s)
  ✓ [5/5] Donation Tracker [Iter 5] - 6.0s (gen: 5.96s)
✓ Completed 25 contracts for granite4:1b [5/5] Donation Tracker | Iteration 5/5

[MODEL TIME] granite4:1b: 144.3s (2.4 minutes)

================================================================================
[MODEL] Processing: llama3.2:1b
================================================================================

  ✓ [1/5] Simple Lottery [Iter 1] - 4.6s (gen: 4.57s)
  ✓ [1/5] Simple Lottery [Iter 2] - 3.7s (gen: 3.67s)
  ✓ [1/5] Simple Lottery [Iter 3] - 3.5s (gen: 3.51s)
  ✓ [1/5] Simple Lottery [Iter 4] - 3.7s (gen: 3.74s)
  ✓ [1/5] Simple Lottery [Iter 5] - 3.9s (gen: 3.9s)
  ✓ [2/5] Whitelist Registry [Iter 1] - 3.4s (gen: 3.42s)
  ✓ [2/5] Whitelist Registry [Iter 2] - 3.2s (gen: 3.18s)
  ✓ [2/5] Whitelist Registry [Iter 3] - 3.3s (gen: 3.25s)
  ✓ [2/5] Whitelist Registry [Iter 4] - 3.2s (gen: 3.17s)
  ✓ [2/5] Whitelist Registry [Iter 5] - 3.2s (gen: 3.19s)
  ✓ [3/5] Dead Man Switch [Iter 1] - 4.4s (gen: 4.44s)
  ✓ [3/5] Dead Man Switch [Iter 2] - 4.7s (gen: 4.68s)
  ✓ [3/5] Dead Man Switch [Iter 3] - 4.8s (gen: 4.84s)
  ✓ [3/5] Dead Man Switch [Iter 4] - 4.4s (gen: 4.43s)
  ✓ [3/5] Dead Man Switch [Iter 5] - 4.5s (gen: 4.51s)
  ✓ [4/5] Split Payment [Iter 1] - 7.8s (gen: 7.81s)
  ✓ [4/5] Split Payment [Iter 2] - 4.3s (gen: 4.31s)
  ✓ [4/5] Split Payment [Iter 3] - 3.7s (gen: 3.69s)
  ✓ [4/5] Split Payment [Iter 4] - 4.4s (gen: 4.43s)
  ✓ [4/5] Split Payment [Iter 5] - 7.6s (gen: 7.58s)
  ✓ [5/5] Donation Tracker [Iter 1] - 4.5s (gen: 4.47s)
  ✓ [5/5] Donation Tracker [Iter 2] - 4.5s (gen: 4.49s)
  ✓ [5/5] Donation Tracker [Iter 3] - 4.1s (gen: 4.08s)
  ✓ [5/5] Donation Tracker [Iter 4] - 4.5s (gen: 4.53s)
  ✓ [5/5] Donation Tracker [Iter 5] - 4.1s (gen: 4.12s)
✓ Completed 25 contracts for llama3.2:1b [5/5] Donation Tracker | Iteration 5/5

[MODEL TIME] llama3.2:1b: 108.0s (1.8 minutes)

================================================================================
[MODEL] Processing: qwen2.5-coder:0.5b
================================================================================

  ✓ [1/5] Simple Lottery [Iter 1] - 3.9s (gen: 3.94s)
  ✓ [1/5] Simple Lottery [Iter 2] - 3.4s (gen: 3.41s)
  ✓ [1/5] Simple Lottery [Iter 3] - 3.3s (gen: 3.26s)
  ✓ [1/5] Simple Lottery [Iter 4] - 3.4s (gen: 3.36s)
  ✓ [1/5] Simple Lottery [Iter 5] - 3.2s (gen: 3.24s)
  ✓ [2/5] Whitelist Registry [Iter 1] - 3.2s (gen: 3.19s)
  ✓ [2/5] Whitelist Registry [Iter 2] - 3.0s (gen: 3.04s)
  ✓ [2/5] Whitelist Registry [Iter 3] - 3.4s (gen: 3.36s)
  ✓ [2/5] Whitelist Registry [Iter 4] - 3.2s (gen: 3.22s)
  ✓ [2/5] Whitelist Registry [Iter 5] - 3.0s (gen: 3.04s)
  ✓ [3/5] Dead Man Switch [Iter 1] - 3.0s (gen: 3.0s)
  ✓ [3/5] Dead Man Switch [Iter 2] - 3.0s (gen: 3.04s)
  ✓ [3/5] Dead Man Switch [Iter 3] - 3.3s (gen: 3.28s)
  ✓ [3/5] Dead Man Switch [Iter 4] - 3.5s (gen: 3.52s)
  ✓ [3/5] Dead Man Switch [Iter 5] - 3.2s (gen: 3.24s)
  ✓ [4/5] Split Payment [Iter 1] - 3.3s (gen: 3.34s)
  ✓ [4/5] Split Payment [Iter 2] - 3.3s (gen: 3.31s)
  ✓ [4/5] Split Payment [Iter 3] - 3.6s (gen: 3.61s)
  ✓ [4/5] Split Payment [Iter 4] - 3.7s (gen: 3.73s)
  ✓ [4/5] Split Payment [Iter 5] - 3.6s (gen: 3.61s)
  ✓ [5/5] Donation Tracker [Iter 1] - 3.6s (gen: 3.59s)
  ✓ [5/5] Donation Tracker [Iter 2] - 3.5s (gen: 3.49s)
  ✓ [5/5] Donation Tracker [Iter 3] - 3.5s (gen: 3.46s)
  ✓ [5/5] Donation Tracker [Iter 4] - 3.2s (gen: 3.21s)
  ✓ [5/5] Donation Tracker [Iter 5] - 3.3s (gen: 3.28s)
✓ Completed 25 contracts for qwen2.5-coder:0.5b [5/5] Donation Tracker | Iteration 5/5

[MODEL TIME] qwen2.5-coder:0.5b: 83.8s (1.4 minutes)

================================================================================
[MODEL] Processing: FT-Granite-4.0-1B:latest
================================================================================

  ✓ [1/5] Simple Lottery [Iter 1] - 10.2s (gen: 10.19s)
  ✓ [1/5] Simple Lottery [Iter 2] - 4.3s (gen: 4.35s)
  ✓ [1/5] Simple Lottery [Iter 3] - 5.1s (gen: 5.13s)
  ✓ [1/5] Simple Lottery [Iter 4] - 5.3s (gen: 5.25s)
  ✓ [1/5] Simple Lottery [Iter 5] - 4.7s (gen: 4.68s)
  ✓ [2/5] Whitelist Registry [Iter 1] - 4.3s (gen: 4.29s)
  ✓ [2/5] Whitelist Registry [Iter 2] - 4.8s (gen: 4.76s)
  ✓ [2/5] Whitelist Registry [Iter 3] - 4.0s (gen: 4.03s)
  ✓ [2/5] Whitelist Registry [Iter 4] - 4.1s (gen: 4.09s)
  ✓ [2/5] Whitelist Registry [Iter 5] - 4.0s (gen: 3.99s)
  ✓ [3/5] Dead Man Switch [Iter 1] - 4.6s (gen: 4.56s)
  ✓ [3/5] Dead Man Switch [Iter 2] - 4.6s (gen: 4.58s)
  ✓ [3/5] Dead Man Switch [Iter 3] - 5.2s (gen: 5.19s)
  ✓ [3/5] Dead Man Switch [Iter 4] - 4.7s (gen: 4.72s)
  ✓ [3/5] Dead Man Switch [Iter 5] - 4.7s (gen: 4.72s)
  ✓ [4/5] Split Payment [Iter 1] - 5.3s (gen: 5.33s)
  ✓ [4/5] Split Payment [Iter 2] - 7.6s (gen: 7.57s)
  ✓ [4/5] Split Payment [Iter 3] - 5.0s (gen: 4.98s)
  ✓ [4/5] Split Payment [Iter 4] - 5.3s (gen: 5.28s)
  ✓ [4/5] Split Payment [Iter 5] - 5.4s (gen: 5.37s)
  ✓ [5/5] Donation Tracker [Iter 1] - 5.5s (gen: 5.5s)
  ✓ [5/5] Donation Tracker [Iter 2] - 4.8s (gen: 4.8s)
  ✓ [5/5] Donation Tracker [Iter 3] - 4.5s (gen: 4.47s)
  ✓ [5/5] Donation Tracker [Iter 4] - 4.8s (gen: 4.77s)
  ✓ [5/5] Donation Tracker [Iter 5] - 4.4s (gen: 4.43s)
✓ Completed 25 contracts for FT-Granite-4.0-1B:latest [5/5] Donation Tracker | Iteration 5/5

[MODEL TIME] FT-Granite-4.0-1B:latest: 127.1s (2.1 minutes)

================================================================================
[MODEL] Processing: FT-Llama-3.2-1B:latest
================================================================================

  ✓ [1/5] Simple Lottery [Iter 1] - 78.1s (gen: 78.11s)
  ✓ [1/5] Simple Lottery [Iter 2] - 72.6s (gen: 72.62s)
  ✓ [1/5] Simple Lottery [Iter 3] - 72.6s (gen: 72.63s)
  ✓ [1/5] Simple Lottery [Iter 4] - 72.7s (gen: 72.73s)
  ✓ [1/5] Simple Lottery [Iter 5] - 4.6s (gen: 4.57s)
  ✓ [2/5] Whitelist Registry [Iter 1] - 4.6s (gen: 4.65s)
  ✓ [2/5] Whitelist Registry [Iter 2] - 2.3s (gen: 2.33s)
  ✓ [2/5] Whitelist Registry [Iter 3] - 2.4s (gen: 2.44s)
  ✓ [2/5] Whitelist Registry [Iter 4] - 2.3s (gen: 2.3s)
  ✓ [2/5] Whitelist Registry [Iter 5] - 2.5s (gen: 2.49s)
  ✓ [3/5] Dead Man Switch [Iter 1] - 2.5s (gen: 2.46s)
  ✓ [3/5] Dead Man Switch [Iter 2] - 4.2s (gen: 4.23s)
  ✓ [3/5] Dead Man Switch [Iter 3] - 4.0s (gen: 3.99s)
  ✓ [3/5] Dead Man Switch [Iter 4] - 2.4s (gen: 2.4s)
  ✓ [3/5] Dead Man Switch [Iter 5] - 25.6s (gen: 25.6s)
  ✓ [4/5] Split Payment [Iter 1] - 22.3s (gen: 22.27s)
  ✓ [4/5] Split Payment [Iter 2] - 12.6s (gen: 12.58s)
  ✓ [4/5] Split Payment [Iter 3] - 2.5s (gen: 2.53s)
  ✓ [4/5] Split Payment [Iter 4] - 72.1s (gen: 72.11s)
  ✓ [4/5] Split Payment [Iter 5] - 22.9s (gen: 22.94s)
  ✓ [5/5] Donation Tracker [Iter 1] - 70.9s (gen: 70.87s)
  ✓ [5/5] Donation Tracker [Iter 2] - 2.5s (gen: 2.48s)
  ✓ [5/5] Donation Tracker [Iter 3] - 84.8s (gen: 84.75s)
  ✓ [5/5] Donation Tracker [Iter 4] - 3.0s (gen: 2.99s)
  ✓ [5/5] Donation Tracker [Iter 5] - 64.2s (gen: 64.17s)
✓ Completed 25 contracts for FT-Llama-3.2-1B:latest [5/5] Donation Tracker | Iteration 5/5

[MODEL TIME] FT-Llama-3.2-1B:latest: 711.3s (11.9 minutes)

================================================================================
[MODEL] Processing: FT-Qwen2.5-Coder-0.5B:latest
================================================================================

  ✓ [1/5] Simple Lottery [Iter 1] - 10.1s (gen: 10.08s)
  ✓ [1/5] Simple Lottery [Iter 2] - 3.3s (gen: 3.31s)
  ✓ [1/5] Simple Lottery [Iter 3] - 3.6s (gen: 3.59s)
  ✓ [1/5] Simple Lottery [Iter 4] - 3.4s (gen: 3.45s)
  ✓ [1/5] Simple Lottery [Iter 5] - 3.8s (gen: 3.77s)
  ✓ [2/5] Whitelist Registry [Iter 1] - 3.3s (gen: 3.33s)
  ✓ [2/5] Whitelist Registry [Iter 2] - 3.4s (gen: 3.35s)
  ✓ [2/5] Whitelist Registry [Iter 3] - 3.1s (gen: 3.09s)
  ✓ [2/5] Whitelist Registry [Iter 4] - 3.2s (gen: 3.22s)
  ✓ [2/5] Whitelist Registry [Iter 5] - 3.2s (gen: 3.19s)
  ✓ [3/5] Dead Man Switch [Iter 1] - 3.2s (gen: 3.21s)
  ✓ [3/5] Dead Man Switch [Iter 2] - 3.1s (gen: 3.08s)
  ✓ [3/5] Dead Man Switch [Iter 3] - 3.4s (gen: 3.43s)
  ✓ [3/5] Dead Man Switch [Iter 4] - 3.1s (gen: 3.07s)
  ✓ [3/5] Dead Man Switch [Iter 5] - 3.1s (gen: 3.15s)
  ✓ [4/5] Split Payment [Iter 1] - 3.1s (gen: 3.13s)
  ✓ [4/5] Split Payment [Iter 2] - 3.1s (gen: 3.09s)
  ✓ [4/5] Split Payment [Iter 3] - 3.1s (gen: 3.12s)
  ✓ [4/5] Split Payment [Iter 4] - 3.1s (gen: 3.14s)
  ✓ [4/5] Split Payment [Iter 5] - 3.0s (gen: 3.02s)
  ✓ [5/5] Donation Tracker [Iter 1] - 3.1s (gen: 3.12s)
  ✓ [5/5] Donation Tracker [Iter 2] - 3.3s (gen: 3.25s)
  ✓ [5/5] Donation Tracker [Iter 3] - 3.1s (gen: 3.13s)
  ✓ [5/5] Donation Tracker [Iter 4] - 3.2s (gen: 3.25s)
  ✓ [5/5] Donation Tracker [Iter 5] - 3.2s (gen: 3.16s)
✓ Completed 25 contracts for FT-Qwen2.5-Coder-0.5B:latest [5/5] Donation Tracker | Iteration 5/5

[MODEL TIME] FT-Qwen2.5-Coder-0.5B:latest: 87.8s (1.5 minutes)

================================================================================
                              SUMMARY
================================================================================

[STATISTICS]
  Total prompts:              5
  Successful generations:     150
  Failed generations:         0
  Generation success rate:    100.0%

[TIMING]
  Total execution time:       1262.3s
                              (21.0 minutes)

[MODEL TIMES]
  granite4:1b               144.3s (2.4 min)
  llama3.2:1b               108.0s (1.8 min)
  qwen2.5-coder:0.5b        83.8s (1.4 min)
  FT-Granite-4.0-1B:latest  127.1s (2.1 min)
  FT-Llama-3.2-1B:latest    711.3s (11.8 min)
  FT-Qwen2.5-Coder-0.5B:latest 87.8s (1.5 min)
================================================================================


[SAVED] Results: fine-tuning/compare-results\generation_results.json
[SAVED] Summary: fine-tuning/compare-results\generation_summary.json