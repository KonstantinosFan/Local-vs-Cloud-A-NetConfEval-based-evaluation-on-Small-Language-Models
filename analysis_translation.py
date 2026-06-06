import pandas as pd
import matplotlib.pyplot as plt
import glob

models = {
    'llama3-8b': ('Llama-3 8B', 'blue', 'o', '-'),
    'mistral-7b': ('Mistral 7B', 'orange', 's', '--'),
    'gpt-3.5-turbo': ('GPT-3.5-Turbo', 'green', '^', '-.')
}

plt.figure(figsize=(8, 5))

for model_key, (model_label, color, marker, linestyle) in models.items():
    files = glob.glob(f'/Users/konstantinosf/conext24-NetConfEval/results_spec_translation/result-{model_key}-reachability-*.csv')
    if files:
        latest = max(files)
        df = pd.read_csv(latest)
        avg = df.groupby('batch_size')['accuracy'].mean()
        plt.plot(avg.index, avg.values, 
                marker=marker, 
                label=model_label, 
                color=color,
                linestyle=linestyle,
                linewidth=1.5,
                markersize=6)

plt.xscale('log')
plt.xticks([1, 2, 5, 10, 20, 25, 50, 100], 
           ['1', '2', '5', '10', '20', '25', '50', '100'])
plt.xlabel('Batch Size')
plt.ylabel('Accuracy')
plt.title('Formal Specification Translation - 1 Policy (Reachability)') 
plt.legend(loc='upper right')
plt.grid(True, which='both', alpha=0.3)
plt.ylim(-0.05, 1.05)
plt.savefig('translation_reachability.pdf', bbox_inches='tight')
plt.show()
