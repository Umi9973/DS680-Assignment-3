# PuchenLiu — Evaluation Artifacts for Agent Disclosure & System Identity

This folder contains all evaluation artifacts for DS680 Assignment 3, including:

- Automated agent disclosure in user-facing interactions  
- System identity, capabilities, and limitations communicated in context  
- GPT‑4.1 vs GPT‑5 comparison summary  
- Qwen‑score automated evaluation  
- All raw JSON/TXT model outputs, experiment scripts, and scoring files  

Files are organized by task module and model version for clarity and reproducibility.

---

## 📁 Directory Structure

```
PuchenLiu/
│── Automated agent disclosure in user-facing interactions/     # Evaluation of agent identity disclosure behavior
│     ├── GPT4.1/                                               # Results generated using GPT-4.1
│     │     ├── automated_agent_gpt4.1_xxx.json                 # Raw JSON output for disclosure evaluation (GPT-4.1)
│     │     ├── automated_agent_gpt4.1_xxx.txt                  # Plain-text output for disclosure tests (GPT-4.1)
│     │     └── GPT4.1-automated.py                             # Script used to run GPT-4.1 disclosure prompts
│     ├── GPT5/                                                 # Results generated using GPT-5
│     │     ├── automated_agent_disclosure_gpt5_xxx.json        # Raw JSON output for disclosure evaluation (GPT-5)
│     │     ├── automated_agent_disclosure_gpt5_xxx.txt         # Plain-text output for disclosure tests (GPT-5)
│     │     └── GPT5-automated.py                               # Script used to run GPT-5 disclosure prompts
│     └── automated_agent_disclosure_prompts.txt                # Prompt set for agent disclosure evaluation
│
│── Qwen-score/                                                 # Blockwise scoring results using Qwen evaluator
│     ├── automated_eval_scores.csv                             # CSV of automated evaluation scores
│     └── system_identity_qwen_scores_*.csv                     # System identity scoring results from Qwen
│
│── System identity, capabilities, and limitations.../          # Evaluation of model identity & capability statements
│     ├── GPT4.1/                                               # Results generated using GPT-4.1
│     │     ├── system_identity_gpt4.1_xxx.json                 # Raw JSON system-identity outputs (GPT-4.1)
│     │     ├── system_identity_gpt4.1_xxx.txt                  # Plain-text system-identity outputs (GPT-4.1)
│     │     └── GPT4.1-system.py                                # Script to run GPT-4.1 system identity prompts
│     ├── GPT5/                                                 # Results generated using GPT-5
│     │     ├── system_identity_eval_gpt5_xxx.json              # Raw JSON system-identity outputs (GPT-5)
│     │     ├── system_identity_eval_gpt5_xxx.txt               # Plain-text system-identity outputs (GPT-5)
│     │     └── GPT5-system.py                                  # Script to run GPT-5 system identity prompts
│     └── system_identity_prompts.txt                           # Prompt set for system identity evaluation
│
│── GPT4_vs_GPT5_summary.txt                                    # Summary comparing GPT-4.1 vs GPT-5 behaviors
│── README.md                                                   # Project documentation
```

---

## 1. Automated Agent Disclosure

This module contains the evaluation of:

- How GPT‑4.1 and GPT‑5 disclose system identity to users  
- Full JSON and TXT outputs  
- Automated evaluation scripts  

Each run is preserved with the original model output.

---

## 2. System Identity, Capabilities, and Limitations

This module evaluates the model’s ability to:

- Describe its identity transparently  
- Explain its capabilities and limitations  
- Communicate uncertainty  
- Adapt explanations to user context  

Includes all raw model outputs and scripts.

---

## 3. Qwen‑score Automated Evaluation

This folder contains:

- Qwen‑based evaluation results (CSV)  
- System identity scoring  
- Automated comparison metrics  

The CSV files can be used for further statistical analysis or visualization.

---

## 4. GPT‑4.1 vs GPT‑5 Summary

`GPT4_vs_GPT5_summary.txt` includes:

- Comparative analysis  
- Strengths and weaknesses  
- Transparency behavior differences  
- Average scores across evaluation dimensions  

---

## 5. Running the Code

All scripts are compatible with **Python 3.9+**.

Example:

```bash
cd "Automated agent disclosure in user-facing interactions/GPT5"
python GPT5-automated.py
```

Scripts are self‑contained and require only an API key (all keys removed for safety).

---

## 6. Author

**Puchen Liu**  
Boston University — DS680  
GitHub: https://github.com/puchenliu
