>> python repair_compilation.py
================================================================================
                  SMART CONTRACT COMPILATION REPAIR PIPELINE
================================================================================

[LOAD] Reading compilation_results.json ...
[LOAD] Reading generation_summary.json ...
[LOAD] Reading prompts CSV ...
[LOAD] 10 specifications loaded from CSV
[LOAD] 9 model(s) found in compilation results

[IDENTIFY] 178 failed contract(s) found that need repair

  deepseek-coder:6.7b: 25 failed contract(s)
  granite4.1:8b: 36 failed contract(s)
  llama3.1:8b: 32 failed contract(s)
  ministral-3:8b: 27 failed contract(s)
  qwen2.5-coder:7b: 14 failed contract(s)
  qwen3:8b: 9 failed contract(s)
  gemma3:27b: 8 failed contract(s)
  gpt-oss:20b: 5 failed contract(s)
  mistral-small:24b: 22 failed contract(s)

[INFO] Pipeline started at: 2026-06-11T09:09:50.291041

================================================================================
                      COMPILATION REPAIR MECHANISM
================================================================================
[CONFIG] Strategies : ['direct_fix', 'chain_of_thought', 'role_based']
[CONFIG] Contracts  : 178
[CONFIG] LLM calls  : 534
================================================================================


================================================================================
[MODEL] deepseek-coder:6.7b  (25 contract(s) to repair)
================================================================================

  ✓ [1/25] Ownership and Access Control | iteration_0 | direct_fix       | compiled=YES | 13.5s
  ✓ [1/25] Ownership and Access Control | iteration_0 | chain_of_thought | compiled=YES | 32.3s +2 retries
  ✓ [1/25] Ownership and Access Control | iteration_0 | role_based       | compiled=YES | 10.5s
  ✓ [2/25] Ownership and Access Control | iteration_1 | direct_fix       | compiled=YES | 26.1s +2 retries
  ✗ [2/25] Ownership and Access Control | iteration_1 | chain_of_thought | compiled=NO  | 30.1s +2 retries
  ✓ [2/25] Ownership and Access Control | iteration_1 | role_based       | compiled=YES | 17.1s +1 retry
  ✓ [3/25] Ownership and Access Control | iteration_2 | direct_fix       | compiled=YES | 10.2s
  ✓ [3/25] Ownership and Access Control | iteration_2 | chain_of_thought | compiled=YES | 12.3s
  ✓ [3/25] Ownership and Access Control | iteration_2 | role_based       | compiled=YES | 10.5s
  ✓ [4/25] Ownership and Access Control | iteration_3 | direct_fix       | compiled=YES | 17.4s +1 retry
  ✓ [4/25] Ownership and Access Control | iteration_3 | chain_of_thought | compiled=YES | 12.4s
  ✓ [4/25] Ownership and Access Control | iteration_3 | role_based       | compiled=YES | 25.9s +2 retries
  ✗ [5/25] Ownership and Access Control | iteration_4 | direct_fix       | compiled=NO  | 26.1s +2 retries
  ✓ [5/25] Ownership and Access Control | iteration_4 | chain_of_thought | compiled=YES | 10.7s
  ✗ [5/25] Ownership and Access Control | iteration_4 | role_based       | compiled=NO  | 25.6s +2 retries
  ✗ [6/25] Simple Voting System | iteration_2 | direct_fix       | compiled=NO  | 49.8s +2 retries
  ✗ [6/25] Simple Voting System | iteration_2 | chain_of_thought | compiled=NO  | 47.6s +2 retries
  ✓ [6/25] Simple Voting System | iteration_2 | role_based       | compiled=YES | 20.2s
  ✓ [7/25] Simple Voting System | iteration_3 | direct_fix       | compiled=YES | 13.7s
  ✓ [7/25] Simple Voting System | iteration_3 | chain_of_thought | compiled=YES | 14.3s
  ✓ [7/25] Simple Voting System | iteration_3 | role_based       | compiled=YES | 15.9s
  ✗ [8/25] ERC20-Like Token | iteration_0 | direct_fix       | compiled=NO  | 30.2s +2 retries
  ✗ [8/25] ERC20-Like Token | iteration_0 | chain_of_thought | compiled=NO  | 39.7s +2 retries
  ✗ [8/25] ERC20-Like Token | iteration_0 | role_based       | compiled=NO  | 24.5s +2 retries
  ✗ [9/25] ERC20-Like Token | iteration_1 | direct_fix       | compiled=NO  | 34.6s +2 retries
  ✗ [9/25] ERC20-Like Token | iteration_1 | chain_of_thought | compiled=NO  | 37.7s +2 retries
  ✗ [9/25] ERC20-Like Token | iteration_1 | role_based       | compiled=NO  | 27.4s +2 retries
  ✗ [10/25] ERC20-Like Token | iteration_2 | direct_fix       | compiled=NO  | 56.9s +2 retries
  ✗ [10/25] ERC20-Like Token | iteration_2 | chain_of_thought | compiled=NO  | 62.3s +2 retries
  ✗ [10/25] ERC20-Like Token | iteration_2 | role_based       | compiled=NO  | 52.9s +2 retries
  ✗ [11/25] ERC20-Like Token | iteration_3 | direct_fix       | compiled=NO  | 32.8s +2 retries
  ✗ [11/25] ERC20-Like Token | iteration_3 | chain_of_thought | compiled=NO  | 42.8s +2 retries
  ✗ [11/25] ERC20-Like Token | iteration_3 | role_based       | compiled=NO  | 28.4s +2 retries
  ✗ [12/25] ERC20-Like Token | iteration_4 | direct_fix       | compiled=NO  | 31.7s +2 retries
  ✗ [12/25] ERC20-Like Token | iteration_4 | chain_of_thought | compiled=NO  | 38.0s +2 retries
  ✗ [12/25] ERC20-Like Token | iteration_4 | role_based       | compiled=NO  | 25.8s +2 retries
  ✗ [13/25] Multi-Signature Wallet | iteration_0 | direct_fix       | compiled=NO  | 83.9s +2 retries
  ✗ [13/25] Multi-Signature Wallet | iteration_0 | chain_of_thought | compiled=NO  | 88.2s +2 retries
  ✗ [13/25] Multi-Signature Wallet | iteration_0 | role_based       | compiled=NO  | 78.2s +2 retries
  ✗ [14/25] Multi-Signature Wallet | iteration_1 | direct_fix       | compiled=NO  | 45.3s +2 retries
  ✗ [14/25] Multi-Signature Wallet | iteration_1 | chain_of_thought | compiled=NO  | 51.3s +2 retries
  ✗ [14/25] Multi-Signature Wallet | iteration_1 | role_based       | compiled=NO  | 44.9s +2 retries
  ✗ [15/25] Multi-Signature Wallet | iteration_2 | direct_fix       | compiled=NO  | 48.2s +2 retries
  ✗ [15/25] Multi-Signature Wallet | iteration_2 | chain_of_thought | compiled=NO  | 48.8s +2 retries
  ✓ [15/25] Multi-Signature Wallet | iteration_2 | role_based       | compiled=YES | 18.2s
  ✗ [16/25] Multi-Signature Wallet | iteration_3 | direct_fix       | compiled=NO  | 51.9s +2 retries
  ✗ [16/25] Multi-Signature Wallet | iteration_3 | chain_of_thought | compiled=NO  | 59.9s +2 retries
  ✗ [16/25] Multi-Signature Wallet | iteration_3 | role_based       | compiled=NO  | 52.0s +2 retries
  ✗ [17/25] Auction Contract | iteration_0 | direct_fix       | compiled=NO  | 42.1s +2 retries
  ✓ [17/25] Auction Contract | iteration_0 | chain_of_thought | compiled=YES | 16.3s
  ✗ [17/25] Auction Contract | iteration_0 | role_based       | compiled=NO  | 43.6s +2 retries
  ✓ [18/25] Auction Contract | iteration_2 | direct_fix       | compiled=YES | 15.0s
  ✓ [18/25] Auction Contract | iteration_2 | chain_of_thought | compiled=YES | 8.8s
  ✓ [18/25] Auction Contract | iteration_2 | role_based       | compiled=YES | 15.6s
  ✓ [19/25] Auction Contract | iteration_3 | direct_fix       | compiled=YES | 14.6s
  ✓ [19/25] Auction Contract | iteration_3 | chain_of_thought | compiled=YES | 22.9s +1 retry
  ✓ [19/25] Auction Contract | iteration_3 | role_based       | compiled=YES | 13.0s
  ✓ [20/25] Auction Contract | iteration_4 | direct_fix       | compiled=YES | 43.8s +2 retries
  ✓ [20/25] Auction Contract | iteration_4 | chain_of_thought | compiled=YES | 15.5s
  ✓ [20/25] Auction Contract | iteration_4 | role_based       | compiled=YES | 13.2s
  ✗ [21/25] Role-Based Access Control | iteration_0 | direct_fix       | compiled=NO  | 39.4s +2 retries
  ✗ [21/25] Role-Based Access Control | iteration_0 | chain_of_thought | compiled=NO  | 50.3s +2 retries
  ✗ [21/25] Role-Based Access Control | iteration_0 | role_based       | compiled=NO  | 35.9s +2 retries
  ✗ [22/25] Role-Based Access Control | iteration_1 | direct_fix       | compiled=NO  | 35.0s +2 retries
  ✗ [22/25] Role-Based Access Control | iteration_1 | chain_of_thought | compiled=NO  | 35.8s +2 retries
  ✗ [22/25] Role-Based Access Control | iteration_1 | role_based       | compiled=NO  | 34.1s +2 retries
  ✗ [23/25] Role-Based Access Control | iteration_2 | direct_fix       | compiled=NO  | 45.6s +2 retries
  ✗ [23/25] Role-Based Access Control | iteration_2 | chain_of_thought | compiled=NO  | 71.4s +2 retries
  ✗ [23/25] Role-Based Access Control | iteration_2 | role_based       | compiled=NO  | 42.8s +2 retries
  ✗ [24/25] Role-Based Access Control | iteration_3 | direct_fix       | compiled=NO  | 26.5s +2 retries
  ✗ [24/25] Role-Based Access Control | iteration_3 | chain_of_thought | compiled=NO  | 32.5s +2 retries
  ✗ [24/25] Role-Based Access Control | iteration_3 | role_based       | compiled=NO  | 29.6s +2 retries
  ✗ [25/25] Role-Based Access Control | iteration_4 | direct_fix       | compiled=NO  | 35.7s +2 retries
  ✗ [25/25] Role-Based Access Control | iteration_4 | chain_of_thought | compiled=NO  | 40.5s +2 retries
  ✗ [25/25] Role-Based Access Control | iteration_4 | role_based       | compiled=NO  | 33.4s +2 retries
