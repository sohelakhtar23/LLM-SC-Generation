================================================================================
                         FINAL ANALYSIS SUMMARY
================================================================================

Analysis Date: 2026-06-11 08:58:26
Generation Results: output\generation_results.json


================================================================================
MODEL: deepseek-coder:6.7b
================================================================================

GENERATION STATISTICS:
----------------------------------------
  Total Attempts:        50
  Successful:            50
  Failed:                0
  Success Rate:          100.00%
  Avg Generation Time:   9.24s

COMPILATION STATISTICS:
----------------------------------------
  Total Attempts:        50
  Successful:            25
  Failed:                25
  Success Rate:          50.00%
  Avg Compilation Time:  0.43s

SECURITY ANALYSIS:
----------------------------------------
  Contracts Analyzed:    25
  Clean Contracts:       8
  Clean Rate:            32.00%

MALIGN VULNERABILITY BREAKDOWN:
----------------------------------------
  Total Malign Vulnerabilities: 27

  High                 6 (22.22%)
  Medium               7 (25.93%)
  Low                 14 (51.85%)


TOP 10 MOST COMMON MALIGN VULNERABILITIES:
----------------------------------------
   1. block-timestamp                                    [Low          ] x13
   2. functions-that-send-ether-to-arbitrary-destinations [High         ] x6
   3. contracts-that-lock-ether                          [Medium       ] x5
   4. reentrancy-vulnerabilities-1                       [Medium       ] x1
   5. builtin-symbol-shadowing                           [Low          ] x1
   6. dangerous-strict-equalities                        [Medium       ] x1


PER-PROMPT SUMMARY (MALIGN VULNERABILITIES):
----------------------------------------

  Ownership and Access Control:
    Compilation Success: 0/5 (0.0%)

  Time-Locked Wallet:
    Compilation Success: 5/5 (100.0%)

  Simple Voting System:
    Compilation Success: 3/5 (60.0%)

  ERC20-Like Token:
    Compilation Success: 0/5 (0.0%)

  Escrow Contract:
    Compilation Success: 5/5 (100.0%)

  Multi-Signature Wallet:
    Compilation Success: 1/5 (20.0%)

  Auction Contract:
    Compilation Success: 1/5 (20.0%)

  Subscription Payment System:
    Compilation Success: 5/5 (100.0%)

  Crowdfunding Contract:
    Compilation Success: 5/5 (100.0%)

  Role-Based Access Control:
    Compilation Success: 0/5 (0.0%)

================================================================================
MODEL: granite4.1:8b
================================================================================

GENERATION STATISTICS:
----------------------------------------
  Total Attempts:        50
  Successful:            50
  Failed:                0
  Success Rate:          100.00%
  Avg Generation Time:   10.56s

COMPILATION STATISTICS:
----------------------------------------
  Total Attempts:        50
  Successful:            14
  Failed:                36
  Success Rate:          28.00%
  Avg Compilation Time:  0.74s

SECURITY ANALYSIS:
----------------------------------------
  Contracts Analyzed:    14
  Clean Contracts:       6
  Clean Rate:            42.86%

MALIGN VULNERABILITY BREAKDOWN:
----------------------------------------
  Total Malign Vulnerabilities: 9

  High                 0 ( 0.00%)
  Medium               1 (11.11%)
  Low                  8 (88.89%)


TOP 10 MOST COMMON MALIGN VULNERABILITIES:
----------------------------------------
   1. block-timestamp                                    [Low          ] x8
   2. contracts-that-lock-ether                          [Medium       ] x1


PER-PROMPT SUMMARY (MALIGN VULNERABILITIES):
----------------------------------------

  Ownership and Access Control:
    Compilation Success: 5/5 (100.0%)

  Time-Locked Wallet:
    Compilation Success: 4/5 (80.0%)

  Simple Voting System:
    Compilation Success: 0/5 (0.0%)

  ERC20-Like Token:
    Compilation Success: 0/5 (0.0%)

  Escrow Contract:
    Compilation Success: 0/5 (0.0%)

  Multi-Signature Wallet:
    Compilation Success: 0/5 (0.0%)

  Auction Contract:
    Compilation Success: 4/5 (80.0%)

  Subscription Payment System:
    Compilation Success: 1/5 (20.0%)

  Crowdfunding Contract:
    Compilation Success: 0/5 (0.0%)

  Role-Based Access Control:
    Compilation Success: 0/5 (0.0%)

