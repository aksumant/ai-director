# script_writer.py
from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_script(idea):
    prompt = f"""
    Create a fast-paced animated challenge video script.
    Rules:
    - Strong hook in first 5 seconds
    - New twist every 10 seconds
    - Clear winner at the end
    Idea: {idea}
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content