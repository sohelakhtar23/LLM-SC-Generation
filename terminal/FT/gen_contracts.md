>> python .\generate_contracts.py
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

[MODELS] ['gemma3:1b', 'granite4:1b', 'llama3.2:1b', 'qwen2.5-coder:0.5b', 'FT-Gemma-3-1B:latest', 'FT-Granite-4.0-1B:latest', 'FT-Llama-3.2-1B:latest', 'FT-Qwen2.5-Coder-0.5B:latest']
[CONFIG] Iterations per prompt: 5
[CONFIG] LLM timeout: 180s (3 minutes)
[CONFIG] Max retries: 2


================================================================================
[MODEL] Processing: gemma3:1b
================================================================================

  ✓ [1/5] Simple Lottery [Iter 1] - 5.3s (gen: 5.32s)
  ✓ [1/5] Simple Lottery [Iter 2] - 4.6s (gen: 4.63s)
  ✓ [1/5] Simple Lottery [Iter 3] - 5.1s (gen: 5.09s)
  ✓ [1/5] Simple Lottery [Iter 4] - 4.6s (gen: 4.57s)
  ✓ [1/5] Simple Lottery [Iter 5] - 5.1s (gen: 5.08s)
  ✓ [2/5] Whitelist Registry [Iter 1] - 4.5s (gen: 4.5s)
  ✓ [2/5] Whitelist Registry [Iter 2] - 4.6s (gen: 4.59s)
  ✓ [2/5] Whitelist Registry [Iter 3] - 4.2s (gen: 4.17s)
  ✓ [2/5] Whitelist Registry [Iter 4] - 4.2s (gen: 4.19s)
  ✓ [2/5] Whitelist Registry [Iter 5] - 4.1s (gen: 4.08s)
  ✓ [3/5] Dead Man Switch [Iter 1] - 4.5s (gen: 4.49s)
  ✓ [3/5] Dead Man Switch [Iter 2] - 4.8s (gen: 4.78s)
  ✓ [3/5] Dead Man Switch [Iter 3] - 5.3s (gen: 5.31s)
  ✓ [3/5] Dead Man Switch [Iter 4] - 4.4s (gen: 4.37s)
  ✓ [3/5] Dead Man Switch [Iter 5] - 4.7s (gen: 4.73s)
  ✓ [4/5] Split Payment [Iter 1] - 4.8s (gen: 4.77s)
  ✓ [4/5] Split Payment [Iter 2] - 4.7s (gen: 4.73s)
  ✓ [4/5] Split Payment [Iter 3] - 5.1s (gen: 5.1s)
  ✓ [4/5] Split Payment [Iter 4] - 5.0s (gen: 4.98s)
  ✓ [4/5] Split Payment [Iter 5] - 5.0s (gen: 4.96s)
  ✓ [5/5] Donation Tracker [Iter 1] - 4.8s (gen: 4.76s)
  ✓ [5/5] Donation Tracker [Iter 2] - 5.2s (gen: 5.2s)
  ✓ [5/5] Donation Tracker [Iter 3] - 5.2s (gen: 5.18s)
  ✓ [5/5] Donation Tracker [Iter 4] - 5.4s (gen: 5.45s)
  ✓ [5/5] Donation Tracker [Iter 5] - 5.1s (gen: 5.13s)
✓ Completed 25 contracts for gemma3:1b [5/5] Donation Tracker | Iteration 5/5

[MODEL TIME] gemma3:1b: 120.2s (2.0 minutes)

