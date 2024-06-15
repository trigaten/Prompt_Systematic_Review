# The Prompt Report Code Repository 
Generative Artificial Intelligence (GenAI) systems are being increasingly deployed across all parts of
industry and research settings. Developers and end users interact with these systems through the use of
prompting or prompt engineering. While prompting is a widespread and highly researched concept, there
exists conflicting terminology and a poor ontological understanding of what constitutes a prompt due to the
area’s nascency. This repository is the code for The Prompt Report, our research that establishes a structured 
understanding of prompts, by assembling a taxonomy of prompting techniques and analyzing their use. This code 
allows for the automated review of papers, the collection of data, and the running of experiments. Our dataset 
is available on [Hugging Face](https://huggingface.co/datasets/PromptSystematicReview/ThePromptReport) and our paper is 
available on [ArXiv.org](https://arxiv.org/pdf/2406.06608). Information is also available on our [website](https://trigaten.github.io/Prompt_Survey_Site/).

## Table of Contents
- [Prompt Engineering Survey](#prompt-engineering-survey)
  - [Install requirements](#install-requirements)
  - [Setting up API keys](#setting-up-api-keys)
  - [Setting up keys for running tests](#setting-up-keys-for-running-tests)
  - [Structure of the Repository](#structure-of-the-repository)
  - [Running the code](#running-the-code)
    - [TLDR;](#tldr)
  - [Notes](#notes)

## Install requirements

after cloning, run `pip install -r requirements.txt` from root

## Setting up API keys

Make a file at root called `.env`.

For OpenAI: https://platform.openai.com/docs/quickstart <br>
For Hugging Face: https://huggingface.co/docs/hub/security-tokens, also run `huggingface-cli login` <br>
For Sematic Scholar: https://www.semanticscholar.org/product/api#api-key  <br>

Use the reference `example.env` file to fill in your API keys/tokens. 
```
OPENAI_API_KEY=sk.-...
SEMANTIC_SCHOLAR_API_KEY=...
HF_TOKEN=...
```

## Setting up keys for running tests
Then to load the .env file, type: <br>
`pip install pytest-dotenv`

You can also choose to update the env file by doing: <br>
`py.test --envfile path/to/.env`

In the case that you have several .env files, create a new env_files in the pytest config folder and type:
```
env_files =
.env
.test.env
.deploy.env
```
## Structure of the Repository
The script `main.py` calls the necessary functions to download all the papers, deduplicate and filter them, and then run all the experiments. 

The core of the repository is in `src/prompt_systematic_review`. The `config_data.py` script contains configurations that are important for running experiments and saving time. You can see in `main.py` how some of these options are used. 

The source folder is divided into 4 main sections: 3 scripts (`automated_review.py`, `collect_papers.py`,`config_data.py`) that deal with collecting the data and running the automated review, the `utils` folder that contains utility functions that are used throughout the repository, the `get_papers` folder that contains the scripts to download the papers, and the `experiments` folder that contains the scripts to run the experiments. 

At the root, there is a `data` folder. It comes pre-loaded with some data that is used for the experiments, however the bulk of the dataset can either be generated by running `main.py` or by downloading the data from Hugging Face. It is in `data/experiments_output` that the results of the experiments are saved.

Notably, the keywords used in the automated review/scraping process are in `src/prompt_systematic_review/utils/keywords.py`. Anyone who wishes to run the automated review can adjust these keywords to their liking in that file. 

## Running the code

### TLDR;
```bash
git clone https://github.com/trigaten/Prompt_Systematic_Review.git && cd Prompt_Systematic_Review
pip install -r requirements.txt
# create a .env file with your API keys
nano .env
git lfs install
git clone https://huggingface.co/datasets/PromptSystematicReview/ThePromptReport
mv ThePromptReport/* data/
python main.py
```

Running `main.py` will download the papers, run the automated review, and run the experiments.
However, if you wish to save time and only run the experiments, you can download the data from [Hugging Face](https://huggingface.co/datasets/PromptSystematicReview/ThePromptReport) and move the papers folder and all the csv files in the dataset into the data folder (should look like `data/papers/*.pdf` and `data/master_papers.csv` etc). Adjust main.py accordingly. 

Every experiment script has a `run_experiment` function that is called in `main.py`. The `run_experiment` function is responsible for running the experiment and saving the results. However each script can be run individually by just running `python src/prompt_systematic_review/experiments/<experiment_name>.py` from root. 

There is one experiment, `graph_internal_references` that, because of weird issues with parallelism, is better run from root as an individual script. To avoid it causing issues with other experiments, it is run last as it is ordered at the bottom of the list in `experiments/__init__.py`.



## Notes

- Sometimes a paper title may appear differently on the arXiv API. For example, "Visual Attention-Prompted Prediction and Learning" (arXiv:2310.08420), according to arXiv API is titled "A visual encoding model based on deep neural networks and transfer learning"

