import os
from openai import OpenAI

client = OpenAI(
    base_url=os.environ.get("ENDPOINT"),
    api_key=os.environ.get("GITHUB_TOKEN"),
)

def get_response(message):
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message},
        ],
        model="gpt-4o",
    )
    return response.choices[0].message.content