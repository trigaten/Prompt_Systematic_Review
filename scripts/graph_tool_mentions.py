import pandas as pd
import matplotlib.pyplot as plt

"""Graph the model counts generated by scripts/count_tool_mentions.py"""

csv_file = "../data/model_citation_counts.csv"
df = pd.read_csv(csv_file)

# sort by alphabetical order
top_20 = df.sort_values(by="count", ascending=False)

plt.figure(figsize=(10, 6))
plt.bar(top_20["tool_name"], top_20["count"], color="blue")
plt.xlabel("Model Name")
plt.ylabel("Count")
plt.title("Counts of Model Mentions in Dataset")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.show()

"""Graph the dataset counts generated by scripts/count_tool_mentions.py"""

csv_file = "../data/dataset_citation_counts.csv"
df = pd.read_csv(csv_file)

# sort by alphabetical order
top_20 = df.sort_values(by="count", ascending=False)

plt.figure(figsize=(10, 6))
plt.bar(top_20["tool_name"], top_20["count"], color="blue")
plt.xlabel("Dataset Name")
plt.ylabel("Count")
plt.title("Counts of Dataset Mentions in Dataset")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.show()

"""Graph the framework counts generated by scripts/count_tool_mentions.py"""

csv_file = "../data/framework_citation_counts.csv"
df = pd.read_csv(csv_file)

# sort by alphabetical order
top_20 = df.sort_values(by="count", ascending=False)

plt.figure(figsize=(10, 6))
plt.bar(top_20["tool_name"], top_20["count"], color="blue")
plt.xlabel("Framework Name")
plt.ylabel("Count")
plt.title("Counts of Framework Mentions in Dataset")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.show()