================================================================================
MODEL: llama3.1:8b
================================================================================

GENERATION STATISTICS:
----------------------------------------
  Total Attempts:        50
  Successful:            50
  Failed:                0
  Success Rate:          100.00%
  Avg Generation Time:   10.58s

COMPILATION STATISTICS:
----------------------------------------
  Total Attempts:        50
  Successful:            18
  Failed:                32
  Success Rate:          36.00%
  Avg Compilation Time:  0.62s

SECURITY ANALYSIS:
----------------------------------------
  Contracts Analyzed:    18
  Clean Contracts:       1
  Clean Rate:            5.56%

MALIGN VULNERABILITY BREAKDOWN:
----------------------------------------
  Total Malign Vulnerabilities: 23

  High                 1 ( 4.35%)
  Medium               7 (30.43%)
  Low                 15 (65.22%)


TOP 10 MOST COMMON MALIGN VULNERABILITIES:
----------------------------------------
   1. block-timestamp                                    [Low          ] x11
   2. contracts-that-lock-ether                          [Medium       ] x6
   3. missing-zero-address-validation                    [Low          ] x4
   4. uninitialized-local-variables                      [Medium       ] x1
   5. state-variable-shadowing                           [High         ] x1


PER-PROMPT SUMMARY (MALIGN VULNERABILITIES):
----------------------------------------

  Ownership and Access Control:
    Compilation Success: 0/5 (0.0%)

  Time-Locked Wallet:
    Compilation Success: 5/5 (100.0%)

  Simple Voting System:
    Compilation Success: 1/5 (20.0%)

  ERC20-Like Token:
    Compilation Success: 0/5 (0.0%)

  Escrow Contract:
    Compilation Success: 3/5 (60.0%)

  Multi-Signature Wallet:
    Compilation Success: 0/5 (0.0%)

  Auction Contract:
    Compilation Success: 0/5 (0.0%)

  Subscription Payment System:
    Compilation Success: 5/5 (100.0%)

  Crowdfunding Contract:
    Compilation Success: 2/5 (40.0%)

  Role-Based Access Control:
    Compilation Success: 2/5 (40.0%)

================================================================================
MODEL: ministral-3:8b
================================================================================

GENERATION STATISTICS:
----------------------------------------
  Total Attempts:        50
  Successful:            50
  Failed:                0
  Success Rate:          100.00%
  Avg Generation Time:   14.87s

COMPILATION STATISTICS:
----------------------------------------
  Total Attempts:        50
  Successful:            23
  Failed:                27
  Success Rate:          46.00%
  Avg Compilation Time:  0.46s

SECURITY ANALYSIS:
----------------------------------------
  Contracts Analyzed:    23
  Clean Contracts:       5
  Clean Rate:            21.74%

MALIGN VULNERABILITY BREAKDOWN:
----------------------------------------
  Total Malign Vulnerabilities: 29

  High                 2 ( 6.90%)
  Medium              10 (34.48%)
  Low                 17 (58.62%)


TOP 10 MOST COMMON MALIGN VULNERABILITIES:
----------------------------------------
   1. block-timestamp                                    [Low          ] x12
   2. contracts-that-lock-ether                          [Medium       ] x6
   3. local-variable-shadowing                           [Low          ] x3
   4. uninitialized-state-variables                      [High         ] x2
   5. missing-events-arithmetic                          [Low          ] x1
   6. dangerous-strict-equalities                        [Medium       ] x1
   7. tautological-compare                               [Medium       ] x1
   8. reentrancy-vulnerabilities-1                       [Medium       ] x1
   9. uninitialized-local-variables                      [Medium       ] x1
  10. missing-zero-address-validation                    [Low          ] x1


