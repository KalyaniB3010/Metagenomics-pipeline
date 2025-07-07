import pandas as pd
from scipy.stats import ttest_ind
import numpy as np

# Load your merged abundance data
df = pd.read_csv("/content/merged_abundance.csv")

# Define the control and PD sample columns
control_cols = [
    "C_SRR370", "C_SRR371", "C_SRR372", "C_SRR373", "C_SRR374",
    "C_SRR377", "C_SRR378", "C_SRR380", "C_SRR381", "C_SRR382"
]

pd_cols = [
    "PD_SRR316", "PD_SRR317", "PD_SRR318", "PD_SRR319", "PD_SRR320",
    "PD_SRR325", "PD_SRR329", "PD_SRR333", "PD_SRR334", "PD_SRR335"
]

# Store results in a list
results = []

# Iterate through each species
for _, row in df.iterrows():
    control_vals = row[control_cols].astype(float)
    pd_vals = row[pd_cols].astype(float)

    # Compute means
    mean_control = np.mean(control_vals)
    mean_pd = np.mean(pd_vals)

    # Log2 Fold Change (avoid log(0) with small epsilon)
    log2fc = np.log2((mean_pd + 1e-6) / (mean_control + 1e-6))

    # Perform two-sample t-test
    t_stat, p_value = ttest_ind(pd_vals, control_vals, equal_var=False)

    # Append result
    results.append({
        "species": row["name"],
        "log2FC": log2fc,
        "t_statistic": t_stat,
        "p_value": p_value,
        "mean_PD": mean_pd,
        "mean_Control": mean_control
    })

# Save results to CSV
results_df = pd.DataFrame(results)
results_df.to_csv("t-test.csv", index=False)

print("T-test analysis complete. Results saved to 't-test.csv'")
