import sys
import json
import os
from openai import OpenAI
from dataclasses import dataclass
from dotenv import load_dotenv, find_dotenv
from rich import print
import prompts

key = load_dotenv(find_dotenv())
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def ai_call(prompt, use_tools=False):
    response = client.responses.create(
        model = "gpt-5",
        input = prompt,
        tools = [{"type": "web_search"}] if use_tools else None   
    )

    text = response.output_text.strip()
    try:
        return json.loads(text)
    except:
        return text



print("---WELCOME TO CAN'T CHOOSE?---")
print("First tell us the amount of options you are choosing from")
options_count = int(input("amount of options: "))
options = []
preferences = []

#getting vals
for option in range(options_count):
    options.append(input(f"option {option+1}: "))

for option in options:
    preferences.append(input(f"Why do you prefer {option}: "))

categories_json = ai_call(prompts.generate_categories(options, preferences), True)
scores_json = ai_call(prompts.fill_categories(options, categories_json), True)
decision = ai_call(prompts.decision(scores_json),False)
print(decision)