✓ Finished repairs for deepseek-coder:6.7b [25/25] Role-Based Access Control | iteration_4 | role_based retry 2/2

================================================================================
[MODEL] granite4.1:8b  (36 contract(s) to repair)
================================================================================

  ✗ [1/36] Time-Locked Wallet | iteration_4 | direct_fix       | compiled=NO  | 27.0s +2 retries
⠴ [1/36] Time-Locked Wallet | iteration_4 | chain_of_thought
[WARN] Timeout – retrying (1/2)...
  ✗ [1/36] Time-Locked Wallet | iteration_4 | chain_of_thought | compiled=NO  | 229.3s +2 retries
  ✗ [1/36] Time-Locked Wallet | iteration_4 | role_based       | compiled=NO  | 22.8s +2 retries
  ✗ [2/36] Simple Voting System | iteration_0 | direct_fix       | compiled=NO  | 45.3s +2 retries
  ✓ [2/36] Simple Voting System | iteration_0 | chain_of_thought | compiled=YES | 39.8s +1 retry
  ✗ [2/36] Simple Voting System | iteration_0 | role_based       | compiled=NO  | 45.1s +2 retries
  ✗ [3/36] Simple Voting System | iteration_1 | direct_fix       | compiled=NO  | 38.6s +2 retries
  ✗ [3/36] Simple Voting System | iteration_1 | chain_of_thought | compiled=NO  | 91.3s +2 retries
  ✗ [3/36] Simple Voting System | iteration_1 | role_based       | compiled=NO  | 39.0s +2 retries
  ✓ [4/36] Simple Voting System | iteration_2 | direct_fix       | compiled=YES | 25.8s +1 retry
  ✓ [4/36] Simple Voting System | iteration_2 | chain_of_thought | compiled=YES | 19.8s
  ✗ [4/36] Simple Voting System | iteration_2 | role_based       | compiled=NO  | 41.9s +2 retries
  ✗ [5/36] Simple Voting System | iteration_3 | direct_fix       | compiled=NO  | 46.2s +2 retries
  ✗ [5/36] Simple Voting System | iteration_3 | chain_of_thought | compiled=NO  | 64.8s +2 retries
  ✗ [5/36] Simple Voting System | iteration_3 | role_based       | compiled=NO  | 47.0s +2 retries
  ✗ [6/36] Simple Voting System | iteration_4 | direct_fix       | compiled=NO  | 31.5s +2 retries
  ✓ [6/36] Simple Voting System | iteration_4 | chain_of_thought | compiled=YES | 34.7s +1 retry
  ✗ [6/36] Simple Voting System | iteration_4 | role_based       | compiled=NO  | 34.0s +2 retries
  ✓ [7/36] ERC20-Like Token | iteration_0 | direct_fix       | compiled=YES | 13.2s
  ✓ [7/36] ERC20-Like Token | iteration_0 | chain_of_thought | compiled=YES | 32.8s +1 retry
  ✓ [7/36] ERC20-Like Token | iteration_0 | role_based       | compiled=YES | 13.5s
  ✓ [8/36] ERC20-Like Token | iteration_1 | direct_fix       | compiled=YES | 13.5s
  ✓ [8/36] ERC20-Like Token | iteration_1 | chain_of_thought | compiled=YES | 34.3s +1 retry
  ✓ [8/36] ERC20-Like Token | iteration_1 | role_based       | compiled=YES | 13.9s
  ✓ [9/36] ERC20-Like Token | iteration_2 | direct_fix       | compiled=YES | 12.9s
  ✓ [9/36] ERC20-Like Token | iteration_2 | chain_of_thought | compiled=YES | 46.8s +2 retries
  ✓ [9/36] ERC20-Like Token | iteration_2 | role_based       | compiled=YES | 13.1s
  ✓ [10/36] ERC20-Like Token | iteration_3 | direct_fix       | compiled=YES | 12.2s
  ✓ [10/36] ERC20-Like Token | iteration_3 | chain_of_thought | compiled=YES | 46.1s +2 retries
  ✓ [10/36] ERC20-Like Token | iteration_3 | role_based       | compiled=YES | 12.8s
  ✓ [11/36] ERC20-Like Token | iteration_4 | direct_fix       | compiled=YES | 13.3s
  ✓ [11/36] ERC20-Like Token | iteration_4 | chain_of_thought | compiled=YES | 34.8s +1 retry
  ✓ [11/36] ERC20-Like Token | iteration_4 | role_based       | compiled=YES | 13.6s
  ✓ [12/36] Escrow Contract | iteration_0 | direct_fix       | compiled=YES | 39.6s +1 retry
  ✗ [12/36] Escrow Contract | iteration_0 | chain_of_thought | compiled=NO  | 93.4s +2 retries
  ✓ [12/36] Escrow Contract | iteration_0 | role_based       | compiled=YES | 39.7s +1 retry
  ✗ [13/36] Escrow Contract | iteration_1 | direct_fix       | compiled=NO  | 57.0s +2 retries
  ✗ [13/36] Escrow Contract | iteration_1 | chain_of_thought | compiled=NO  | 79.0s +2 retries
  ✓ [13/36] Escrow Contract | iteration_1 | role_based       | compiled=YES | 36.6s +1 retry
  ✓ [14/36] Escrow Contract | iteration_2 | direct_fix       | compiled=YES | 15.0s
  ✓ [14/36] Escrow Contract | iteration_2 | chain_of_thought | compiled=YES | 26.2s
  ✓ [14/36] Escrow Contract | iteration_2 | role_based       | compiled=YES | 16.0s
  ✓ [15/36] Escrow Contract | iteration_3 | direct_fix       | compiled=YES | 58.4s +2 retries
  ✓ [15/36] Escrow Contract | iteration_3 | chain_of_thought | compiled=YES | 32.2s
  ✓ [15/36] Escrow Contract | iteration_3 | role_based       | compiled=YES | 42.1s +1 retry
  ✓ [16/36] Escrow Contract | iteration_4 | direct_fix       | compiled=YES | 24.2s
  ✓ [16/36] Escrow Contract | iteration_4 | chain_of_thought | compiled=YES | 81.8s +2 retries
  ✓ [16/36] Escrow Contract | iteration_4 | role_based       | compiled=YES | 24.1s
  ✗ [17/36] Multi-Signature Wallet | iteration_0 | direct_fix       | compiled=NO  | 44.8s +2 retries
  ✗ [17/36] Multi-Signature Wallet | iteration_0 | chain_of_thought | compiled=NO  | 63.5s +2 retries
  ✗ [17/36] Multi-Signature Wallet | iteration_0 | role_based       | compiled=NO  | 46.5s +2 retries
  ✓ [18/36] Multi-Signature Wallet | iteration_1 | direct_fix       | compiled=YES | 43.7s +2 retries
  ✗ [18/36] Multi-Signature Wallet | iteration_1 | chain_of_thought | compiled=NO  | 54.1s +2 retries
  ✗ [18/36] Multi-Signature Wallet | iteration_1 | role_based       | compiled=NO  | 46.1s +2 retries
  ✗ [19/36] Multi-Signature Wallet | iteration_2 | direct_fix       | compiled=NO  | 44.0s +2 retries
  ✗ [19/36] Multi-Signature Wallet | iteration_2 | chain_of_thought | compiled=NO  | 62.1s +2 retries
  ✗ [19/36] Multi-Signature Wallet | iteration_2 | role_based       | compiled=NO  | 44.0s +2 retries
  ✗ [20/36] Multi-Signature Wallet | iteration_3 | direct_fix       | compiled=NO  | 47.4s +2 retries
  ✗ [20/36] Multi-Signature Wallet | iteration_3 | chain_of_thought | compiled=NO  | 76.0s +2 retries
  ✗ [20/36] Multi-Signature Wallet | iteration_3 | role_based       | compiled=NO  | 47.5s +2 retries
  ✗ [21/36] Multi-Signature Wallet | iteration_4 | direct_fix       | compiled=NO  | 46.8s +2 retries
  ✗ [21/36] Multi-Signature Wallet | iteration_4 | chain_of_thought | compiled=NO  | 53.2s +2 retries
  ✗ [21/36] Multi-Signature Wallet | iteration_4 | role_based       | compiled=NO  | 42.1s +2 retries
  ✗ [22/36] Auction Contract | iteration_2 | direct_fix       | compiled=NO  | 41.7s +2 retries
  ✗ [22/36] Auction Contract | iteration_2 | chain_of_thought | compiled=NO  | 65.0s +2 retries
  ✗ [22/36] Auction Contract | iteration_2 | role_based       | compiled=NO  | 44.9s +2 retries
  ✓ [23/36] Subscription Payment System | iteration_0 | direct_fix       | compiled=YES | 8.8s
  ✓ [23/36] Subscription Payment System | iteration_0 | chain_of_thought | compiled=YES | 11.7s
  ✓ [23/36] Subscription Payment System | iteration_0 | role_based       | compiled=YES | 9.1s
  ✗ [24/36] Subscription Payment System | iteration_1 | direct_fix       | compiled=NO  | 32.3s +2 retries
  ✗ [24/36] Subscription Payment System | iteration_1 | chain_of_thought | compiled=NO  | 41.2s +2 retries
  ✗ [24/36] Subscription Payment System | iteration_1 | role_based       | compiled=NO  | 32.7s +2 retries
  ✓ [25/36] Subscription Payment System | iteration_3 | direct_fix       | compiled=YES | 17.0s +1 retry
  ✓ [25/36] Subscription Payment System | iteration_3 | chain_of_thought | compiled=YES | 23.3s +1 retry
  ✓ [25/36] Subscription Payment System | iteration_3 | role_based       | compiled=YES | 10.0s
  ✗ [26/36] Subscription Payment System | iteration_4 | direct_fix       | compiled=NO  | 28.8s +2 retries
  ✗ [26/36] Subscription Payment System | iteration_4 | chain_of_thought | compiled=NO  | 40.8s +2 retries
  ✗ [26/36] Subscription Payment System | iteration_4 | role_based       | compiled=NO  | 30.5s +2 retries
  ✗ [27/36] Crowdfunding Contract | iteration_0 | direct_fix       | compiled=NO  | 36.0s +2 retries
  ✗ [27/36] Crowdfunding Contract | iteration_0 | chain_of_thought | compiled=NO  | 55.5s +2 retries
  ✗ [27/36] Crowdfunding Contract | iteration_0 | role_based       | compiled=NO  | 38.3s +2 retries
  ✗ [28/36] Crowdfunding Contract | iteration_1 | direct_fix       | compiled=NO  | 32.9s +2 retries
  ✗ [28/36] Crowdfunding Contract | iteration_1 | chain_of_thought | compiled=NO  | 50.6s +2 retries
  ✗ [28/36] Crowdfunding Contract | iteration_1 | role_based       | compiled=NO  | 34.0s +2 retries
  ✗ [29/36] Crowdfunding Contract | iteration_2 | direct_fix       | compiled=NO  | 32.3s +2 retries
  ✗ [29/36] Crowdfunding Contract | iteration_2 | chain_of_thought | compiled=NO  | 60.4s +2 retries
  ✓ [29/36] Crowdfunding Contract | iteration_2 | role_based       | compiled=YES | 11.5s
  ✗ [30/36] Crowdfunding Contract | iteration_3 | direct_fix       | compiled=NO  | 33.3s +2 retries
  ✓ [30/36] Crowdfunding Contract | iteration_3 | chain_of_thought | compiled=YES | 43.2s +1 retry
  ✗ [30/36] Crowdfunding Contract | iteration_3 | role_based       | compiled=NO  | 33.4s +2 retries
  ✗ [31/36] Crowdfunding Contract | iteration_4 | direct_fix       | compiled=NO  | 38.6s +2 retries
  ✓ [31/36] Crowdfunding Contract | iteration_4 | chain_of_thought | compiled=YES | 22.4s
  ✗ [31/36] Crowdfunding Contract | iteration_4 | role_based       | compiled=NO  | 39.0s +2 retries
  ✗ [32/36] Role-Based Access Control | iteration_0 | direct_fix       | compiled=NO  | 33.9s +2 retries
  ✗ [32/36] Role-Based Access Control | iteration_0 | chain_of_thought | compiled=NO  | 43.6s +2 retries
  ✗ [32/36] Role-Based Access Control | iteration_0 | role_based       | compiled=NO  | 36.5s +2 retries
  ✗ [33/36] Role-Based Access Control | iteration_1 | direct_fix       | compiled=NO  | 30.4s +2 retries
  ✗ [33/36] Role-Based Access Control | iteration_1 | chain_of_thought | compiled=NO  | 40.2s +2 retries
  ✗ [33/36] Role-Based Access Control | iteration_1 | role_based       | compiled=NO  | 30.4s +2 retries
  ✗ [34/36] Role-Based Access Control | iteration_2 | direct_fix       | compiled=NO  | 29.5s +2 retries
  ✗ [34/36] Role-Based Access Control | iteration_2 | chain_of_thought | compiled=NO  | 42.5s +2 retries
  ✗ [34/36] Role-Based Access Control | iteration_2 | role_based       | compiled=NO  | 29.8s +2 retries
  ✗ [35/36] Role-Based Access Control | iteration_3 | direct_fix       | compiled=NO  | 28.3s +2 retries
  ✗ [35/36] Role-Based Access Control | iteration_3 | chain_of_thought | compiled=NO  | 42.6s +2 retries
  ✗ [35/36] Role-Based Access Control | iteration_3 | role_based       | compiled=NO  | 29.1s +2 retries
  ✗ [36/36] Role-Based Access Control | iteration_4 | direct_fix       | compiled=NO  | 34.7s +2 retries
  ✗ [36/36] Role-Based Access Control | iteration_4 | chain_of_thought | compiled=NO  | 50.6s +2 retries
  ✗ [36/36] Role-Based Access Control | iteration_4 | role_based       | compiled=NO  | 34.8s +2 retries
