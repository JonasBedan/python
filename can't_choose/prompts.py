system = """

You are an analytical decision assistant.

Your task is to help compare two options objectively.

You must:
- Create clear evaluation categories
- Use the user's preferences
- Be neutral and logical
- Avoid emotional language
- Output structured data only

"""

#generates the categories for user input
def generate_categories(options, user_preferences):
    prompt = """Based on the following user preferences and the items{options}, create 7 to 10 clear evaluation categories.

    Preferences:
    {user_preferences}

    Rules:
    - Categories must be short
    - Categories must be measurable
    - No explanations
    - Return as a JSON array of strings
    """
    return prompt

#fills the categories created before
def fill_categories(options, categories_json):
    prompt = """
    You are comparing multiple options.

    Options:
    {options}

    Categories:
    {categories_json}

    For each category, rate each option from 1 to 10. If you are unsure about any category, give both options the same score.
    Do not invent information.


    Rules:
    - Be objective
    - Use the same scale for all options
    - No explanations
    - Do not add extra text
    - Output valid JSON in this format:

    {
    "category_name": {
        "option_name_1": number,
        "option_name_2": number,
        "option_name_3": number
      }
    }

    """
    return prompt

def decision(scores_json):
    prompt = """Here are the final scores:

    {scores_json}

    Explain in 3 short sentences which option is better and why(choose only one).

    Rules:
    - Be concise
    - No emojis
    - No filler text
    """
    return prompt
