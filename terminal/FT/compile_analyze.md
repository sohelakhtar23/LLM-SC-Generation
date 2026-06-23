>> python .\compile_and_analyze.py
[LOADED] fine-tuning/compare-results\generation_results.json
[LOADED] fine-tuning/compare-results\generation_summary.json
[MODELS] 8 model(s) found

================================================================================
                    COMPILATION AND ANALYSIS
================================================================================


================================================================================
[MODEL] Processing: gemma3:1b
================================================================================

  ✗ Simple Lottery [iteration_0] - Compile: 0.4s
  ✗ Simple Lottery [iteration_1] - Compile: 0.2s
  ✗ Simple Lottery [iteration_2] - Compile: 0.2s
  ✗ Simple Lottery [iteration_3] - Compile: 0.2s
  ✗ Simple Lottery [iteration_4] - Compile: 0.2s
  ✗ Whitelist Registry [iteration_0] - Compile: 0.2s
  ✗ Whitelist Registry [iteration_1] - Compile: 0.2s
  ✗ Whitelist Registry [iteration_2] - Compile: 0.2s
  ✗ Whitelist Registry [iteration_3] - Compile: 0.2s
  ✗ Whitelist Registry [iteration_4] - Compile: 0.2s
  ✗ Dead Man Switch [iteration_0] - Compile: 0.2s
  ✗ Dead Man Switch [iteration_1] - Compile: 0.2s
  ✗ Dead Man Switch [iteration_2] - Compile: 0.2s
  ✗ Dead Man Switch [iteration_3] - Compile: 0.2s
  ✗ Dead Man Switch [iteration_4] - Compile: 0.2s
⠹ Processing Split Payment - iteration_0Exception in thread Thread-33 (_readerthread):
Traceback (most recent call last):
  File "C:\Users\DELL\AppData\Local\Programs\Python\Python312\Lib\threading.py", line 1073, in _bootstrap_inner
    self.run()
  File "C:\Users\DELL\AppData\Local\Programs\Python\Python312\Lib\threading.py", line 1010, in run
    self._target(*self._args, **self._kwargs)
  File "C:\Users\DELL\AppData\Local\Programs\Python\Python312\Lib\subprocess.py", line 1597, in _readerthread
    buffer.append(fh.read())
                  ^^^^^^^^^
  File "C:\Users\DELL\AppData\Local\Programs\Python\Python312\Lib\encodings\cp1254.py", line 23, in decode
    return codecs.charmap_decode(input,self.errors,decoding_table)[0]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 175: character maps to <undefined>
  ✗ Split Payment [iteration_0] - Compile: 0.2s
  ✗ Split Payment [iteration_1] - Compile: 0.2s
  ✗ Split Payment [iteration_2] - Compile: 0.2s
  ✗ Split Payment [iteration_3] - Compile: 0.2s
  ✗ Split Payment [iteration_4] - Compile: 0.2s
  ✗ Donation Tracker [iteration_0] - Compile: 0.2s
  ✗ Donation Tracker [iteration_1] - Compile: 0.2s
  ✗ Donation Tracker [iteration_2] - Compile: 0.2s
  ✗ Donation Tracker [iteration_3] - Compile: 0.2s
  ✗ Donation Tracker [iteration_4] - Compile: 0.2s
✓ Completed 25 contracts for gemma3:1b Processing Donation Tracker - iteration_4