✓ Finished repairs for granite4.1:8b [36/36] Role-Based Access Control | iteration_4 | role_based retry 2/2

================================================================================
[MODEL] llama3.1:8b  (32 contract(s) to repair)
================================================================================

  ✗ [1/32] Ownership and Access Control | iteration_0 | direct_fix       | compiled=NO  | 17.8s +2 retries
  ✗ [1/32] Ownership and Access Control | iteration_0 | chain_of_thought | compiled=NO  | 32.8s +2 retries
  ✗ [1/32] Ownership and Access Control | iteration_0 | role_based       | compiled=NO  | 28.6s +2 retries
  ✗ [2/32] Ownership and Access Control | iteration_1 | direct_fix       | compiled=NO  | 16.3s +2 retries
  ✓ [2/32] Ownership and Access Control | iteration_1 | chain_of_thought | compiled=YES | 10.5s
  ✗ [2/32] Ownership and Access Control | iteration_1 | role_based       | compiled=NO  | 25.6s +2 retries
  ✗ [3/32] Ownership and Access Control | iteration_2 | direct_fix       | compiled=NO  | 18.3s +2 retries
  ✓ [3/32] Ownership and Access Control | iteration_2 | chain_of_thought | compiled=YES | 10.2s
  ✗ [3/32] Ownership and Access Control | iteration_2 | role_based       | compiled=NO  | 22.7s +2 retries
  ✗ [4/32] Ownership and Access Control | iteration_3 | direct_fix       | compiled=NO  | 16.7s +2 retries
  ✓ [4/32] Ownership and Access Control | iteration_3 | chain_of_thought | compiled=YES | 9.9s
  ✗ [4/32] Ownership and Access Control | iteration_3 | role_based       | compiled=NO  | 25.5s +2 retries
  ✗ [5/32] Ownership and Access Control | iteration_4 | direct_fix       | compiled=NO  | 15.2s +2 retries
  ✓ [5/32] Ownership and Access Control | iteration_4 | chain_of_thought | compiled=YES | 20.8s +1 retry
  ✗ [5/32] Ownership and Access Control | iteration_4 | role_based       | compiled=NO  | 21.2s +2 retries
  ✗ [6/32] Simple Voting System | iteration_0 | direct_fix       | compiled=NO  | 41.4s +2 retries
  ✓ [6/32] Simple Voting System | iteration_0 | chain_of_thought | compiled=YES | 49.4s +2 retries
  ✗ [6/32] Simple Voting System | iteration_0 | role_based       | compiled=NO  | 51.8s +2 retries
  ✗ [7/32] Simple Voting System | iteration_1 | direct_fix       | compiled=NO  | 43.6s +2 retries
  ✓ [7/32] Simple Voting System | iteration_1 | chain_of_thought | compiled=YES | 32.0s +1 retry
  ✗ [7/32] Simple Voting System | iteration_1 | role_based       | compiled=NO  | 50.4s +2 retries