================================================================================
[MODEL] Processing: granite4:1b
================================================================================

  ✓ [1/5] Simple Lottery [Iter 1] - 8.1s (gen: 8.13s)
  ✓ [1/5] Simple Lottery [Iter 2] - 5.4s (gen: 5.4s)
  ✓ [1/5] Simple Lottery [Iter 3] - 5.7s (gen: 5.68s)
  ✓ [1/5] Simple Lottery [Iter 4] - 4.9s (gen: 4.86s)
  ✓ [1/5] Simple Lottery [Iter 5] - 5.5s (gen: 5.54s)
  ✓ [2/5] Whitelist Registry [Iter 1] - 4.6s (gen: 4.64s)
  ✓ [2/5] Whitelist Registry [Iter 2] - 4.7s (gen: 4.65s)
  ✓ [2/5] Whitelist Registry [Iter 3] - 4.6s (gen: 4.56s)
  ✓ [2/5] Whitelist Registry [Iter 4] - 4.6s (gen: 4.63s)
  ✓ [2/5] Whitelist Registry [Iter 5] - 4.7s (gen: 4.67s)
  ✓ [3/5] Dead Man Switch [Iter 1] - 6.6s (gen: 6.59s)
  ✓ [3/5] Dead Man Switch [Iter 2] - 5.8s (gen: 5.8s)
  ✓ [3/5] Dead Man Switch [Iter 3] - 5.7s (gen: 5.65s)
  ✓ [3/5] Dead Man Switch [Iter 4] - 5.6s (gen: 5.62s)
  ✓ [3/5] Dead Man Switch [Iter 5] - 6.4s (gen: 6.39s)
  ✓ [4/5] Split Payment [Iter 1] - 6.4s (gen: 6.42s)
  ✓ [4/5] Split Payment [Iter 2] - 6.7s (gen: 6.72s)
  ✓ [4/5] Split Payment [Iter 3] - 6.7s (gen: 6.73s)
  ✓ [4/5] Split Payment [Iter 4] - 7.1s (gen: 7.08s)
  ✓ [4/5] Split Payment [Iter 5] - 8.5s (gen: 8.49s)
  ✓ [5/5] Donation Tracker [Iter 1] - 6.0s (gen: 5.96s)
  ✓ [5/5] Donation Tracker [Iter 2] - 5.9s (gen: 5.87s)
  ✓ [5/5] Donation Tracker [Iter 3] - 6.1s (gen: 6.14s)
  ✓ [5/5] Donation Tracker [Iter 4] - 5.9s (gen: 5.89s)
  ✓ [5/5] Donation Tracker [Iter 5] - 5.9s (gen: 5.9s)
✓ Completed 25 contracts for granite4:1b [5/5] Donation Tracker | Iteration 5/5

[MODEL TIME] granite4:1b: 148.0s (2.5 minutes)

================================================================================
[MODEL] Processing: llama3.2:1b
================================================================================

  ✓ [1/5] Simple Lottery [Iter 1] - 6.2s (gen: 6.23s)
  ✓ [1/5] Simple Lottery [Iter 2] - 3.3s (gen: 3.28s)
  ✓ [1/5] Simple Lottery [Iter 3] - 3.6s (gen: 3.64s)
  ✓ [1/5] Simple Lottery [Iter 4] - 3.5s (gen: 3.51s)
  ✓ [1/5] Simple Lottery [Iter 5] - 3.7s (gen: 3.73s)
  ✓ [2/5] Whitelist Registry [Iter 1] - 3.2s (gen: 3.2s)
  ✓ [2/5] Whitelist Registry [Iter 2] - 3.2s (gen: 3.18s)
  ✓ [2/5] Whitelist Registry [Iter 3] - 3.2s (gen: 3.24s)
  ✓ [2/5] Whitelist Registry [Iter 4] - 3.1s (gen: 3.13s)
  ✓ [2/5] Whitelist Registry [Iter 5] - 3.1s (gen: 3.13s)
  ✓ [3/5] Dead Man Switch [Iter 1] - 4.4s (gen: 4.35s)
  ✓ [3/5] Dead Man Switch [Iter 2] - 4.6s (gen: 4.62s)
  ✓ [3/5] Dead Man Switch [Iter 3] - 4.4s (gen: 4.35s)
  ✓ [3/5] Dead Man Switch [Iter 4] - 4.4s (gen: 4.42s)
  ✓ [3/5] Dead Man Switch [Iter 5] - 5.0s (gen: 4.95s)
  ✓ [4/5] Split Payment [Iter 1] - 5.6s (gen: 5.59s)
  ✓ [4/5] Split Payment [Iter 2] - 5.4s (gen: 5.41s)
  ✓ [4/5] Split Payment [Iter 3] - 5.6s (gen: 5.61s)
  ✓ [4/5] Split Payment [Iter 4] - 4.8s (gen: 4.77s)
  ✓ [4/5] Split Payment [Iter 5] - 5.8s (gen: 5.77s)
  ✓ [5/5] Donation Tracker [Iter 1] - 5.9s (gen: 5.89s)
  ✓ [5/5] Donation Tracker [Iter 2] - 5.9s (gen: 5.94s)
  ✓ [5/5] Donation Tracker [Iter 3] - 4.2s (gen: 4.16s)
  ✓ [5/5] Donation Tracker [Iter 4] - 4.7s (gen: 4.65s)
  ✓ [5/5] Donation Tracker [Iter 5] - 3.8s (gen: 3.79s)