PER-PROMPT SUMMARY (MALIGN VULNERABILITIES):
----------------------------------------

  Ownership and Access Control:
    Compilation Success: 3/5 (60.0%)

  Time-Locked Wallet:
    Compilation Success: 4/5 (80.0%)

  Simple Voting System:
    Compilation Success: 3/5 (60.0%)

  ERC20-Like Token:
    Compilation Success: 4/5 (80.0%)

  Escrow Contract:
    Compilation Success: 1/5 (20.0%)

  Multi-Signature Wallet:
    Compilation Success: 1/5 (20.0%)

  Auction Contract:
    Compilation Success: 0/5 (0.0%)

  Subscription Payment System:
    Compilation Success: 4/5 (80.0%)

  Crowdfunding Contract:
    Compilation Success: 2/5 (40.0%)

  Role-Based Access Control:
    Compilation Success: 1/5 (20.0%)

================================================================================
MODEL: qwen2.5-coder:7b
================================================================================

GENERATION STATISTICS:
----------------------------------------
  Total Attempts:        50
  Successful:            50
  Failed:                0
  Success Rate:          100.00%
  Avg Generation Time:   8.95s

COMPILATION STATISTICS:
----------------------------------------
  Total Attempts:        50
  Successful:            36
  Failed:                14
  Success Rate:          72.00%
  Avg Compilation Time:  0.30s

SECURITY ANALYSIS:
----------------------------------------
  Contracts Analyzed:    36
  Clean Contracts:       14
  Clean Rate:            38.89%

MALIGN VULNERABILITY BREAKDOWN:
----------------------------------------
  Total Malign Vulnerabilities: 29

  High                 2 ( 6.90%)
  Medium               7 (24.14%)
  Low                 20 (68.97%)


TOP 10 MOST COMMON MALIGN VULNERABILITIES:
----------------------------------------
   1. block-timestamp                                    [Low          ] x19
   2. contracts-that-lock-ether                          [Medium       ] x5
   3. uninitialized-state-variables                      [High         ] x2
   4. uninitialized-local-variables                      [Medium       ] x1
   5. reentrancy-vulnerabilities-1                       [Medium       ] x1
   6. builtin-symbol-shadowing                           [Low          ] x1


PER-PROMPT SUMMARY (MALIGN VULNERABILITIES):
----------------------------------------

  Ownership and Access Control:
    Compilation Success: 5/5 (100.0%)

  Time-Locked Wallet:
    Compilation Success: 5/5 (100.0%)

  Simple Voting System:
    Compilation Success: 0/5 (0.0%)

  ERC20-Like Token:
    Compilation Success: 5/5 (100.0%)

  Escrow Contract:
    Compilation Success: 5/5 (100.0%)

  Multi-Signature Wallet:
    Compilation Success: 2/5 (40.0%)

  Auction Contract:
    Compilation Success: 5/5 (100.0%)

  Subscription Payment System:
    Compilation Success: 5/5 (100.0%)

  Crowdfunding Contract:
    Compilation Success: 4/5 (80.0%)

  Role-Based Access Control:
    Compilation Success: 0/5 (0.0%)

================================================================================
MODEL: qwen3:8b
================================================================================

GENERATION STATISTICS:
----------------------------------------
  Total Attempts:        50
  Successful:            50
  Failed:                0
  Success Rate:          100.00%
  Avg Generation Time:   104.72s

COMPILATION STATISTICS:
----------------------------------------
  Total Attempts:        50
  Successful:            41
  Failed:                9
  Success Rate:          82.00%
  Avg Compilation Time:  0.26s

SECURITY ANALYSIS:
----------------------------------------
  Contracts Analyzed:    41
  Clean Contracts:       18
  Clean Rate:            43.90%

MALIGN VULNERABILITY BREAKDOWN:
----------------------------------------
  Total Malign Vulnerabilities: 34

  High                 1 ( 2.94%)
  Medium              11 (32.35%)
  Low                 22 (64.71%)