⠸ [8/32] Simple Voting System | iteration_2 | direct_fix retry 2/2
[WARN] Timeout – retrying (1/2)...
  ✗ [8/32] Simple Voting System | iteration_2 | direct_fix       | compiled=NO  | 239.8s +2 retries
  ✓ [8/32] Simple Voting System | iteration_2 | chain_of_thought | compiled=YES | 29.1s +1 retry
  ✗ [8/32] Simple Voting System | iteration_2 | role_based       | compiled=NO  | 44.4s +2 retries
  ✓ [9/32] Simple Voting System | iteration_4 | direct_fix       | compiled=YES | 32.5s +1 retry
  ✗ [9/32] Simple Voting System | iteration_4 | chain_of_thought | compiled=NO  | 48.8s +2 retries
  ✓ [9/32] Simple Voting System | iteration_4 | role_based       | compiled=YES | 33.3s +1 retry
  ✗ [10/32] ERC20-Like Token | iteration_0 | direct_fix       | compiled=NO  | 26.6s +2 retries
  ✗ [10/32] ERC20-Like Token | iteration_0 | chain_of_thought | compiled=NO  | 32.1s +2 retries
  ✗ [10/32] ERC20-Like Token | iteration_0 | role_based       | compiled=NO  | 40.9s +2 retries
  ✗ [11/32] ERC20-Like Token | iteration_1 | direct_fix       | compiled=NO  | 31.1s +2 retries
  ✓ [11/32] ERC20-Like Token | iteration_1 | chain_of_thought | compiled=YES | 13.4s
  ✓ [11/32] ERC20-Like Token | iteration_1 | role_based       | compiled=YES | 25.3s +1 retry
  ✗ [12/32] ERC20-Like Token | iteration_2 | direct_fix       | compiled=NO  | 37.8s +2 retries
  ✗ [12/32] ERC20-Like Token | iteration_2 | chain_of_thought | compiled=NO  | 46.8s +2 retries
  ✗ [12/32] ERC20-Like Token | iteration_2 | role_based       | compiled=NO  | 35.8s +2 retries
  ✗ [13/32] ERC20-Like Token | iteration_3 | direct_fix       | compiled=NO  | 25.9s +2 retries
  ✗ [13/32] ERC20-Like Token | iteration_3 | chain_of_thought | compiled=NO  | 36.6s +2 retries
  ✓ [13/32] ERC20-Like Token | iteration_3 | role_based       | compiled=YES | 26.3s +1 retry
  ✗ [14/32] ERC20-Like Token | iteration_4 | direct_fix       | compiled=NO  | 31.4s +2 retries
  ✗ [14/32] ERC20-Like Token | iteration_4 | chain_of_thought | compiled=NO  | 35.9s +2 retries
  ✗ [14/32] ERC20-Like Token | iteration_4 | role_based       | compiled=NO  | 33.9s +2 retries
  ✓ [15/32] Escrow Contract | iteration_1 | direct_fix       | compiled=YES | 34.9s +1 retry
  ✓ [15/32] Escrow Contract | iteration_1 | chain_of_thought | compiled=YES | 21.4s
  ✓ [15/32] Escrow Contract | iteration_1 | role_based       | compiled=YES | 34.9s +1 retry
  ✗ [16/32] Escrow Contract | iteration_4 | direct_fix       | compiled=NO  | 48.4s +2 retries
  ✓ [16/32] Escrow Contract | iteration_4 | chain_of_thought | compiled=YES | 42.7s +1 retry
  ✗ [16/32] Escrow Contract | iteration_4 | role_based       | compiled=NO  | 50.0s +2 retries
  ✗ [17/32] Multi-Signature Wallet | iteration_0 | direct_fix       | compiled=NO  | 46.9s +2 retries
  ✗ [17/32] Multi-Signature Wallet | iteration_0 | chain_of_thought | compiled=NO  | 50.9s +2 retries
  ✗ [17/32] Multi-Signature Wallet | iteration_0 | role_based       | compiled=NO  | 54.6s +2 retries
  ✗ [18/32] Multi-Signature Wallet | iteration_1 | direct_fix       | compiled=NO  | 43.6s +2 retries
  ✗ [18/32] Multi-Signature Wallet | iteration_1 | chain_of_thought | compiled=NO  | 54.8s +2 retries
  ✗ [18/32] Multi-Signature Wallet | iteration_1 | role_based       | compiled=NO  | 48.5s +2 retries
  ✗ [19/32] Multi-Signature Wallet | iteration_2 | direct_fix       | compiled=NO  | 49.7s +2 retries
  ✗ [19/32] Multi-Signature Wallet | iteration_2 | chain_of_thought | compiled=NO  | 64.1s +2 retries
  ✗ [19/32] Multi-Signature Wallet | iteration_2 | role_based       | compiled=NO  | 51.1s +2 retries
  ✗ [20/32] Multi-Signature Wallet | iteration_3 | direct_fix       | compiled=NO  | 46.4s +2 retries
⠋ [20/32] Multi-Signature Wallet | iteration_3 | chain_of_thought retry 1/2
[WARN] Timeout – retrying (1/2)...
  ✗ [20/32] Multi-Signature Wallet | iteration_3 | chain_of_thought | compiled=NO  | 236.3s +2 retries
  ✗ [20/32] Multi-Signature Wallet | iteration_3 | role_based       | compiled=NO  | 50.2s +2 retries
  ✗ [21/32] Multi-Signature Wallet | iteration_4 | direct_fix       | compiled=NO  | 42.2s +2 retries
  ✗ [21/32] Multi-Signature Wallet | iteration_4 | chain_of_thought | compiled=NO  | 51.6s +2 retries
  ✓ [21/32] Multi-Signature Wallet | iteration_4 | role_based       | compiled=YES | 43.9s +2 retries
  ✗ [22/32] Auction Contract | iteration_0 | direct_fix       | compiled=NO  | 58.3s +2 retries
  ✓ [22/32] Auction Contract | iteration_0 | chain_of_thought | compiled=YES | 23.3s
  ✓ [22/32] Auction Contract | iteration_0 | role_based       | compiled=YES | 44.4s +1 retry
  ✗ [23/32] Auction Contract | iteration_1 | direct_fix       | compiled=NO  | 58.4s +2 retries
  ✗ [23/32] Auction Contract | iteration_1 | chain_of_thought | compiled=NO  | 64.0s +2 retries
  ✗ [23/32] Auction Contract | iteration_1 | role_based       | compiled=NO  | 64.1s +2 retries
  ✗ [24/32] Auction Contract | iteration_2 | direct_fix       | compiled=NO  | 44.2s +2 retries
  ✗ [24/32] Auction Contract | iteration_2 | chain_of_thought | compiled=NO  | 62.0s +2 retries
  ✗ [24/32] Auction Contract | iteration_2 | role_based       | compiled=NO  | 48.6s +2 retries
  ✓ [25/32] Auction Contract | iteration_3 | direct_fix       | compiled=YES | 16.8s
  ✓ [25/32] Auction Contract | iteration_3 | chain_of_thought | compiled=YES | 21.2s
  ✓ [25/32] Auction Contract | iteration_3 | role_based       | compiled=YES | 18.9s
  ✗ [26/32] Auction Contract | iteration_4 | direct_fix       | compiled=NO  | 38.5s +2 retries
  ✗ [26/32] Auction Contract | iteration_4 | chain_of_thought | compiled=NO  | 41.5s +2 retries
  ✗ [26/32] Auction Contract | iteration_4 | role_based       | compiled=NO  | 44.8s +2 retries
  ✗ [27/32] Crowdfunding Contract | iteration_0 | direct_fix       | compiled=NO  | 33.0s +2 retries
  ✗ [27/32] Crowdfunding Contract | iteration_0 | chain_of_thought | compiled=NO  | 47.6s +2 retries
  ✗ [27/32] Crowdfunding Contract | iteration_0 | role_based       | compiled=NO  | 43.4s +2 retries
  ✓ [28/32] Crowdfunding Contract | iteration_1 | direct_fix       | compiled=YES | 12.6s
  ✓ [28/32] Crowdfunding Contract | iteration_1 | chain_of_thought | compiled=YES | 33.0s +1 retry
  ✓ [28/32] Crowdfunding Contract | iteration_1 | role_based       | compiled=YES | 12.8s
  ✗ [29/32] Crowdfunding Contract | iteration_3 | direct_fix       | compiled=NO  | 38.0s +2 retries
  ✗ [29/32] Crowdfunding Contract | iteration_3 | chain_of_thought | compiled=NO  | 48.6s +2 retries
  ✗ [29/32] Crowdfunding Contract | iteration_3 | role_based       | compiled=NO  | 40.9s +2 retries
  ✗ [30/32] Role-Based Access Control | iteration_0 | direct_fix       | compiled=NO  | 56.2s +2 retries
  ✗ [30/32] Role-Based Access Control | iteration_0 | chain_of_thought | compiled=NO  | 67.9s +2 retries
  ✗ [30/32] Role-Based Access Control | iteration_0 | role_based       | compiled=NO  | 78.7s +2 retries
  ✗ [31/32] Role-Based Access Control | iteration_2 | direct_fix       | compiled=NO  | 45.7s +2 retries
  ✓ [31/32] Role-Based Access Control | iteration_2 | chain_of_thought | compiled=YES | 20.2s
  ✗ [31/32] Role-Based Access Control | iteration_2 | role_based       | compiled=NO  | 46.8s +2 retries
  ✗ [32/32] Role-Based Access Control | iteration_3 | direct_fix       | compiled=NO  | 32.8s +2 retries
  ✗ [32/32] Role-Based Access Control | iteration_3 | chain_of_thought | compiled=NO  | 43.8s +2 retries
  ✗ [32/32] Role-Based Access Control | iteration_3 | role_based       | compiled=NO  | 45.3s +2 retries
✓ Finished repairs for llama3.1:8b [32/32] Role-Based Access Control | iteration_3 | role_based retry 2/2

