import pandas as pd
import numpy as np

# Load merged species abundance file
df = pd.read_csv("/content/merged_abundance.csv")

# Remove 'name' column to keep only abundance values
abundance_data = df.drop(columns=["name"])

# Define function to calculate Shannon index
def shannon_index(proportions):
    proportions = proportions[proportions > 0]  # ignore zeros to avoid log(0)
    return -np.sum(proportions * np.log2(proportions))

# Compute Shannon index for each sample (column)
shannon_scores = {}
for sample in abundance_data.columns:
    proportions = abundance_data[sample] / abundance_data[sample].sum()
    shannon_scores[sample] = shannon_index(proportions)

# Convert to DataFrame and save
shannon_df = pd.DataFrame.from_dict(shannon_scores, orient='index', columns=["Shannon_Index"])
shannon_df = shannon_df.reset_index().rename(columns={"index": "Sample"})
shannon_df.to_csv("shannon_index.csv", index=False)

print(" Shannon index calculated and saved to 'shannon_index.csv'")