================================================================================
[MODEL] Processing: granite4:1b
================================================================================

  ✗ Simple Lottery [iteration_0] - Compile: 0.2s
  ✗ Simple Lottery [iteration_1] - Compile: 0.2s
  ✗ Simple Lottery [iteration_2] - Compile: 0.2s
  ✗ Simple Lottery [iteration_3] - Compile: 0.2s
  ✗ Simple Lottery [iteration_4] - Compile: 0.2s
  ✗ Whitelist Registry [iteration_0] - Compile: 0.2s
  ✗ Whitelist Registry [iteration_1] - Compile: 0.2s
  ✗ Whitelist Registry [iteration_2] - Compile: 0.2s
  ✗ Whitelist Registry [iteration_3] - Compile: 0.2s
  ✗ Whitelist Registry [iteration_4] - Compile: 0.2s
  ✗ Dead Man Switch [iteration_0] - Compile: 0.2s
  ✗ Dead Man Switch [iteration_1] - Compile: 0.2s
  ✗ Dead Man Switch [iteration_2] - Compile: 0.2s
  ✗ Dead Man Switch [iteration_3] - Compile: 0.2s
  ✗ Dead Man Switch [iteration_4] - Compile: 0.2s
  ✗ Split Payment [iteration_0] - Compile: 0.2s
  ✗ Split Payment [iteration_1] - Compile: 0.2s
  ✗ Split Payment [iteration_2] - Compile: 0.2s
  ✗ Split Payment [iteration_3] - Compile: 0.2s
  ✗ Split Payment [iteration_4] - Compile: 0.2s
  ✗ Donation Tracker [iteration_0] - Compile: 0.2s
  ✗ Donation Tracker [iteration_1] - Compile: 0.2s
  ✗ Donation Tracker [iteration_2] - Compile: 0.2s
  ✗ Donation Tracker [iteration_3] - Compile: 0.2s
  ✗ Donation Tracker [iteration_4] - Compile: 0.2s
✓ Completed 25 contracts for granite4:1b Processing Donation Tracker - iteration_4

================================================================================
[MODEL] Processing: llama3.2:1b
================================================================================

  ✗ Simple Lottery [iteration_0] - Compile: 0.2s
  ✗ Simple Lottery [iteration_1] - Compile: 0.2s
  ✗ Simple Lottery [iteration_2] - Compile: 0.2s
  ✗ Simple Lottery [iteration_3] - Compile: 0.2s
  ✗ Simple Lottery [iteration_4] - Compile: 0.2s
  ✗ Whitelist Registry [iteration_0] - Compile: 0.2s
  ✗ Whitelist Registry [iteration_1] - Compile: 0.2s
  ✗ Whitelist Registry [iteration_2] - Compile: 0.2s
  ✗ Whitelist Registry [iteration_3] - Compile: 0.2s
  ✗ Whitelist Registry [iteration_4] - Compile: 0.2s
  ✗ Dead Man Switch [iteration_0] - Compile: 0.2s
  ✗ Dead Man Switch [iteration_1] - Compile: 0.2s
  ✗ Dead Man Switch [iteration_2] - Compile: 0.2s
  ✗ Dead Man Switch [iteration_3] - Compile: 0.2s
  ✗ Dead Man Switch [iteration_4] - Compile: 0.2s
  ✗ Split Payment [iteration_0] - Compile: 0.2s
  ✗ Split Payment [iteration_1] - Compile: 0.2s
  ✗ Split Payment [iteration_2] - Compile: 0.2s
  ✗ Split Payment [iteration_3] - Compile: 0.2s
  ✗ Split Payment [iteration_4] - Compile: 0.2s
  ✗ Donation Tracker [iteration_0] - Compile: 0.2s
  ✗ Donation Tracker [iteration_1] - Compile: 0.2s
  ✓ Donation Tracker [iteration_2] - Compile: 0.2s
  ✗ Donation Tracker [iteration_3] - Compile: 0.2s
  ✗ Donation Tracker [iteration_4] - Compile: 0.2s
✓ Completed 25 contracts for llama3.2:1b Processing Donation Tracker - iteration_4