TOP 10 MOST COMMON MALIGN VULNERABILITIES:
----------------------------------------
   1. block-timestamp                                    [Low          ] x19
   2. contracts-that-lock-ether                          [Medium       ] x5
   3. reentrancy-vulnerabilities-1                       [Medium       ] x3
   4. dangerous-strict-equalities                        [Medium       ] x3
   5. builtin-symbol-shadowing                           [Low          ] x2
   6. missing-zero-address-validation                    [Low          ] x1
   7. functions-that-send-ether-to-arbitrary-destinations [High         ] x1


PER-PROMPT SUMMARY (MALIGN VULNERABILITIES):
----------------------------------------

  Ownership and Access Control:
    Compilation Success: 5/5 (100.0%)

  Time-Locked Wallet:
    Compilation Success: 5/5 (100.0%)

  Simple Voting System:
    Compilation Success: 4/5 (80.0%)

  ERC20-Like Token:
    Compilation Success: 4/5 (80.0%)

  Escrow Contract:
    Compilation Success: 3/5 (60.0%)

  Multi-Signature Wallet:
    Compilation Success: 3/5 (60.0%)

  Auction Contract:
    Compilation Success: 4/5 (80.0%)

  Subscription Payment System:
    Compilation Success: 5/5 (100.0%)

  Crowdfunding Contract:
    Compilation Success: 5/5 (100.0%)

  Role-Based Access Control:
    Compilation Success: 3/5 (60.0%)

================================================================================
MODEL: gemma3:27b
================================================================================

GENERATION STATISTICS:
----------------------------------------
  Total Attempts:        50
  Successful:            50
  Failed:                0
  Success Rate:          100.00%
  Avg Generation Time:   33.63s

COMPILATION STATISTICS:
----------------------------------------
  Total Attempts:        50
  Successful:            42
  Failed:                8
  Success Rate:          84.00%
  Avg Compilation Time:  0.25s

SECURITY ANALYSIS:
----------------------------------------
  Contracts Analyzed:    42
  Clean Contracts:       16
  Clean Rate:            38.10%

MALIGN VULNERABILITY BREAKDOWN:
----------------------------------------
  Total Malign Vulnerabilities: 35

  High                 0 ( 0.00%)
  Medium              11 (31.43%)
  Low                 24 (68.57%)


TOP 10 MOST COMMON MALIGN VULNERABILITIES:
----------------------------------------
   1. block-timestamp                                    [Low          ] x19
   2. incorrect-erc20-interface                          [Medium       ] x5
   3. contracts-that-lock-ether                          [Medium       ] x5
   4. local-variable-shadowing                           [Low          ] x3
   5. missing-zero-address-validation                    [Low          ] x2
   6. reentrancy-vulnerabilities-1                       [Medium       ] x1


PER-PROMPT SUMMARY (MALIGN VULNERABILITIES):
----------------------------------------

  Ownership and Access Control:
    Compilation Success: 5/5 (100.0%)

  Time-Locked Wallet:
    Compilation Success: 5/5 (100.0%)

  Simple Voting System:
    Compilation Success: 5/5 (100.0%)

  ERC20-Like Token:
    Compilation Success: 5/5 (100.0%)

  Escrow Contract:
    Compilation Success: 3/5 (60.0%)

  Multi-Signature Wallet:
    Compilation Success: 0/5 (0.0%)

  Auction Contract:
    Compilation Success: 5/5 (100.0%)

  Subscription Payment System:
    Compilation Success: 5/5 (100.0%)

  Crowdfunding Contract:
    Compilation Success: 4/5 (80.0%)

  Role-Based Access Control:
    Compilation Success: 5/5 (100.0%)

================================================================================
MODEL: gpt-oss:20b
================================================================================

GENERATION STATISTICS:
----------------------------------------
  Total Attempts:        50
  Successful:            50
  Failed:                0
  Success Rate:          100.00%
  Avg Generation Time:   27.82s

