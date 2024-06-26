import pandas as pd
import os
import matplotlib.pyplot as plt
from prompt_systematic_review.config_data import DataFolderPath

"""Graph the model counts generated by scripts/count_models.py"""


def graph_models(inputFile="model_citation_counts.csv"):
    csv_file = os.path.join(DataFolderPath, inputFile)
    df = pd.read_csv(csv_file)

    # sort by alphabetical order
    top_20 = df.sort_values(by="count", ascending=False)

    plt.figure(figsize=(10, 6))
    plt.bar(top_20["model_name"], top_20["count"], color="#2E8991")
    plt.xlabel("Model Name", fontsize=20)
    plt.ylabel("Count", fontsize=20)
    plt.title("Counts of Model Mentions in Dataset", fontsize=30)

    plt.xticks(rotation=45, ha="right", fontsize=15)  # Adjust fontsize as needed
    plt.yticks(fontsize=15)  # Adjust fontsize as needed

    plt.tight_layout()

    output_dir = os.path.join(DataFolderPath, "experiments_output")
    os.makedirs(output_dir, exist_ok=True)  # Create directory if it doesn't exist

    # output_file_path = os.path.join(output_dir, "graph_models_output.png")
    output_file_path = os.path.join("graph_models_output.pdf")

    plt.savefig(output_file_path, format="pdf", bbox_inches="tight")


class Experiment:
    def run():
        graph_models()


if __name__ == "__main__":
    graph_models()