================================================================================
[MODEL] Processing: qwen2.5-coder:0.5b
================================================================================

  ✗ Simple Lottery [iteration_0] - Compile: 0.2s
  ✗ Simple Lottery [iteration_1] - Compile: 0.2s
  ✗ Simple Lottery [iteration_2] - Compile: 0.2s
  ✗ Simple Lottery [iteration_3] - Compile: 0.2s
  ✗ Simple Lottery [iteration_4] - Compile: 0.2s
  ✗ Whitelist Registry [iteration_0] - Compile: 0.2s
  ✗ Whitelist Registry [iteration_1] - Compile: 0.2s
  ✗ Whitelist Registry [iteration_2] - Compile: 0.2s
  ✗ Whitelist Registry [iteration_3] - Compile: 0.2s
  ✗ Whitelist Registry [iteration_4] - Compile: 0.2s
  ✗ Dead Man Switch [iteration_0] - Compile: 0.2s
  ✗ Dead Man Switch [iteration_1] - Compile: 0.3s
  ✗ Dead Man Switch [iteration_2] - Compile: 0.2s
  ✗ Dead Man Switch [iteration_3] - Compile: 0.2s
  ✗ Dead Man Switch [iteration_4] - Compile: 0.2s
  ✗ Split Payment [iteration_0] - Compile: 0.2s
  ✗ Split Payment [iteration_1] - Compile: 0.2s
  ✗ Split Payment [iteration_2] - Compile: 0.2s
  ✗ Split Payment [iteration_3] - Compile: 0.2s
  ✗ Split Payment [iteration_4] - Compile: 0.2s
  ✗ Donation Tracker [iteration_0] - Compile: 0.2s
  ✗ Donation Tracker [iteration_1] - Compile: 0.2s
  ✗ Donation Tracker [iteration_2] - Compile: 0.2s
  ✗ Donation Tracker [iteration_3] - Compile: 0.2s
  ✗ Donation Tracker [iteration_4] - Compile: 0.2s
✓ Completed 25 contracts for qwen2.5-coder:0.5b Processing Donation Tracker - iteration_4

================================================================================
[MODEL] Processing: FT-Gemma-3-1B:latest
================================================================================

  ✗ Simple Lottery [iteration_0] - Compile: 0.2s
  ✗ Simple Lottery [iteration_1] - Compile: 0.2s
  ✗ Simple Lottery [iteration_2] - Compile: 0.2s
  ✗ Simple Lottery [iteration_3] - Compile: 0.2s
  ✗ Simple Lottery [iteration_4] - Compile: 0.2s
  ✗ Whitelist Registry [iteration_0] - Compile: 0.2s
  ✗ Whitelist Registry [iteration_1] - Compile: 0.2s
  ✗ Whitelist Registry [iteration_2] - Compile: 0.2s
  ✗ Whitelist Registry [iteration_3] - Compile: 0.2s
  ✗ Whitelist Registry [iteration_4] - Compile: 0.2s
  ✗ Dead Man Switch [iteration_0] - Compile: 0.2s
  ✗ Dead Man Switch [iteration_1] - Compile: 0.2s
  ✗ Dead Man Switch [iteration_2] - Compile: 0.2s
  ✗ Dead Man Switch [iteration_3] - Compile: 0.2s
  ✗ Dead Man Switch [iteration_4] - Compile: 0.2s
  ✗ Split Payment [iteration_0] - Compile: 0.2s
  ✗ Split Payment [iteration_1] - Compile: 0.2s
  ✗ Split Payment [iteration_2] - Compile: 0.2s
  ✗ Split Payment [iteration_3] - Compile: 0.2s
  ✗ Split Payment [iteration_4] - Compile: 0.2s
  ✗ Donation Tracker [iteration_0] - Compile: 0.2s
  ✗ Donation Tracker [iteration_1] - Compile: 0.2s
  ✗ Donation Tracker [iteration_2] - Compile: 0.2s
  ✗ Donation Tracker [iteration_3] - Compile: 0.2s
  ✗ Donation Tracker [iteration_4] - Compile: 0.2s
✓ Completed 25 contracts for FT-Gemma-3-1B:latest Processing Donation Tracker - iteration_4

================================================================================
[MODEL] Processing: FT-Granite-4.0-1B:latest
================================================================================

  ✗ Simple Lottery [iteration_0] - Compile: 0.2s
  ✗ Simple Lottery [iteration_1] - Compile: 0.2s
  ✗ Simple Lottery [iteration_2] - Compile: 0.2s
  ✗ Simple Lottery [iteration_3] - Compile: 0.2s
  ✗ Simple Lottery [iteration_4] - Compile: 0.2s
  ✗ Whitelist Registry [iteration_0] - Compile: 0.2s
  ✗ Whitelist Registry [iteration_1] - Compile: 0.2s
  ✗ Whitelist Registry [iteration_2] - Compile: 0.2s
  ✗ Whitelist Registry [iteration_3] - Compile: 0.2s
  ✗ Whitelist Registry [iteration_4] - Compile: 0.2s
  ✗ Dead Man Switch [iteration_0] - Compile: 0.2s
  ✗ Dead Man Switch [iteration_1] - Compile: 0.2s
  ✓ Dead Man Switch [iteration_2] - Compile: 0.2s
  ✗ Dead Man Switch [iteration_3] - Compile: 0.2s
  ✗ Dead Man Switch [iteration_4] - Compile: 0.2s
  ✗ Split Payment [iteration_0] - Compile: 0.2s
  ✗ Split Payment [iteration_1] - Compile: 0.2s
  ✗ Split Payment [iteration_2] - Compile: 0.2s
  ✗ Split Payment [iteration_3] - Compile: 0.2s
  ✗ Split Payment [iteration_4] - Compile: 0.2s
  ✗ Donation Tracker [iteration_0] - Compile: 0.2s
  ✗ Donation Tracker [iteration_1] - Compile: 0.2s
  ✗ Donation Tracker [iteration_2] - Compile: 0.2s
  ✗ Donation Tracker [iteration_3] - Compile: 0.2s
  ✗ Donation Tracker [iteration_4] - Compile: 0.2s
