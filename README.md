# Local-vs-Cloud-A-NetConfEval-based-evaluation-on-Small-Language-Models
Extending NetConfEval (Wang et al., CoNEXT 2024) to evaluate local SLMs on network configuration tasks.

This repository contains the modified benchmark scripts, analysis code, and raw results for the paper "Local vs Cloud: Evaluating Small Language Models on Network Configuration Tasks." It extends the NetConfEval benchmark (Wang et al., PACMNET CoNEXT 2024, https://github.com/RedHatResearch/conext24-NetConfEval) — which we gratefully acknowledge — by evaluating local Small Language Models (Llama-3 8B and Mistral 7B via Ollama) on the Formal Specification Translation and Conflict Detection tasks. All credit for the original benchmark design, dataset, and evaluation framework belongs to the NetConfEval authors.


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