✓ Completed 25 contracts for llama3.2:1b [5/5] Donation Tracker | Iteration 5/5

[MODEL TIME] llama3.2:1b: 110.6s (1.8 minutes)

================================================================================
[MODEL] Processing: qwen2.5-coder:0.5b
================================================================================

  ✓ [1/5] Simple Lottery [Iter 1] - 9.2s (gen: 9.19s)
  ✓ [1/5] Simple Lottery [Iter 2] - 3.6s (gen: 3.61s)
  ✓ [1/5] Simple Lottery [Iter 3] - 3.2s (gen: 3.18s)
  ✓ [1/5] Simple Lottery [Iter 4] - 3.1s (gen: 3.09s)
  ✓ [1/5] Simple Lottery [Iter 5] - 3.6s (gen: 3.61s)
  ✓ [2/5] Whitelist Registry [Iter 1] - 3.0s (gen: 3.0s)
  ✓ [2/5] Whitelist Registry [Iter 2] - 3.4s (gen: 3.43s)
  ✓ [2/5] Whitelist Registry [Iter 3] - 3.1s (gen: 3.05s)
  ✓ [2/5] Whitelist Registry [Iter 4] - 3.0s (gen: 3.03s)
  ✓ [2/5] Whitelist Registry [Iter 5] - 3.0s (gen: 3.03s)
  ✓ [3/5] Dead Man Switch [Iter 1] - 3.2s (gen: 3.22s)
  ✓ [3/5] Dead Man Switch [Iter 2] - 3.5s (gen: 3.53s)
  ✓ [3/5] Dead Man Switch [Iter 3] - 3.0s (gen: 2.98s)
  ✓ [3/5] Dead Man Switch [Iter 4] - 3.3s (gen: 3.33s)
  ✓ [3/5] Dead Man Switch [Iter 5] - 3.1s (gen: 3.07s)
  ✓ [4/5] Split Payment [Iter 1] - 3.3s (gen: 3.3s)
  ✓ [4/5] Split Payment [Iter 2] - 3.6s (gen: 3.6s)
  ✓ [4/5] Split Payment [Iter 3] - 3.3s (gen: 3.32s)
  ✓ [4/5] Split Payment [Iter 4] - 3.5s (gen: 3.52s)
  ✓ [4/5] Split Payment [Iter 5] - 3.6s (gen: 3.59s)
  ✓ [5/5] Donation Tracker [Iter 1] - 3.4s (gen: 3.37s)
  ✓ [5/5] Donation Tracker [Iter 2] - 3.4s (gen: 3.35s)
  ✓ [5/5] Donation Tracker [Iter 3] - 3.5s (gen: 3.52s)
  ✓ [5/5] Donation Tracker [Iter 4] - 3.4s (gen: 3.44s)
  ✓ [5/5] Donation Tracker [Iter 5] - 3.0s (gen: 2.97s)
✓ Completed 25 contracts for qwen2.5-coder:0.5b [5/5] Donation Tracker | Iteration 5/5

[MODEL TIME] qwen2.5-coder:0.5b: 88.4s (1.5 minutes)