================================================================================
[MODEL] ministral-3:8b  (27 contract(s) to repair)
================================================================================

  ✗ [1/27] Ownership and Access Control | iteration_2 | direct_fix       | compiled=NO  | 22.7s +2 retries
  ✓ [1/27] Ownership and Access Control | iteration_2 | chain_of_thought | compiled=YES | 8.8s
  ✗ [1/27] Ownership and Access Control | iteration_2 | role_based       | compiled=NO  | 17.6s +2 retries
  ✗ [2/27] Ownership and Access Control | iteration_4 | direct_fix       | compiled=NO  | 20.1s +2 retries
  ✓ [2/27] Ownership and Access Control | iteration_4 | chain_of_thought | compiled=YES | 25.9s +2 retries
  ✗ [2/27] Ownership and Access Control | iteration_4 | role_based       | compiled=NO  | 21.2s +2 retries
  ✓ [3/27] Time-Locked Wallet | iteration_0 | direct_fix       | compiled=YES | 8.9s
  ✓ [3/27] Time-Locked Wallet | iteration_0 | chain_of_thought | compiled=YES | 24.8s +1 retry
  ✓ [3/27] Time-Locked Wallet | iteration_0 | role_based       | compiled=YES | 13.7s
  ✗ [4/27] Simple Voting System | iteration_1 | direct_fix       | compiled=NO  | 43.0s +2 retries
  ✓ [4/27] Simple Voting System | iteration_1 | chain_of_thought | compiled=YES | 41.7s +1 retry
  ✓ [4/27] Simple Voting System | iteration_1 | role_based       | compiled=YES | 34.3s +1 retry
  ✓ [5/27] Simple Voting System | iteration_4 | direct_fix       | compiled=YES | 18.3s
  ✓ [5/27] Simple Voting System | iteration_4 | chain_of_thought | compiled=YES | 25.4s
  ✓ [5/27] Simple Voting System | iteration_4 | role_based       | compiled=YES | 22.0s
  ✓ [6/27] ERC20-Like Token | iteration_0 | direct_fix       | compiled=YES | 18.2s
  ✓ [6/27] ERC20-Like Token | iteration_0 | chain_of_thought | compiled=YES | 22.4s
  ✓ [6/27] ERC20-Like Token | iteration_0 | role_based       | compiled=YES | 20.6s
  ✓ [7/27] Escrow Contract | iteration_0 | direct_fix       | compiled=YES | 46.5s +1 retry
  ✓ [7/27] Escrow Contract | iteration_0 | chain_of_thought | compiled=YES | 26.2s
  ✓ [7/27] Escrow Contract | iteration_0 | role_based       | compiled=YES | 24.5s
  ✓ [8/27] Escrow Contract | iteration_2 | direct_fix       | compiled=YES | 69.1s +2 retries
  ✓ [8/27] Escrow Contract | iteration_2 | chain_of_thought | compiled=YES | 25.2s
  ✓ [8/27] Escrow Contract | iteration_2 | role_based       | compiled=YES | 49.0s +1 retry
  ✗ [9/27] Escrow Contract | iteration_3 | direct_fix       | compiled=NO  | 75.3s +2 retries
  ✗ [9/27] Escrow Contract | iteration_3 | chain_of_thought | compiled=NO  | 84.1s +2 retries
  ✗ [9/27] Escrow Contract | iteration_3 | role_based       | compiled=NO  | 84.9s +2 retries
  ✓ [10/27] Escrow Contract | iteration_4 | direct_fix       | compiled=YES | 24.9s
  ✓ [10/27] Escrow Contract | iteration_4 | chain_of_thought | compiled=YES | 27.8s
  ✓ [10/27] Escrow Contract | iteration_4 | role_based       | compiled=YES | 27.0s
  ✓ [11/27] Multi-Signature Wallet | iteration_0 | direct_fix       | compiled=YES | 61.3s +2 retries
  ✗ [11/27] Multi-Signature Wallet | iteration_0 | chain_of_thought | compiled=NO  | 72.1s +2 retries
  ✗ [11/27] Multi-Signature Wallet | iteration_0 | role_based       | compiled=NO  | 72.6s +2 retries
  ✗ [12/27] Multi-Signature Wallet | iteration_1 | direct_fix       | compiled=NO  | 56.5s +2 retries
  ✗ [12/27] Multi-Signature Wallet | iteration_1 | chain_of_thought | compiled=NO  | 64.7s +2 retries
  ✗ [12/27] Multi-Signature Wallet | iteration_1 | role_based       | compiled=NO  | 64.1s +2 retries
  ✗ [13/27] Multi-Signature Wallet | iteration_2 | direct_fix       | compiled=NO  | 60.1s +2 retries
  ✗ [13/27] Multi-Signature Wallet | iteration_2 | chain_of_thought | compiled=NO  | 73.5s +2 retries
  ✗ [13/27] Multi-Signature Wallet | iteration_2 | role_based       | compiled=NO  | 87.9s +2 retries
  ✗ [14/27] Multi-Signature Wallet | iteration_4 | direct_fix       | compiled=NO  | 75.3s +2 retries
  ✗ [14/27] Multi-Signature Wallet | iteration_4 | chain_of_thought | compiled=NO  | 78.1s +2 retries
  ✗ [14/27] Multi-Signature Wallet | iteration_4 | role_based       | compiled=NO  | 66.8s +2 retries
  ✓ [15/27] Auction Contract | iteration_0 | direct_fix       | compiled=YES | 35.8s +1 retry
  ✗ [15/27] Auction Contract | iteration_0 | chain_of_thought | compiled=NO  | 70.2s +2 retries
  ✗ [15/27] Auction Contract | iteration_0 | role_based       | compiled=NO  | 74.8s +2 retries
  ✗ [16/27] Auction Contract | iteration_1 | direct_fix       | compiled=NO  | 61.3s +2 retries
  ✗ [16/27] Auction Contract | iteration_1 | chain_of_thought | compiled=NO  | 78.9s +2 retries
  ✓ [16/27] Auction Contract | iteration_1 | role_based       | compiled=YES | 66.3s +2 retries
  ✓ [17/27] Auction Contract | iteration_2 | direct_fix       | compiled=YES | 18.7s
  ✓ [17/27] Auction Contract | iteration_2 | chain_of_thought | compiled=YES | 75.6s +2 retries
  ✗ [17/27] Auction Contract | iteration_2 | role_based       | compiled=NO  | 58.2s +2 retries
  ✓ [18/27] Auction Contract | iteration_3 | direct_fix       | compiled=YES | 20.6s
  ✓ [18/27] Auction Contract | iteration_3 | chain_of_thought | compiled=YES | 25.9s
  ✓ [18/27] Auction Contract | iteration_3 | role_based       | compiled=YES | 23.4s
  ✓ [19/27] Auction Contract | iteration_4 | direct_fix       | compiled=YES | 20.5s
  ✓ [19/27] Auction Contract | iteration_4 | chain_of_thought | compiled=YES | 25.5s
  ✓ [19/27] Auction Contract | iteration_4 | role_based       | compiled=YES | 22.6s
  ✓ [20/27] Subscription Payment System | iteration_0 | direct_fix       | compiled=YES | 14.2s
  ✓ [20/27] Subscription Payment System | iteration_0 | chain_of_thought | compiled=YES | 18.7s
  ✓ [20/27] Subscription Payment System | iteration_0 | role_based       | compiled=YES | 16.7s
  ✗ [21/27] Crowdfunding Contract | iteration_2 | direct_fix       | compiled=NO  | 63.8s +2 retries
  ✓ [21/27] Crowdfunding Contract | iteration_2 | chain_of_thought | compiled=YES | 25.6s
  ✗ [21/27] Crowdfunding Contract | iteration_2 | role_based       | compiled=NO  | 80.3s +2 retries
  ✗ [22/27] Crowdfunding Contract | iteration_3 | direct_fix       | compiled=NO  | 65.3s +2 retries
  ✗ [22/27] Crowdfunding Contract | iteration_3 | chain_of_thought | compiled=NO  | 83.9s +2 retries
  ✗ [22/27] Crowdfunding Contract | iteration_3 | role_based       | compiled=NO  | 80.7s +2 retries
  ✗ [23/27] Crowdfunding Contract | iteration_4 | direct_fix       | compiled=NO  | 51.8s +2 retries
  ✗ [23/27] Crowdfunding Contract | iteration_4 | chain_of_thought | compiled=NO  | 71.8s +2 retries
  ✗ [23/27] Crowdfunding Contract | iteration_4 | role_based       | compiled=NO  | 59.3s +2 retries
  ✗ [24/27] Role-Based Access Control | iteration_0 | direct_fix       | compiled=NO  | 57.6s +2 retries
  ✓ [24/27] Role-Based Access Control | iteration_0 | chain_of_thought | compiled=YES | 43.6s +1 retry
  ✗ [24/27] Role-Based Access Control | iteration_0 | role_based       | compiled=NO  | 64.4s +2 retries
  ✓ [25/27] Role-Based Access Control | iteration_1 | direct_fix       | compiled=YES | 30.1s +1 retry
  ✓ [25/27] Role-Based Access Control | iteration_1 | chain_of_thought | compiled=YES | 19.1s
  ✓ [25/27] Role-Based Access Control | iteration_1 | role_based       | compiled=YES | 47.5s +2 retries
  ✓ [26/27] Role-Based Access Control | iteration_3 | direct_fix       | compiled=YES | 36.3s +1 retry
  ✓ [26/27] Role-Based Access Control | iteration_3 | chain_of_thought | compiled=YES | 21.1s
  ✗ [26/27] Role-Based Access Control | iteration_3 | role_based       | compiled=NO  | 56.4s +2 retries
  ✗ [27/27] Role-Based Access Control | iteration_4 | direct_fix       | compiled=NO  | 57.3s +2 retries
  ✓ [27/27] Role-Based Access Control | iteration_4 | chain_of_thought | compiled=YES | 22.0s
  ✗ [27/27] Role-Based Access Control | iteration_4 | role_based       | compiled=NO  | 57.2s +2 retries