✓ Completed 25 contracts for FT-Granite-4.0-1B:latest Processing Donation Tracker - iteration_4

================================================================================
[MODEL] Processing: FT-Llama-3.2-1B:latest
================================================================================

  ✗ Simple Lottery [iteration_0] - Compile: 0.2s
  ✓ Simple Lottery [iteration_1] - Compile: 0.2s
  ✗ Simple Lottery [iteration_2] - Compile: 0.2s
  ✗ Simple Lottery [iteration_3] - Compile: 0.2s
  ✗ Simple Lottery [iteration_4] - Compile: 0.2s
  ✓ Whitelist Registry [iteration_0] - Compile: 0.2s
  ✓ Whitelist Registry [iteration_1] - Compile: 0.2s
  ✓ Whitelist Registry [iteration_2] - Compile: 0.2s
  ✓ Whitelist Registry [iteration_3] - Compile: 0.2s
  ✓ Whitelist Registry [iteration_4] - Compile: 0.2s
  ✗ Dead Man Switch [iteration_0] - Compile: 0.2s
  ✓ Dead Man Switch [iteration_1] - Compile: 0.2s
  ✓ Dead Man Switch [iteration_2] - Compile: 0.2s
  ✓ Dead Man Switch [iteration_3] - Compile: 0.2s
  ✗ Dead Man Switch [iteration_4] - Compile: 0.2s
  ✗ Split Payment [iteration_0] - Compile: 0.2s
  ✗ Split Payment [iteration_1] - Compile: 0.2s
  ✗ Split Payment [iteration_2] - Compile: 0.2s
  ✗ Split Payment [iteration_3] - Compile: 0.2s
  ✗ Split Payment [iteration_4] - Compile: 0.2s
  ✗ Donation Tracker [iteration_0] - Compile: 0.2s
  ✗ Donation Tracker [iteration_1] - Compile: 0.2s
  ✗ Donation Tracker [iteration_2] - Compile: 0.2s
  ✗ Donation Tracker [iteration_3] - Compile: 0.2s
  ✗ Donation Tracker [iteration_4] - Compile: 0.2s
✓ Completed 25 contracts for FT-Llama-3.2-1B:latest Processing Donation Tracker - iteration_4

================================================================================
[MODEL] Processing: FT-Qwen2.5-Coder-0.5B:latest
================================================================================

  ✗ Simple Lottery [iteration_0] - Compile: 0.2s
  ✗ Simple Lottery [iteration_1] - Compile: 0.2s
  ✗ Simple Lottery [iteration_2] - Compile: 0.2s
  ✗ Simple Lottery [iteration_3] - Compile: 0.2s
  ✗ Simple Lottery [iteration_4] - Compile: 0.2s
  ✓ Whitelist Registry [iteration_0] - Compile: 0.2s
  ✗ Whitelist Registry [iteration_1] - Compile: 0.2s
  ✗ Whitelist Registry [iteration_2] - Compile: 0.2s
  ✗ Whitelist Registry [iteration_3] - Compile: 0.2s
  ✗ Whitelist Registry [iteration_4] - Compile: 0.2s
  ✓ Dead Man Switch [iteration_0] - Compile: 0.2s
  ✗ Dead Man Switch [iteration_1] - Compile: 0.2s
  ✗ Dead Man Switch [iteration_2] - Compile: 0.2s
  ✗ Dead Man Switch [iteration_3] - Compile: 0.2s
  ✗ Dead Man Switch [iteration_4] - Compile: 0.2s
  ✗ Split Payment [iteration_0] - Compile: 0.2s
  ✓ Split Payment [iteration_1] - Compile: 0.2s
  ✗ Split Payment [iteration_2] - Compile: 0.2s
  ✗ Split Payment [iteration_3] - Compile: 0.2s
  ✓ Split Payment [iteration_4] - Compile: 0.2s
  ✗ Donation Tracker [iteration_0] - Compile: 0.2s
  ✗ Donation Tracker [iteration_1] - Compile: 0.2s
  ✓ Donation Tracker [iteration_2] - Compile: 0.2s
  ✓ Donation Tracker [iteration_3] - Compile: 0.2s
  ✓ Donation Tracker [iteration_4] - Compile: 0.2s