================================================================================
[MODEL] Processing: FT-Gemma-3-1B:latest
================================================================================

  ✓ [1/5] Simple Lottery [Iter 1] - 5.9s (gen: 5.93s)
  ✓ [1/5] Simple Lottery [Iter 2] - 4.1s (gen: 4.11s)
  ✓ [1/5] Simple Lottery [Iter 3] - 4.8s (gen: 4.79s)
  ✓ [1/5] Simple Lottery [Iter 4] - 4.5s (gen: 4.51s)
  ✓ [1/5] Simple Lottery [Iter 5] - 4.0s (gen: 3.96s)
  ✓ [2/5] Whitelist Registry [Iter 1] - 3.8s (gen: 3.84s)
  ✓ [2/5] Whitelist Registry [Iter 2] - 79.9s (gen: 79.93s)
  ✓ [2/5] Whitelist Registry [Iter 3] - 4.0s (gen: 4.01s)
  ✓ [2/5] Whitelist Registry [Iter 4] - 3.8s (gen: 3.81s)
  ✓ [2/5] Whitelist Registry [Iter 5] - 4.2s (gen: 4.25s)
  ✓ [3/5] Dead Man Switch [Iter 1] - 3.9s (gen: 3.86s)
  ✓ [3/5] Dead Man Switch [Iter 2] - 3.8s (gen: 3.78s)
  ✓ [3/5] Dead Man Switch [Iter 3] - 3.9s (gen: 3.9s)
  ✓ [3/5] Dead Man Switch [Iter 4] - 3.9s (gen: 3.92s)
  ✓ [3/5] Dead Man Switch [Iter 5] - 3.6s (gen: 3.6s)
  ✓ [4/5] Split Payment [Iter 1] - 4.4s (gen: 4.37s)
  ✓ [4/5] Split Payment [Iter 2] - 3.9s (gen: 3.91s)
  ✓ [4/5] Split Payment [Iter 3] - 3.8s (gen: 3.75s)
  ✓ [4/5] Split Payment [Iter 4] - 4.2s (gen: 4.21s)
  ✓ [4/5] Split Payment [Iter 5] - 4.2s (gen: 4.2s)
  ✓ [5/5] Donation Tracker [Iter 1] - 3.8s (gen: 3.77s)
  ✓ [5/5] Donation Tracker [Iter 2] - 4.1s (gen: 4.11s)
  ✓ [5/5] Donation Tracker [Iter 3] - 4.6s (gen: 4.61s)
  ✓ [5/5] Donation Tracker [Iter 4] - 3.9s (gen: 3.92s)
  ✓ [5/5] Donation Tracker [Iter 5] - 4.0s (gen: 4.02s)
✓ Completed 25 contracts for FT-Gemma-3-1B:latest [5/5] Donation Tracker | Iteration 5/5

[MODEL TIME] FT-Gemma-3-1B:latest: 179.1s (3.0 minutes)

================================================================================
[MODEL] Processing: FT-Granite-4.0-1B:latest
================================================================================

  ✓ [1/5] Simple Lottery [Iter 1] - 11.4s (gen: 11.43s)
  ✓ [1/5] Simple Lottery [Iter 2] - 4.5s (gen: 4.49s)
  ✓ [1/5] Simple Lottery [Iter 3] - 4.2s (gen: 4.22s)
  ✓ [1/5] Simple Lottery [Iter 4] - 4.9s (gen: 4.92s)
  ✓ [1/5] Simple Lottery [Iter 5] - 5.6s (gen: 5.59s)
  ✓ [2/5] Whitelist Registry [Iter 1] - 4.2s (gen: 4.17s)
  ✓ [2/5] Whitelist Registry [Iter 2] - 4.0s (gen: 4.01s)
  ✓ [2/5] Whitelist Registry [Iter 3] - 4.1s (gen: 4.1s)
  ✓ [2/5] Whitelist Registry [Iter 4] - 4.0s (gen: 4.01s)
  ✓ [2/5] Whitelist Registry [Iter 5] - 4.3s (gen: 4.26s)
  ✓ [3/5] Dead Man Switch [Iter 1] - 4.4s (gen: 4.4s)
  ✓ [3/5] Dead Man Switch [Iter 2] - 4.9s (gen: 4.88s)
  ✓ [3/5] Dead Man Switch [Iter 3] - 4.7s (gen: 4.73s)
  ✓ [3/5] Dead Man Switch [Iter 4] - 4.9s (gen: 4.9s)
  ✓ [3/5] Dead Man Switch [Iter 5] - 5.0s (gen: 4.95s)
  ✓ [4/5] Split Payment [Iter 1] - 5.9s (gen: 5.93s)
  ✓ [4/5] Split Payment [Iter 2] - 4.8s (gen: 4.75s)
  ✓ [4/5] Split Payment [Iter 3] - 5.8s (gen: 5.79s)
  ✓ [4/5] Split Payment [Iter 4] - 4.7s (gen: 4.67s)
  ✓ [4/5] Split Payment [Iter 5] - 5.1s (gen: 5.07s)
  ✓ [5/5] Donation Tracker [Iter 1] - 4.5s (gen: 4.5s)
  ✓ [5/5] Donation Tracker [Iter 2] - 4.7s (gen: 4.65s)
  ✓ [5/5] Donation Tracker [Iter 3] - 4.7s (gen: 4.68s)
  ✓ [5/5] Donation Tracker [Iter 4] - 4.6s (gen: 4.63s)
  ✓ [5/5] Donation Tracker [Iter 5] - 5.9s (gen: 5.91s)
