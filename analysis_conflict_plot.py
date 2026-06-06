import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

models = ['Llama-3 8B', 'Mistral 7B', 'GPT-3.5-Turbo']
tpr = [97.9, 94.8, 88.7]
tnr = [43.1, 34.8, 4.2]
fpr = [56.9, 65.2, 95.8]

x = np.arange(len(models))
width = 0.25

fig, ax = plt.subplots(figsize=(8, 5))

bars1 = ax.bar(x - width, tpr, width, label='True Positive Rate', color='green', alpha=0.8)
bars2 = ax.bar(x, tnr, width, label='True Negative Rate', color='blue', alpha=0.8)
bars3 = ax.bar(x + width, fpr, width, label='False Positive Rate', color='red', alpha=0.8)

ax.set_xlabel('Model')
ax.set_ylabel('Rate (%)')
ax.set_title('Conflict Detection Performance')
ax.set_xticks(x)
ax.set_xticklabels(models)
ax.legend(loc='upper right')
ax.set_ylim(0, 110)
ax.grid(True, axis='y', alpha=0.3)

for bar in bars1:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
            f'{bar.get_height():.1f}%', ha='center', va='bottom', fontsize=8)
for bar in bars2:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
            f'{bar.get_height():.1f}%', ha='center', va='bottom', fontsize=8)
for bar in bars3:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
            f'{bar.get_height():.1f}%', ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.savefig('conflict_detection.pdf', bbox_inches='tight')
plt.show()
