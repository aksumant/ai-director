import os
from openai import OpenAI

def generate_script(idea):
    # This securely reads the key we saved in Render's Environment Variables
    api_key = os.getenv("OPENAI_API_KEY")
    
    # Initialize the correct, modern OpenAI client
    client = OpenAI(api_key=api_key)
    
    # Generate the script using the optimized gpt-4o-mini model
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert AI Video Director. Write viral, engaging video scripts."},
            {"role": "user", "content": f"Create a complete viral script for this idea: {idea}"}
        ]
    )
    
    return response.choices[0].message.content
