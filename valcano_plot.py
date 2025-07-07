import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load t-test result CSV
df = pd.read_csv("/content/t-test.csv")

# Add columns for volcano plot
df['neg_log10_pval'] = -np.log10(df['p_value'])
df['significant'] = 'Not Significant'
df.loc[(df['p_value'] < 0.05) & (df['log2FC'] > 1), 'significant'] = 'Up in PD'
df.loc[(df['p_value'] < 0.05) & (df['log2FC'] < -1), 'significant'] = 'Up in Control'

# Plot
plt.figure(figsize=(12, 8))
palette = {'Not Significant': 'lightgray', 'Up in PD': 'tomato', 'Up in Control': 'royalblue'}

sns.scatterplot(data=df, x='log2FC', y='neg_log10_pval', hue='significant', palette=palette,
                edgecolor='black', alpha=0.7, s=70)

# Threshold lines
plt.axhline(y=-np.log10(0.05), color='black', linestyle='--')
plt.axvline(x=1, color='black', linestyle='--')
plt.axvline(x=-1, color='black', linestyle='--')

plt.title("Volcano Plot: Differentially Abundant Species (PD vs Control)", fontsize=14)
plt.xlabel("Log2 Fold Change", fontsize=12)
plt.ylabel("-log10(p-value)", fontsize=12)
plt.legend(title="Significance", loc='upper right')
plt.tight_layout()
plt.savefig("volcano_plot.png", dpi=300)
plt.show()