✓ Completed 25 contracts for FT-Qwen2.5-Coder-0.5B:latest Processing Donation Tracker - iteration_4

================================================================================
                         ANALYZING RESULTS
================================================================================

[ANALYZING] gemma3:1b...
[ANALYZING] granite4:1b...
[ANALYZING] llama3.2:1b...
[ANALYZING] qwen2.5-coder:0.5b...
[ANALYZING] FT-Gemma-3-1B:latest...
[ANALYZING] FT-Granite-4.0-1B:latest...
[ANALYZING] FT-Llama-3.2-1B:latest...
[ANALYZING] FT-Qwen2.5-Coder-0.5B:latest...

[COMPLETED] Analysis finished

[SAVED] Compilation results: fine-tuning/compare-results\compilation_results.json
[SAVED] Final analysis: fine-tuning/compare-results\cp_analysis.json
[SAVED] Detailed summary: fine-tuning/compare-results\cp_detailed_summary.txt
[SAVED] Quick summary: fine-tuning/compare-results\cp_quick_summary.txt

================================================================================
================================================================================
                          QUICK SUMMARY
================================================================================

[gemma3:1b]
  Avg Generation Time: 4.81s
  Compilation Rate:    0/25 (0.00%)
  Clean Contracts:     0/0
  Vulnerabilities:     0
    High:              0
    Medium:            0
    Low:               0

[granite4:1b]
  Avg Generation Time: 5.92s
  Compilation Rate:    0/25 (0.00%)
  Clean Contracts:     0/0
  Vulnerabilities:     0
    High:              0
    Medium:            0
    Low:               0

[llama3.2:1b]
  Avg Generation Time: 4.42s
  Compilation Rate:    1/25 (4.00%)
  Clean Contracts:     1/1
  Vulnerabilities:     0
    High:              0
    Medium:            0
    Low:               0

[qwen2.5-coder:0.5b]
  Avg Generation Time: 3.53s
  Compilation Rate:    0/25 (0.00%)
  Clean Contracts:     0/0
  Vulnerabilities:     0
    High:              0
    Medium:            0
    Low:               0

[FT-Gemma-3-1B:latest]
  Avg Generation Time: 7.16s
  Compilation Rate:    0/25 (0.00%)
  Clean Contracts:     0/0
  Vulnerabilities:     0
    High:              0
    Medium:            0
    Low:               0

[FT-Granite-4.0-1B:latest]
  Avg Generation Time: 5.03s
  Compilation Rate:    1/25 (4.00%)
  Clean Contracts:     1/1
  Vulnerabilities:     0
    High:              0
    Medium:            0
    Low:               0

[FT-Llama-3.2-1B:latest]
  Avg Generation Time: 32.01s
  Compilation Rate:    9/25 (36.00%)
  Clean Contracts:     9/9
  Vulnerabilities:     0
    High:              0
    Medium:            0
    Low:               0

[FT-Qwen2.5-Coder-0.5B:latest]
  Avg Generation Time: 3.18s
  Compilation Rate:    7/25 (28.00%)
  Clean Contracts:     4/7
  Vulnerabilities:     4
    High:              0
    Medium:            3
    Low:               1

================================================================================

================================================================================
[SUCCESS] Compilation and analysis complete!
================================================================================