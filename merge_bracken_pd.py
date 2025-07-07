import pandas as pd

# Define file paths for each sample
files = {
    # Control samples
    "Control1": "/content/SRR370_bracken_species.txt",
    "Control2": "/content/SRR371_bracken_species.txt",
    "Control3": "/content/SRR372_bracken_species.txt",
    "Control4": "/content/SRR373_bracken_species.txt",
    "Control5": "/content/SRR374_bracken_species.txt",
    "Control6": "/content/SRR377_bracken_species.txt",
    "Control7": "/content/SRR378_bracken_species.txt",
    "Control8": "/content/SRR380_bracken_species.txt",
    "Control9": "/content/SRR381_bracken_species.txt",
    "Control10": "/content/SRR382_bracken_species.txt",

    # Parkinson's Disease (PD) samples
    "PD1": "/content/SRR316_bracken_species.txt",
    "PD2": "/content/SRR317_bracken_species.txt",
    "PD3": "/content/SRR318_bracken_species.txt",
    "PD4": "/content/SRR319_bracken_species.txt",
    "PD5": "/content/SRR320_bracken_species.txt",
    "PD6": "/content/SRR325_bracken_species.txt",
    "PD7": "/content/SRR329_bracken_species.txt",
    "PD8": "/content/SRR333_bracken_species.txt",
    "PD9": "/content/SRR334_bracken_species.txt",
    "PD10": "/content/SRR335_bracken_species.txt"
}

# Read and process each file
dfs = []
for sample, path in files.items():
    df = pd.read_csv(path, sep='\t', usecols=['name', 'fraction_total_reads'])
    df = df.rename(columns={'fraction_total_reads': sample})
    dfs.append(df)

# Merge all dataframes on 'name'
merged_df = dfs[0]
for df in dfs[1:]:
    merged_df = pd.merge(merged_df, df, on='name', how='outer')

# Fill NaNs with 0
merged_df.fillna(0, inplace=True)

# Save the merged output
merged_df.to_csv("merged_abundance.csv", index=False)

print("? Merging completed. Output saved as 'merged_abundance.csv'")