COMPILATION STATISTICS:
----------------------------------------
  Total Attempts:        50
  Successful:            45
  Failed:                5
  Success Rate:          90.00%
  Avg Compilation Time:  0.24s

SECURITY ANALYSIS:
----------------------------------------
  Contracts Analyzed:    45
  Clean Contracts:       27
  Clean Rate:            60.00%

MALIGN VULNERABILITY BREAKDOWN:
----------------------------------------
  Total Malign Vulnerabilities: 24

  High                 0 ( 0.00%)
  Medium               8 (33.33%)
  Low                 16 (66.67%)


TOP 10 MOST COMMON MALIGN VULNERABILITIES:
----------------------------------------
   1. block-timestamp                                    [Low          ] x16
   2. reentrancy-vulnerabilities-1                       [Medium       ] x3
   3. dangerous-strict-equalities                        [Medium       ] x3
   4. contracts-that-lock-ether                          [Medium       ] x2


PER-PROMPT SUMMARY (MALIGN VULNERABILITIES):
----------------------------------------

  Ownership and Access Control:
    Compilation Success: 5/5 (100.0%)

  Time-Locked Wallet:
    Compilation Success: 5/5 (100.0%)

  Simple Voting System:
    Compilation Success: 5/5 (100.0%)

  ERC20-Like Token:
    Compilation Success: 5/5 (100.0%)

  Escrow Contract:
    Compilation Success: 5/5 (100.0%)

  Multi-Signature Wallet:
    Compilation Success: 5/5 (100.0%)

  Auction Contract:
    Compilation Success: 3/5 (60.0%)

  Subscription Payment System:
    Compilation Success: 5/5 (100.0%)

  Crowdfunding Contract:
    Compilation Success: 3/5 (60.0%)

  Role-Based Access Control:
    Compilation Success: 4/5 (80.0%)

================================================================================
MODEL: mistral-small:24b
================================================================================

GENERATION STATISTICS:
----------------------------------------
  Total Attempts:        50
  Successful:            50
  Failed:                0
  Success Rate:          100.00%
  Avg Generation Time:   24.38s

COMPILATION STATISTICS:
----------------------------------------
  Total Attempts:        50
  Successful:            28
  Failed:                22
  Success Rate:          56.00%
  Avg Compilation Time:  0.40s

SECURITY ANALYSIS:
----------------------------------------
  Contracts Analyzed:    28
  Clean Contracts:       11
  Clean Rate:            39.29%

MALIGN VULNERABILITY BREAKDOWN:
----------------------------------------
  Total Malign Vulnerabilities: 24

  High                 2 ( 8.33%)
  Medium               6 (25.00%)
  Low                 16 (66.67%)


TOP 10 MOST COMMON MALIGN VULNERABILITIES:
----------------------------------------
   1. block-timestamp                                    [Low          ] x16
   2. contracts-that-lock-ether                          [Medium       ] x5
   3. functions-that-send-ether-to-arbitrary-destinations [High         ] x2
   4. reentrancy-vulnerabilities-1                       [Medium       ] x1


PER-PROMPT SUMMARY (MALIGN VULNERABILITIES):
----------------------------------------

  Ownership and Access Control:
    Compilation Success: 2/5 (40.0%)

  Time-Locked Wallet:
    Compilation Success: 5/5 (100.0%)

  Simple Voting System:
    Compilation Success: 0/5 (0.0%)

  ERC20-Like Token:
    Compilation Success: 5/5 (100.0%)

  Escrow Contract:
    Compilation Success: 5/5 (100.0%)

  Multi-Signature Wallet:
    Compilation Success: 0/5 (0.0%)

  Auction Contract:
    Compilation Success: 2/5 (40.0%)

  Subscription Payment System:
    Compilation Success: 5/5 (100.0%)

  Crowdfunding Contract:
    Compilation Success: 4/5 (80.0%)

  Role-Based Access Control:
    Compilation Success: 0/5 (0.0%)


