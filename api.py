import os
from openai import OpenAI

client = OpenAI(
    base_url=os.environ.get("ENDPOINT"),
    api_key=os.environ.get("GITHUB_TOKEN"),
)

def get_response(message, conversation_history):
    messages = [{"role": "system", "content": "You are a helpful assistant."}]

    # Add conversation history
    for role, content in conversation_history:
        messages.append({"role": role, "content": content})

    # Add current message
    messages.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        messages=messages,
        model="gpt-4o",
    )
    return response.choices[0].message.content