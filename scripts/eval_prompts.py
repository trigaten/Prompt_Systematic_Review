"""
Test a set of prompts against a dataset and return the results. Currently working for GSM-8k. You must add your openAI API key to the key variable below.
"""

from prompt_systematic_review.role_prompting import evaluate_prompts
import openai
from dotenv import load_dotenv
import os
from datetime import datetime
import json
from prompt_systematic_review.role_prompting import Prompt

load_dotenv(dotenv_path="./.env")  # load all entries from .env file
openai.api_key = os.getenv("OPENAI_API_KEY")  # load openai key
with open(
    "data/prompts.json", "r"
) as file:  # load prompts from prompts.json to make prompts more modular.
    prompts = json.load(file)

baseline_prompts = [prompts["baseline1"], prompts["baseline2"], prompts["baseline3"]]
zero_shot_cot_prompts = [
    prompts["Now, let's..."],
    prompts["plan-and-solve"],
    prompts["thread-of-thought"],
]

zero_shot_baseline = Prompt("0-Shot Vanilla", baseline_prompts[0], 1)
zero_shot_CoT = Prompt("0-Shot CoT", zero_shot_cot_prompts[0], 2)
few_shot_baseline = Prompt("Few-Shot Vanilla", baseline_prompts[1], 2, True)

prompts_to_test = [
    zero_shot_baseline,
    zero_shot_CoT,
    few_shot_baseline,
]

dataset = "mmlu"  # mmlu or gsm8k
config_name = None  # main if gs8k, None if mmlu
split = "test"
# model = "gpt-4-1106-preview"
model = "gpt-3.5-turbo"
examples = 3  # number of examples to test
start = 0  # start index for dataset
log_interval = 25  # log interval for creatings jsons of results by query
max_toks = 300
rereading = False  # if true, will "reread" the question to the LM at query time
return_json = False
SEED = 42
temp = 0.0

eval = evaluate_prompts(
    prompts_to_test,
    dataset,
    config_name,
    split,
    model,
    examples,
    start_index=start,
    log_interval=log_interval,
    max_tokens=max_toks,
    reread=rereading,
    json_mode=return_json,
    seed=SEED,
    temperature=temp,
)

# Getting current date and time in YYYY-MM-DD_HH-MM-SS format
current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# File path for the JSON file
file_path = f"data/benchmarking/eval_results_{current_datetime}.json"

# Writing the dictionary to a JSON file
with open(file_path, "w") as json_file:
    json.dump(eval, json_file)