✓ Completed 25 contracts for FT-Granite-4.0-1B:latest [5/5] Donation Tracker | Iteration 5/5

[MODEL TIME] FT-Granite-4.0-1B:latest: 125.7s (2.1 minutes)

================================================================================
[MODEL] Processing: FT-Llama-3.2-1B:latest
================================================================================

  ✓ [1/5] Simple Lottery [Iter 1] - 11.6s (gen: 11.61s)
  ✓ [1/5] Simple Lottery [Iter 2] - 2.3s (gen: 2.33s)
  ✓ [1/5] Simple Lottery [Iter 3] - 54.9s (gen: 54.88s)
  ✓ [1/5] Simple Lottery [Iter 4] - 72.0s (gen: 72.03s)
  ✓ [1/5] Simple Lottery [Iter 5] - 72.1s (gen: 72.1s)
  ✓ [2/5] Whitelist Registry [Iter 1] - 2.5s (gen: 2.45s)
  ✓ [2/5] Whitelist Registry [Iter 2] - 38.8s (gen: 38.84s)
  ✓ [2/5] Whitelist Registry [Iter 3] - 2.4s (gen: 2.38s)
  ✓ [2/5] Whitelist Registry [Iter 4] - 2.6s (gen: 2.55s)
  ✓ [2/5] Whitelist Registry [Iter 5] - 2.3s (gen: 2.29s)
  ✓ [3/5] Dead Man Switch [Iter 1] - 72.2s (gen: 72.25s)
  ✓ [3/5] Dead Man Switch [Iter 2] - 2.5s (gen: 2.53s)
  ✓ [3/5] Dead Man Switch [Iter 3] - 2.4s (gen: 2.39s)
  ✓ [3/5] Dead Man Switch [Iter 4] - 2.5s (gen: 2.49s)
  ✓ [3/5] Dead Man Switch [Iter 5] - 71.9s (gen: 71.94s)
  ✓ [4/5] Split Payment [Iter 1] - 70.8s (gen: 70.78s)
  ✓ [4/5] Split Payment [Iter 2] - 4.4s (gen: 4.36s)
  ✓ [4/5] Split Payment [Iter 3] - 13.5s (gen: 13.51s)
  ✓ [4/5] Split Payment [Iter 4] - 71.4s (gen: 71.43s)
  ✓ [4/5] Split Payment [Iter 5] - 4.6s (gen: 4.62s)
  ✓ [5/5] Donation Tracker [Iter 1] - 71.7s (gen: 71.71s)
  ✓ [5/5] Donation Tracker [Iter 2] - 72.0s (gen: 72.01s)
  ✓ [5/5] Donation Tracker [Iter 3] - 3.5s (gen: 3.53s)
  ✓ [5/5] Donation Tracker [Iter 4] - 71.8s (gen: 71.79s)
  ✓ [5/5] Donation Tracker [Iter 5] - 3.4s (gen: 3.43s)
✓ Completed 25 contracts for FT-Llama-3.2-1B:latest [5/5] Donation Tracker | Iteration 5/5