✓ Finished repairs for ministral-3:8b [27/27] Role-Based Access Control | iteration_4 | role_based retry 2/2

================================================================================
[MODEL] qwen2.5-coder:7b  (14 contract(s) to repair)
================================================================================

  ✗ [1/14] Simple Voting System | iteration_0 | direct_fix       | compiled=NO  | 29.4s +2 retries
  ✗ [1/14] Simple Voting System | iteration_0 | chain_of_thought | compiled=NO  | 45.4s +2 retries
  ✗ [1/14] Simple Voting System | iteration_0 | role_based       | compiled=NO  | 27.0s +2 retries
  ✗ [2/14] Simple Voting System | iteration_1 | direct_fix       | compiled=NO  | 28.4s +2 retries
  ✓ [2/14] Simple Voting System | iteration_1 | chain_of_thought | compiled=YES | 17.9s
  ✗ [2/14] Simple Voting System | iteration_1 | role_based       | compiled=NO  | 26.8s +2 retries
  ✗ [3/14] Simple Voting System | iteration_2 | direct_fix       | compiled=NO  | 30.2s +2 retries
  ✓ [3/14] Simple Voting System | iteration_2 | chain_of_thought | compiled=YES | 57.2s +2 retries
  ✗ [3/14] Simple Voting System | iteration_2 | role_based       | compiled=NO  | 30.3s +2 retries
  ✗ [4/14] Simple Voting System | iteration_3 | direct_fix       | compiled=NO  | 35.7s +2 retries
  ✗ [4/14] Simple Voting System | iteration_3 | chain_of_thought | compiled=NO  | 55.8s +2 retries
  ✗ [4/14] Simple Voting System | iteration_3 | role_based       | compiled=NO  | 35.6s +2 retries
  ✗ [5/14] Simple Voting System | iteration_4 | direct_fix       | compiled=NO  | 26.7s +2 retries
  ✗ [5/14] Simple Voting System | iteration_4 | chain_of_thought | compiled=NO  | 49.0s +2 retries
  ✗ [5/14] Simple Voting System | iteration_4 | role_based       | compiled=NO  | 27.8s +2 retries
  ✗ [6/14] Multi-Signature Wallet | iteration_0 | direct_fix       | compiled=NO  | 33.5s +2 retries
  ✗ [6/14] Multi-Signature Wallet | iteration_0 | chain_of_thought | compiled=NO  | 49.3s +2 retries
  ✗ [6/14] Multi-Signature Wallet | iteration_0 | role_based       | compiled=NO  | 33.5s +2 retries
  ✗ [7/14] Multi-Signature Wallet | iteration_2 | direct_fix       | compiled=NO  | 39.3s +2 retries
  ✗ [7/14] Multi-Signature Wallet | iteration_2 | chain_of_thought | compiled=NO  | 51.3s +2 retries
  ✗ [7/14] Multi-Signature Wallet | iteration_2 | role_based       | compiled=NO  | 39.2s +2 retries
  ✗ [8/14] Multi-Signature Wallet | iteration_3 | direct_fix       | compiled=NO  | 34.3s +2 retries
  ✓ [8/14] Multi-Signature Wallet | iteration_3 | chain_of_thought | compiled=YES | 34.6s +1 retry
  ✓ [8/14] Multi-Signature Wallet | iteration_3 | role_based       | compiled=YES | 12.6s
  ✗ [9/14] Crowdfunding Contract | iteration_3 | direct_fix       | compiled=NO  | 37.2s +2 retries
  ✗ [9/14] Crowdfunding Contract | iteration_3 | chain_of_thought | compiled=NO  | 50.0s +2 retries
  ✗ [9/14] Crowdfunding Contract | iteration_3 | role_based       | compiled=NO  | 37.2s +2 retries
  ✗ [10/14] Role-Based Access Control | iteration_0 | direct_fix       | compiled=NO  | 35.4s +2 retries
  ✓ [10/14] Role-Based Access Control | iteration_0 | chain_of_thought | compiled=YES | 16.8s
  ✗ [10/14] Role-Based Access Control | iteration_0 | role_based       | compiled=NO  | 35.2s +2 retries
  ✗ [11/14] Role-Based Access Control | iteration_1 | direct_fix       | compiled=NO  | 31.8s +2 retries
  ✗ [11/14] Role-Based Access Control | iteration_1 | chain_of_thought | compiled=NO  | 40.0s +2 retries
  ✗ [11/14] Role-Based Access Control | iteration_1 | role_based       | compiled=NO  | 31.9s +2 retries
  ✗ [12/14] Role-Based Access Control | iteration_2 | direct_fix       | compiled=NO  | 34.6s +2 retries
  ✓ [12/14] Role-Based Access Control | iteration_2 | chain_of_thought | compiled=YES | 16.2s
  ✗ [12/14] Role-Based Access Control | iteration_2 | role_based       | compiled=NO  | 37.4s +2 retries
  ✗ [13/14] Role-Based Access Control | iteration_3 | direct_fix       | compiled=NO  | 34.4s +2 retries
  ✓ [13/14] Role-Based Access Control | iteration_3 | chain_of_thought | compiled=YES | 17.4s
  ✗ [13/14] Role-Based Access Control | iteration_3 | role_based       | compiled=NO  | 35.0s +2 retries
  ✗ [14/14] Role-Based Access Control | iteration_4 | direct_fix       | compiled=NO  | 31.1s +2 retries
  ✗ [14/14] Role-Based Access Control | iteration_4 | chain_of_thought | compiled=NO  | 39.0s +2 retries
  ✗ [14/14] Role-Based Access Control | iteration_4 | role_based       | compiled=NO  | 31.0s +2 retries
✓ Finished repairs for qwen2.5-coder:7b [14/14] Role-Based Access Control | iteration_4 | role_based retry 2/2

================================================================================
[MODEL] qwen3:8b  (9 contract(s) to repair)
================================================================================

  ✓ [1/9] Simple Voting System | iteration_2 | direct_fix       | compiled=YES | 49.2s
  ✓ [1/9] Simple Voting System | iteration_2 | chain_of_thought | compiled=YES | 135.2s +2 retries
  ✓ [1/9] Simple Voting System | iteration_2 | role_based       | compiled=YES | 45.6s
  ✓ [2/9] ERC20-Like Token | iteration_1 | direct_fix       | compiled=YES | 27.4s
⠦ [2/9] ERC20-Like Token | iteration_1 | chain_of_thought retry 1/2
[WARN] Timeout – retrying (1/2)...
  ✓ [2/9] ERC20-Like Token | iteration_1 | chain_of_thought | compiled=YES | 266.5s +1 retry
  ✓ [2/9] ERC20-Like Token | iteration_1 | role_based       | compiled=YES | 44.5s
  ✓ [3/9] Escrow Contract | iteration_0 | direct_fix       | compiled=YES | 50.4s
⠋ [3/9] Escrow Contract | iteration_0 | chain_of_thought
[WARN] Timeout – retrying (1/2)...
⠹ [3/9] Escrow Contract | iteration_0 | chain_of_thought
[WARN] Timeout – retrying (2/2)...
  ✓ [3/9] Escrow Contract | iteration_0 | chain_of_thought | compiled=YES | 423.2s
  ✓ [3/9] Escrow Contract | iteration_0 | role_based       | compiled=YES | 80.1s
  ✓ [4/9] Escrow Contract | iteration_3 | direct_fix       | compiled=YES | 23.0s
  ✓ [4/9] Escrow Contract | iteration_3 | chain_of_thought | compiled=YES | 27.1s
⠧ [4/9] Escrow Contract | iteration_3 | role_based
[WARN] Timeout – retrying (1/2)...
  ✓ [4/9] Escrow Contract | iteration_3 | role_based       | compiled=YES | 215.7s
⠏ [5/9] Multi-Signature Wallet | iteration_0 | direct_fix
[WARN] Timeout – retrying (1/2)...
⠋ [5/9] Multi-Signature Wallet | iteration_0 | direct_fix
[WARN] Timeout – retrying (2/2)...
  ✓ [5/9] Multi-Signature Wallet | iteration_0 | direct_fix       | compiled=YES | 566.9s +2 retries
  ✗ [5/9] Multi-Signature Wallet | iteration_0 | chain_of_thought | compiled=NO  | 119.0s +2 retries
  ✗ [5/9] Multi-Signature Wallet | iteration_0 | role_based       | compiled=NO  | 182.1s +2 retries
⠙ [6/9] Multi-Signature Wallet | iteration_1 | direct_fix
[WARN] Timeout – retrying (1/2)...
  ✓ [6/9] Multi-Signature Wallet | iteration_1 | direct_fix       | compiled=YES | 288.1s
  ✓ [6/9] Multi-Signature Wallet | iteration_1 | chain_of_thought | compiled=YES | 85.7s
  ✓ [6/9] Multi-Signature Wallet | iteration_1 | role_based       | compiled=YES | 68.5s
  ✓ [7/9] Auction Contract | iteration_0 | direct_fix       | compiled=YES | 28.0s
  ✓ [7/9] Auction Contract | iteration_0 | chain_of_thought | compiled=YES | 19.4s
  ✓ [7/9] Auction Contract | iteration_0 | role_based       | compiled=YES | 59.5s
  ✓ [8/9] Role-Based Access Control | iteration_0 | direct_fix       | compiled=YES | 48.9s
  ✓ [8/9] Role-Based Access Control | iteration_0 | chain_of_thought | compiled=YES | 45.2s
