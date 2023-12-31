import os
import json
from prompt_systematic_review.get_papers.semantic_scholar_source import (
    SemanticScholarSource,
)
from prompt_systematic_review.utils.keywords import keywords_list
import pandas as pd
from tqdm import tqdm


def create_directory(directory_name):
    """Create a directory if it doesn't already exist."""
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)


def save_papers_to_json(papers, file_path):
    """Save a list of Paper objects to a JSON file."""
    papers_dict = [paper.to_dict() for paper in papers]
    with open(file_path, "w") as file:
        json.dump(papers_dict, file, indent=4)


def query_semantic_scholar(downloadName: str = None, verbose=False):
    sss = SemanticScholarSource()

    all_papers_df = pd.DataFrame()

    if verbose:
        iterator = tqdm(keywords_list, desc="Processing keywords")
    else:
        iterator = keywords_list

    for keyword in iterator:
        papers = sss.getPapers(300, [keyword])
        papers_data = [paper.to_dict() for paper in papers]
        papers_df = pd.DataFrame(papers_data)
        all_papers_df = pd.concat([all_papers_df, papers_df], ignore_index=True)

    if downloadName:
        all_papers_df.to_csv(downloadName, index=False)
        if verbose:
            print(f"Saved all papers to '{downloadName}'.")

    return all_papers_df