[MODEL TIME] FT-Llama-3.2-1B:latest: 800.3s (13.3 minutes)

================================================================================
[MODEL] Processing: FT-Qwen2.5-Coder-0.5B:latest
================================================================================

  ✓ [1/5] Simple Lottery [Iter 1] - 4.5s (gen: 4.52s)
  ✓ [1/5] Simple Lottery [Iter 2] - 3.1s (gen: 3.1s)
  ✓ [1/5] Simple Lottery [Iter 3] - 3.0s (gen: 3.02s)
  ✓ [1/5] Simple Lottery [Iter 4] - 3.2s (gen: 3.21s)
  ✓ [1/5] Simple Lottery [Iter 5] - 3.3s (gen: 3.28s)
  ✓ [2/5] Whitelist Registry [Iter 1] - 3.0s (gen: 2.98s)
  ✓ [2/5] Whitelist Registry [Iter 2] - 3.0s (gen: 2.97s)
  ✓ [2/5] Whitelist Registry [Iter 3] - 3.0s (gen: 2.96s)
  ✓ [2/5] Whitelist Registry [Iter 4] - 2.8s (gen: 2.85s)
  ✓ [2/5] Whitelist Registry [Iter 5] - 2.9s (gen: 2.86s)
  ✓ [3/5] Dead Man Switch [Iter 1] - 3.2s (gen: 3.18s)
  ✓ [3/5] Dead Man Switch [Iter 2] - 3.2s (gen: 3.17s)
  ✓ [3/5] Dead Man Switch [Iter 3] - 3.6s (gen: 3.55s)
  ✓ [3/5] Dead Man Switch [Iter 4] - 2.9s (gen: 2.87s)
  ✓ [3/5] Dead Man Switch [Iter 5] - 3.2s (gen: 3.19s)
  ✓ [4/5] Split Payment [Iter 1] - 3.1s (gen: 3.11s)
  ✓ [4/5] Split Payment [Iter 2] - 3.1s (gen: 3.14s)
  ✓ [4/5] Split Payment [Iter 3] - 3.1s (gen: 3.1s)
  ✓ [4/5] Split Payment [Iter 4] - 3.2s (gen: 3.22s)
  ✓ [4/5] Split Payment [Iter 5] - 3.1s (gen: 3.06s)
  ✓ [5/5] Donation Tracker [Iter 1] - 3.3s (gen: 3.33s)
  ✓ [5/5] Donation Tracker [Iter 2] - 3.3s (gen: 3.33s)
  ✓ [5/5] Donation Tracker [Iter 3] - 3.1s (gen: 3.06s)
  ✓ [5/5] Donation Tracker [Iter 4] - 3.2s (gen: 3.21s)
  ✓ [5/5] Donation Tracker [Iter 5] - 3.3s (gen: 3.27s)
✓ Completed 25 contracts for FT-Qwen2.5-Coder-0.5B:latest [5/5] Donation Tracker | Iteration 5/5

[MODEL TIME] FT-Qwen2.5-Coder-0.5B:latest: 79.6s (1.3 minutes)

================================================================================
                              SUMMARY
================================================================================

[STATISTICS]
  Total prompts:              5
  Successful generations:     200
  Failed generations:         0
  Generation success rate:    100.0%

[TIMING]
  Total execution time:       1652.0s
                              (27.5 minutes)

[MODEL TIMES]
  gemma3:1b                 120.2s (2.0 min)
  granite4:1b               148.0s (2.5 min)
  llama3.2:1b               110.6s (1.8 min)
  qwen2.5-coder:0.5b        88.4s (1.5 min)
  FT-Gemma-3-1B:latest      179.1s (3.0 min)
  FT-Granite-4.0-1B:latest  125.7s (2.1 min)
  FT-Llama-3.2-1B:latest    800.3s (13.3 min)
  FT-Qwen2.5-Coder-0.5B:latest 79.6s (1.3 min)
================================================================================


[SAVED] Results: fine-tuning/compare-results\generation_results.json
[SAVED] Summary: fine-tuning/compare-results\generation_summary.json
(.venv) PS C:\sohel\LLM-SC-Generation> 