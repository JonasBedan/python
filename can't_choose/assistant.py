import sys
import json
import os
from openai import OpenAI
from dataclasses import dataclass
from dotenv import load_dotenv, find_dotenv
from rich import print
import prompts



key = load_dotenv(find_dotenv())
if not os.getenv("OPENAI_API_KEY"):
    print("Missing OPENAI_API_KEY")
    sys.exit()
    
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))



def ai_call(prompt, use_tools=False):

    response = client.responses.create(
        model="gpt-5",
        input=prompt,
        tools=[{"type": "web_search"}] if use_tools else None
    )

    text = response.output_text.strip()

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return text




print("---WELCOME TO CAN'T CHOOSE?---")
print("First tell us the amount of options you are choosing from")
options_count = int(input("amount of options: "))
options = []
preferences = []
categories = []
weighted_categories = {}


#getting vals
for option in range(options_count):
    options.append(input(f"option {option+1}: "))

for option in options:
    preferences.append(input(f"Why do you prefer {option}: "))

categories_json = ai_call(prompts.generate_categories(options, preferences), True)


print("these are the categories generated for your options")
for category in categories_json:
    while True:
        weight = input(f"How important is {category} (0-10):")
    
        if weight.isdigit() and 0 <= int(weight) <= 10:
            weighted_categories[category] = int(weight)
            break
        else:
            print("Enter number 0-10.")


scores_json = ai_call(prompts.fill_categories(options, weighted_categories), True)
decision = ai_call(prompts.decision(scores_json),False)

print(decision)

