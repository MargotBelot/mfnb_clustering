import pandas as pd
import json

# Load TSV file
df = pd.read_csv("/Users/margot/Desktop/Théo/Clustering/cluster_0.9.json", sep="\t", dtype=str)

# Rename columns if needed
df.columns = ["label_ID", "label_v", "group_ID"]

# Convert to JSON
json_output = df.to_dict(orient="records")

# Save the output
with open("/Users/margot/Desktop/Théo/Clustering/clustering_fixed.json", "w", encoding="utf-8") as f:
    json.dump(json_output, f, indent=4, ensure_ascii=False)

print("Fixed JSON saved as clustering_fixed.json")