⠏ [8/9] Role-Based Access Control | iteration_0 | role_based
[WARN] Timeout – retrying (1/2)...
  ✓ [8/9] Role-Based Access Control | iteration_0 | role_based       | compiled=YES | 303.2s +1 retry
  ✓ [9/9] Role-Based Access Control | iteration_2 | direct_fix       | compiled=YES | 43.8s
  ✓ [9/9] Role-Based Access Control | iteration_2 | chain_of_thought | compiled=YES | 32.6s
  ✓ [9/9] Role-Based Access Control | iteration_2 | role_based       | compiled=YES | 58.9s
✓ Finished repairs for qwen3:8b [9/9] Role-Based Access Control | iteration_2 | role_based

================================================================================
[MODEL] gemma3:27b  (8 contract(s) to repair)
================================================================================

  ✗ [1/8] Escrow Contract | iteration_3 | direct_fix       | compiled=NO  | 170.8s +2 retries
  ✓ [1/8] Escrow Contract | iteration_3 | chain_of_thought | compiled=YES | 65.6s
  ✗ [1/8] Escrow Contract | iteration_3 | role_based       | compiled=NO  | 159.5s +2 retries
  ✗ [2/8] Escrow Contract | iteration_4 | direct_fix       | compiled=NO  | 171.2s +2 retries
  ✓ [2/8] Escrow Contract | iteration_4 | chain_of_thought | compiled=YES | 197.8s +2 retries
  ✗ [2/8] Escrow Contract | iteration_4 | role_based       | compiled=NO  | 189.0s +2 retries
  ✗ [3/8] Multi-Signature Wallet | iteration_0 | direct_fix       | compiled=NO  | 172.8s +2 retries
  ✓ [3/8] Multi-Signature Wallet | iteration_0 | chain_of_thought | compiled=YES | 76.4s
  ✗ [3/8] Multi-Signature Wallet | iteration_0 | role_based       | compiled=NO  | 178.4s +2 retries
  ✓ [4/8] Multi-Signature Wallet | iteration_1 | direct_fix       | compiled=YES | 55.2s
  ✓ [4/8] Multi-Signature Wallet | iteration_1 | chain_of_thought | compiled=YES | 60.8s
  ✓ [4/8] Multi-Signature Wallet | iteration_1 | role_based       | compiled=YES | 131.3s +1 retry
  ✓ [5/8] Multi-Signature Wallet | iteration_2 | direct_fix       | compiled=YES | 101.3s +1 retry
  ✓ [5/8] Multi-Signature Wallet | iteration_2 | chain_of_thought | compiled=YES | 71.3s
  ✓ [5/8] Multi-Signature Wallet | iteration_2 | role_based       | compiled=YES | 59.9s
  ✓ [6/8] Multi-Signature Wallet | iteration_3 | direct_fix       | compiled=YES | 47.3s
  ✗ [6/8] Multi-Signature Wallet | iteration_3 | chain_of_thought | compiled=NO  | 199.1s +2 retries
  ✓ [6/8] Multi-Signature Wallet | iteration_3 | role_based       | compiled=YES | 48.5s
  ✓ [7/8] Multi-Signature Wallet | iteration_4 | direct_fix       | compiled=YES | 49.1s
  ✓ [7/8] Multi-Signature Wallet | iteration_4 | chain_of_thought | compiled=YES | 65.4s
  ✓ [7/8] Multi-Signature Wallet | iteration_4 | role_based       | compiled=YES | 121.9s +1 retry
  ✗ [8/8] Crowdfunding Contract | iteration_1 | direct_fix       | compiled=NO  | 140.3s +2 retries
  ✗ [8/8] Crowdfunding Contract | iteration_1 | chain_of_thought | compiled=NO  | 163.7s +2 retries
  ✗ [8/8] Crowdfunding Contract | iteration_1 | role_based       | compiled=NO  | 141.1s +2 retries
✓ Finished repairs for gemma3:27b [8/8] Crowdfunding Contract | iteration_1 | role_based retry 2/2

================================================================================
[MODEL] gpt-oss:20b  (5 contract(s) to repair)
================================================================================

  ✓ [1/5] Auction Contract | iteration_0 | direct_fix       | compiled=YES | 30.3s
  ✓ [1/5] Auction Contract | iteration_0 | chain_of_thought | compiled=YES | 26.6s
  ✓ [1/5] Auction Contract | iteration_0 | role_based       | compiled=YES | 59.9s +1 retry
  ✓ [2/5] Auction Contract | iteration_1 | direct_fix       | compiled=YES | 32.1s
  ✓ [2/5] Auction Contract | iteration_1 | chain_of_thought | compiled=YES | 61.1s +1 retry
  ✓ [2/5] Auction Contract | iteration_1 | role_based       | compiled=YES | 32.5s
  ✓ [3/5] Crowdfunding Contract | iteration_1 | direct_fix       | compiled=YES | 33.3s
  ✓ [3/5] Crowdfunding Contract | iteration_1 | chain_of_thought | compiled=YES | 24.0s
  ✓ [3/5] Crowdfunding Contract | iteration_1 | role_based       | compiled=YES | 24.3s
  ✓ [4/5] Crowdfunding Contract | iteration_3 | direct_fix       | compiled=YES | 101.7s +1 retry
  ✓ [4/5] Crowdfunding Contract | iteration_3 | chain_of_thought | compiled=YES | 42.5s
  ✓ [4/5] Crowdfunding Contract | iteration_3 | role_based       | compiled=YES | 27.8s
  ✓ [5/5] Role-Based Access Control | iteration_0 | direct_fix       | compiled=YES | 22.4s
  ✓ [5/5] Role-Based Access Control | iteration_0 | chain_of_thought | compiled=YES | 24.2s
  ✓ [5/5] Role-Based Access Control | iteration_0 | role_based       | compiled=YES | 33.9s
✓ Finished repairs for gpt-oss:20b [5/5] Role-Based Access Control | iteration_0 | role_based

