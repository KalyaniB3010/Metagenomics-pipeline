import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load t-test results
df = pd.read_csv("/content/t-test.csv")

# Filter for significant species (p < 0.05)
significant = df[df["p_value"] < 0.05]

# Sort by p-value (optional)
significant = significant.sort_values("p_value")

# Select top 20 most significant species (optional - can adjust)
top_species = significant.head(20)

# Set species as index
heatmap_data = top_species.set_index("species")[["log2FC"]]

# Plot heatmap
plt.figure(figsize=(8, max(6, len(heatmap_data)*0.5)))  # auto-adjust height
sns.set(style="whitegrid")

ax = sns.heatmap(heatmap_data, annot=True, cmap="coolwarm", center=0, cbar_kws={'label': 'Log2 Fold Change'})

# Aesthetic tweaks
plt.title("Differentially Abundant Species (p < 0.05)", fontsize=14)
plt.xlabel("Group Comparison")
plt.ylabel("Species")
plt.xticks(rotation=45)
plt.tight_layout()

# Save or show plot
plt.savefig("differential_species_heatmap.png", dpi=300)
plt.show()
