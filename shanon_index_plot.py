import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("/content/shannon_index.csv")

# Add a group column based on sample name
df["Group"] = df["Sample"].apply(lambda x: "Control" if x.startswith("C_") else "PD")

# Set plot style
sns.set(style="whitegrid")

# Create plot
plt.figure(figsize=(8, 6))
sns.boxplot(x="Group", y="Shannon_Index", data=df, palette="Set2")
sns.stripplot(x="Group", y="Shannon_Index", data=df, color="black", size=6, jitter=True)

# Titles and labels
plt.title("Shannon Diversity Index: Control vs Parkinson's Disease", fontsize=14)
plt.xlabel("Group", fontsize=12)
plt.ylabel("Shannon Index", fontsize=12)

# Save plot
plt.tight_layout()
plt.savefig("shannon_index_comparison.png", dpi=300)
plt.show()
