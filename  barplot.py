import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the merged abundance file
df = pd.read_csv("/content/merged_abundance.csv")

# Separate columns into Control and PD
control_cols = [col for col in df.columns if col.startswith("C_")]
pd_cols = [col for col in df.columns if col.startswith("PD_")]

# Calculate mean abundance
df["Mean_Control"] = df[control_cols].mean(axis=1)
df["Mean_PD"] = df[pd_cols].mean(axis=1)

# Top 10 species in each group
top_control = df.nlargest(10, "Mean_Control")[["name", "Mean_Control"]].rename(columns={"Mean_Control": "Abundance"})
top_control["Group"] = "Control"

top_pd = df.nlargest(10, "Mean_PD")[["name", "Mean_PD"]].rename(columns={"Mean_PD": "Abundance"})
top_pd["Group"] = "PD"

# Combine both
top_species = pd.concat([top_control, top_pd])

# Plot
plt.figure(figsize=(10, 6))
sns.barplot(data=top_species, x="Abundance", y="name", hue="Group", dodge=True)
plt.title("Top 10 Species in Control vs PD")
plt.xlabel("Mean Relative Abundance")
plt.ylabel("Species")
plt.tight_layout()
plt.legend(title="Group")
plt.savefig("Top10 species.png", dpi=300)
plt.show()
