# Local-vs-Cloud-A-NetConfEval-based-evaluation-on-Small-Language-Models
Extending NetConfEval (Wang et al., CoNEXT 2024) to evaluate local SLMs on network configuration tasks.

This repository contains the modified benchmark scripts, analysis code, and raw results for the paper "Local vs Cloud: Evaluating Small Language Models on Network Configuration Tasks." It extends the NetConfEval benchmark (Wang et al., CoNEXT 2024, https://github.com/RedHatResearch/conext24-NetConfEval), which I gratefully acknowledge, by evaluating local Small Language Models (Llama-3 8B and Mistral 7B via Ollama) on the Formal Specification Translation and Conflict Detection tasks.

## About This Project

Network configuration is one of the most error-prone and time-consuming
tasks in network operations. Large Language Models (LLMs) have shown
promise in automating this process, but existing work, including
NetConfEval has exclusively evaluated closed-source, cloud-based
models such as GPT-4 and GPT-3.5-Turbo. These models require sending
potentially sensitive network configurations to external APIs, which
raises serious privacy and security concerns for operators managing
critical infrastructure.

This project was developed as part of the research project submitted for the graduate course CS-533 - Introduction to Research on Computer Networks within the Computer Science Department at the University of Crete which asks a simple but unanswered question: can a free, locally-run Small Language Model do the same job?

I reproduce two tasks from the NetConfEval benchmark — Formal #what exactly from these two tasks!??
Specification Translation and Conflict Detection — using Llama-3 8B 
and Mistral 7B served locally via Ollama on a standard MacBook Air M4 
with 16GB of RAM. No cloud infrastructure was used for local model 
inference. GPT-3.5-Turbo was run via API as a cloud baseline to 
validate our reproduction against the original paper's results.

The modified benchmark files are:
model_configs.py;
step1_formal_spec_conflict_detection.py;
utils.py;

My analysis scripts are:
analysis_conflict_plot.py;
analysis_errors.py;
analysis_loadbalancing.py;
analysis_translation.py;
analysis_waypoint;



## Key Findings

- For Formal Specification Translation, local models perform comparably 
  to GPT-3.5-Turbo at small batch sizes but degrade sharply beyond 
  batch size 10–20. At batch size 100, Mistral 7B reaches 0% accuracy 
  while GPT-3.5-Turbo retains 65.2%.

- Local models produce structurally malformed output on up to 41.6% 
  of complex queries — a reliability problem not observed with 
  GPT-3.5-Turbo. This exposed latent bugs in the original benchmark 
  scripts, which were fixed as part of this work.

- For Conflict Detection, local models unexpectedly outperform 
  GPT-3.5-Turbo. Llama-3 8B achieves a 97.9% true positive rate 
  compared to 88.7% for GPT-3.5-Turbo. GPT-3.5-Turbo flags 95.8% 
  of non-conflicting requirement pairs as conflicting — a near-total 
  false positive bias.

- Local models incur zero monetary cost. GPT-3.5-Turbo cost €5.68 
  for the full benchmark of 3,845 queries. Running the same benchmark 
  with GPT-4o would cost approximately €25–30, and with GPT-5.5 
  approximately €110–130.

## Conclusion

The viability of local SLMs for network configuration is task-dependent.
Local models are already competitive for conflict detection and can be 
deployed today by operators who cannot use external APIs. For complex 
multi-policy translation at large batch sizes, cloud models remain 
significantly better. Fine-tuning local models on domain-specific data 
is a promising direction for closing this gap.


## Attribution

This work is built on top of the NetConfEval benchmark:

> Changjie Wang, Mariano Scazzariello, Alireza Farshin, Simone Ferlin, 
> Dejan Kostić, and Marco Chiesa. 2024. NetConfEval: Can LLMs Facilitate 
> Network Configuration? Proc. ACM Netw. 2, CoNEXT2, Article 7 (2024). 
> https://doi.org/10.1145/3656296

Original repository: https://github.com/RedHatResearch/conext24-NetConfEval

All credit for the benchmark design, dataset, and evaluation framework 
belongs to the original authors. This repository contains only the 
modifications and analysis scripts described in the paper above.
