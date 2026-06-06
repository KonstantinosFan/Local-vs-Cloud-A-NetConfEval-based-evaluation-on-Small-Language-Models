import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob

models = {
    'llama3-8b': 'Llama-3 8B',
    'mistral-7b': 'Mistral 7B',
    'gpt-3.5-turbo': 'GPT-3.5-Turbo'
}

tasks = {
    'reachability': '1 Policy',
    'reachability_waypoint': '2 Policies',
    'loadbalancing_reachability_waypoint': '3 Policies'
}

data = {model_label: [] for model_label in models.values()}

for model_key, model_label in models.items():
    for pattern, task_label in tasks.items():
        files = glob.glob(f'/Users/konstantinosf/conext24-NetConfEval/results_spec_translation/result-{model_key}-{pattern}-*.csv')
        if files:
            latest = max(files)
            df = pd.read_csv(latest)
            model_errors = df['model_error'].notna().sum()
            error_rate = model_errors / len(df) * 100
            data[model_label].append(error_rate)

x = np.arange(len(tasks))
width = 0.25

fig, ax = plt.subplots(figsize=(8, 5))

colors = ['blue', 'orange', 'green']
for i, (model_label, error_rates) in enumerate(data.items()):
    bars = ax.bar(x + (i - 1) * width, error_rates, width,
                  label=model_label, color=colors[i], alpha=0.8)
    for bar in bars:
        if bar.get_height() > 0:
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                   f'{bar.get_height():.1f}%', ha='center', va='bottom', fontsize=8)

ax.set_xlabel('Task Complexity')
ax.set_ylabel('Model Error Rate (%)')
ax.set_title('Model Error Rate by Task Complexity')
ax.set_xticks(x)
ax.set_xticklabels(tasks.values())
ax.legend(loc='upper left')
ax.set_ylim(0, 55)
ax.grid(True, axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('error_analysis.pdf', bbox_inches='tight')
plt.show()
