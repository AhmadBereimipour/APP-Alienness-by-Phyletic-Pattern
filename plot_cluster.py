import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# read matrix
df = pd.read_csv("phyletic_2level.tsv", sep="\t")

# gene names
df = df.set_index("gene")

# remove summary column if exists
if "present_count" in df.columns:
    df = df.drop(columns=["present_count"])

# convert similarity -> presence
binary = (df > 0.5).astype(int)

# clustering heatmap
sns.clustermap(
    binary,
    cmap="viridis",
    metric="euclidean",
    method="average",
    figsize=(10,10)
)

plt.savefig("HGT_cluster_heatmap.png", dpi=300)
print("Saved: HGT_cluster_heatmap.png")