================================================================================
[MODEL] mistral-small:24b  (22 contract(s) to repair)
================================================================================

  ✗ [1/22] Ownership and Access Control | iteration_0 | direct_fix       | compiled=NO  | 36.5s +2 retries
  ✗ [1/22] Ownership and Access Control | iteration_0 | chain_of_thought | compiled=NO  | 57.8s +2 retries
  ✗ [1/22] Ownership and Access Control | iteration_0 | role_based       | compiled=NO  | 28.2s +2 retries
  ✗ [2/22] Ownership and Access Control | iteration_1 | direct_fix       | compiled=NO  | 27.7s +2 retries
  ✗ [2/22] Ownership and Access Control | iteration_1 | chain_of_thought | compiled=NO  | 55.7s +2 retries
  ✗ [2/22] Ownership and Access Control | iteration_1 | role_based       | compiled=NO  | 27.5s +2 retries
  ✗ [3/22] Ownership and Access Control | iteration_4 | direct_fix       | compiled=NO  | 26.9s +2 retries
  ✗ [3/22] Ownership and Access Control | iteration_4 | chain_of_thought | compiled=NO  | 62.8s +2 retries
  ✗ [3/22] Ownership and Access Control | iteration_4 | role_based       | compiled=NO  | 28.8s +2 retries
  ✓ [4/22] Simple Voting System | iteration_0 | direct_fix       | compiled=YES | 58.6s +1 retry
  ✓ [4/22] Simple Voting System | iteration_0 | chain_of_thought | compiled=YES | 75.2s +1 retry
  ✓ [4/22] Simple Voting System | iteration_0 | role_based       | compiled=YES | 58.7s +1 retry
  ✓ [5/22] Simple Voting System | iteration_1 | direct_fix       | compiled=YES | 32.0s
  ✓ [5/22] Simple Voting System | iteration_1 | chain_of_thought | compiled=YES | 40.2s
  ✓ [5/22] Simple Voting System | iteration_1 | role_based       | compiled=YES | 32.0s
  ✓ [6/22] Simple Voting System | iteration_2 | direct_fix       | compiled=YES | 26.0s
  ✓ [6/22] Simple Voting System | iteration_2 | chain_of_thought | compiled=YES | 42.0s
  ✓ [6/22] Simple Voting System | iteration_2 | role_based       | compiled=YES | 26.4s
  ✓ [7/22] Simple Voting System | iteration_3 | direct_fix       | compiled=YES | 51.0s +1 retry
  ✓ [7/22] Simple Voting System | iteration_3 | chain_of_thought | compiled=YES | 39.2s
  ✓ [7/22] Simple Voting System | iteration_3 | role_based       | compiled=YES | 26.2s
  ✓ [8/22] Simple Voting System | iteration_4 | direct_fix       | compiled=YES | 35.1s
  ✓ [8/22] Simple Voting System | iteration_4 | chain_of_thought | compiled=YES | 41.1s
  ✓ [8/22] Simple Voting System | iteration_4 | role_based       | compiled=YES | 63.9s +1 retry
  ✗ [9/22] Multi-Signature Wallet | iteration_0 | direct_fix       | compiled=NO  | 101.8s +2 retries
  ✓ [9/22] Multi-Signature Wallet | iteration_0 | chain_of_thought | compiled=YES | 82.1s +1 retry
  ✗ [9/22] Multi-Signature Wallet | iteration_0 | role_based       | compiled=NO  | 108.6s +2 retries
  ✗ [10/22] Multi-Signature Wallet | iteration_1 | direct_fix       | compiled=NO  | 105.0s +2 retries
  ✗ [10/22] Multi-Signature Wallet | iteration_1 | chain_of_thought | compiled=NO  | 138.6s +2 retries
  ✗ [10/22] Multi-Signature Wallet | iteration_1 | role_based       | compiled=NO  | 107.8s +2 retries
  ✗ [11/22] Multi-Signature Wallet | iteration_2 | direct_fix       | compiled=NO  | 103.6s +2 retries
  ✗ [11/22] Multi-Signature Wallet | iteration_2 | chain_of_thought | compiled=NO  | 136.1s +2 retries
  ✗ [11/22] Multi-Signature Wallet | iteration_2 | role_based       | compiled=NO  | 103.8s +2 retries
  ✓ [12/22] Multi-Signature Wallet | iteration_3 | direct_fix       | compiled=YES | 109.9s +2 retries
  ✓ [12/22] Multi-Signature Wallet | iteration_3 | chain_of_thought | compiled=YES | 88.1s +1 retry
  ✗ [12/22] Multi-Signature Wallet | iteration_3 | role_based       | compiled=NO  | 108.0s +2 retries
  ✗ [13/22] Multi-Signature Wallet | iteration_4 | direct_fix       | compiled=NO  | 119.8s +2 retries
  ✓ [13/22] Multi-Signature Wallet | iteration_4 | chain_of_thought | compiled=YES | 151.4s +2 retries
  ✗ [13/22] Multi-Signature Wallet | iteration_4 | role_based       | compiled=NO  | 120.5s +2 retries
  ✓ [14/22] Auction Contract | iteration_0 | direct_fix       | compiled=YES | 59.6s +1 retry
  ✓ [14/22] Auction Contract | iteration_0 | chain_of_thought | compiled=YES | 35.9s
  ✗ [14/22] Auction Contract | iteration_0 | role_based       | compiled=NO  | 91.2s +2 retries
  ✓ [15/22] Auction Contract | iteration_3 | direct_fix       | compiled=YES | 32.8s
  ✓ [15/22] Auction Contract | iteration_3 | chain_of_thought | compiled=YES | 55.4s
  ✓ [15/22] Auction Contract | iteration_3 | role_based       | compiled=YES | 32.8s
  ✓ [16/22] Auction Contract | iteration_4 | direct_fix       | compiled=YES | 28.4s
  ✓ [16/22] Auction Contract | iteration_4 | chain_of_thought | compiled=YES | 83.1s +1 retry
  ✓ [16/22] Auction Contract | iteration_4 | role_based       | compiled=YES | 56.9s +1 retry
  ✗ [17/22] Crowdfunding Contract | iteration_4 | direct_fix       | compiled=NO  | 77.1s +2 retries
  ✗ [17/22] Crowdfunding Contract | iteration_4 | chain_of_thought | compiled=NO  | 95.2s +2 retries
  ✗ [17/22] Crowdfunding Contract | iteration_4 | role_based       | compiled=NO  | 75.0s +2 retries
  ✓ [18/22] Role-Based Access Control | iteration_0 | direct_fix       | compiled=YES | 88.4s +2 retries
  ✗ [18/22] Role-Based Access Control | iteration_0 | chain_of_thought | compiled=NO  | 123.8s +2 retries
  ✓ [18/22] Role-Based Access Control | iteration_0 | role_based       | compiled=YES | 31.6s
  ✓ [19/22] Role-Based Access Control | iteration_1 | direct_fix       | compiled=YES | 65.1s +1 retry
  ✗ [19/22] Role-Based Access Control | iteration_1 | chain_of_thought | compiled=NO  | 131.9s +2 retries
  ✓ [19/22] Role-Based Access Control | iteration_1 | role_based       | compiled=YES | 64.8s +1 retry
  ✓ [20/22] Role-Based Access Control | iteration_2 | direct_fix       | compiled=YES | 93.5s +2 retries
  ✗ [20/22] Role-Based Access Control | iteration_2 | chain_of_thought | compiled=NO  | 118.0s +2 retries
  ✓ [20/22] Role-Based Access Control | iteration_2 | role_based       | compiled=YES | 34.6s
  ✓ [21/22] Role-Based Access Control | iteration_3 | direct_fix       | compiled=YES | 60.9s +1 retry
  ✗ [21/22] Role-Based Access Control | iteration_3 | chain_of_thought | compiled=NO  | 108.5s +2 retries
  ✗ [21/22] Role-Based Access Control | iteration_3 | role_based       | compiled=NO  | 87.5s +2 retries
  ✓ [22/22] Role-Based Access Control | iteration_4 | direct_fix       | compiled=YES | 62.4s +1 retry
  ✗ [22/22] Role-Based Access Control | iteration_4 | chain_of_thought | compiled=NO  | 121.9s +2 retries
  ✗ [22/22] Role-Based Access Control | iteration_4 | role_based       | compiled=NO  | 90.5s +2 retries
✓ Finished repairs for mistral-small:24b [22/22] Role-Based Access Control | iteration_4 | role_based retry 2/2

[TIMING] Total repair time: 27292.7s (454.9 min)

[AGGREGATE] Computing repair statistics...

[AGGREGATE] Done.

[SAVED] output\repair_cp_results.json
[SAVED] output\repair_cp_summary.json
[SAVED] output\repair_cp_report.txt

================================================================================
                         COMPILATION REPAIR QUICK SUMMARY
================================================================================

[deepseek-coder:6.7b]
  Failed contracts attempted : 25
  direct_fix          : 8 repaired / 25 (32.0%)  clean=4  H=0 M=1 L=3
  chain_of_thought    : 9 repaired / 25 (36.0%)  clean=5  H=0 M=2 L=5
  role_based          : 10 repaired / 25 (40.0%)  clean=6  H=0 M=0 L=4

[granite4.1:8b]
  Failed contracts attempted : 36
  direct_fix          : 13 repaired / 36 (36.1%)  clean=7  H=0 M=4 L=4
  chain_of_thought    : 15 repaired / 36 (41.7%)  clean=6  H=0 M=7 L=4
  role_based          : 13 repaired / 36 (36.1%)  clean=7  H=1 M=5 L=3

[llama3.1:8b]
  Failed contracts attempted : 32
  direct_fix          : 4 repaired / 32 (12.5%)  clean=1  H=1 M=2 L=3
  chain_of_thought    : 14 repaired / 32 (43.8%)  clean=4  H=4 M=8 L=3
  role_based          : 8 repaired / 32 (25.0%)  clean=1  H=2 M=5 L=5

[ministral-3:8b]
  Failed contracts attempted : 27
  direct_fix          : 14 repaired / 27 (51.9%)  clean=3  H=0 M=11 L=13
  chain_of_thought    : 18 repaired / 27 (66.7%)  clean=7  H=0 M=15 L=9
  role_based          : 12 repaired / 27 (44.4%)  clean=2  H=2 M=11 L=8

[qwen2.5-coder:7b]
  Failed contracts attempted : 14
  direct_fix          : 0 repaired / 14 (0.0%)  clean=0  H=0 M=0 L=0
  chain_of_thought    : 6 repaired / 14 (42.9%)  clean=3  H=1 M=0 L=0
  role_based          : 1 repaired / 14 (7.1%)  clean=0  H=1 M=0 L=0

[qwen3:8b]
  Failed contracts attempted : 9
  direct_fix          : 9 repaired / 9 (100.0%)  clean=5  H=0 M=2 L=3
  chain_of_thought    : 8 repaired / 9 (88.9%)  clean=4  H=1 M=2 L=3
  role_based          : 8 repaired / 9 (88.9%)  clean=4  H=0 M=2 L=3

[gemma3:27b]
  Failed contracts attempted : 8
  direct_fix          : 4 repaired / 8 (50.0%)  clean=2  H=0 M=3 L=0
  chain_of_thought    : 6 repaired / 8 (75.0%)  clean=1  H=1 M=4 L=2
  role_based          : 4 repaired / 8 (50.0%)  clean=1  H=0 M=3 L=0

[gpt-oss:20b]
  Failed contracts attempted : 5
  direct_fix          : 5 repaired / 5 (100.0%)  clean=1  H=0 M=1 L=6
  chain_of_thought    : 5 repaired / 5 (100.0%)  clean=1  H=0 M=0 L=6
  role_based          : 5 repaired / 5 (100.0%)  clean=1  H=0 M=0 L=6

[mistral-small:24b]
  Failed contracts attempted : 22
  direct_fix          : 14 repaired / 22 (63.6%)  clean=6  H=0 M=4 L=3
  chain_of_thought    : 11 repaired / 22 (50.0%)  clean=1  H=1 M=8 L=3
  role_based          : 10 repaired / 22 (45.5%)  clean=4  H=0 M=2 L=2
================================================================================

================================================================================
[SUCCESS] Compilation repair pipeline complete!
          Results in: output/repair_cp_results.json
          Summary in: output/repair_cp_summary.json
          Report  in: output/repair_cp_report.txt
          Repaired .sol files in: output/compilation_repairs/
================================================================================

[INFO] Pipeline completed at: 2026-06-11T16:44:43.040235