import pandas as pd 
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
from adjustText import adjust_text  # install via: pip install adjustText

# Load abundance data
df = pd.read_csv('/content/merged_abundance (1).csv')  # update path if needed
df = df.set_index(df.columns[0])
df_transposed = df.T

# Select 4 PD and 4 Control samples
selected_samples = [
    'C_SRR370', 'C_SRR371', 'C_SRR372', 'C_SRR373',
    'PD_SRR316', 'PD_SRR317', 'PD_SRR318', 'PD_SRR319'
]
df_subset = df_transposed.loc[selected_samples]

# Remove outliers using Isolation Forest
iso = IsolationForest(contamination='auto', random_state=42)
outliers = iso.fit_predict(df_subset)
df_no_outliers = df_subset[outliers == 1]

# Standardize
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df_no_outliers)

# Perform PCA with 3 components
pca = PCA(n_components=3)
pca_result = pca.fit_transform(scaled_data)

# Store results in DataFrame
pca_df = pd.DataFrame(pca_result, columns=['PC1', 'PC2', 'PC3'], index=df_no_outliers.index)
pca_df['Group'] = ['Control' if x.startswith('C_') else 'PD' for x in pca_df.index]

# ---- Plot PC1 vs PC3 (excluding C_SRR370) ----
pca_df_pc1_pc3 = pca_df.drop('C_SRR370')  # Remove only from this plot

plt.figure(figsize=(10, 7))
for group, color in zip(['Control', 'PD'], ['royalblue', 'tomato']):
    subset = pca_df_pc1_pc3[pca_df_pc1_pc3['Group'] == group]
    plt.scatter(subset['PC1'], subset['PC3'], label=group, s=100, alpha=0.8, edgecolors='k')

# Add labels
texts = []
for i in range(pca_df_pc1_pc3.shape[0]):
    texts.append(plt.text(pca_df_pc1_pc3['PC1'][i], pca_df_pc1_pc3['PC3'][i], pca_df_pc1_pc3.index[i], fontsize=9))
adjust_text(texts, arrowprops=dict(arrowstyle='-', color='gray', lw=0.5))

# Label and save
plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}%)')
plt.ylabel(f'PC3 ({pca.explained_variance_ratio_[2]*100:.1f}%)')
plt.title('PCA: PC1 vs PC3 (C_SRR370 Removed)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('PCA3 vs 3 plot.png', dpi=300)
plt.show()
