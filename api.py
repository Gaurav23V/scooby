import os
from openai import OpenAI

client = OpenAI(
    base_url=os.environ.get("ENDPOINT"),
    api_key=os.environ.get("GITHUB_TOKEN"),
)

SYSTEM_INSTRUCTIONS = """You are a terminal-based AI assistant named Scooby powered by GPT-4O.
Keep your responses conversational and friendly. Do not use markdown formatting in your
responses unless specifically asked. Provide clear, readable responses that work well
in a terminal environment."""


def get_streaming_response(message, conversation_history):
    messages = [{"role": "system", "content": SYSTEM_INSTRUCTIONS}]

    for role, content in conversation_history:
        messages.append({"role": role, "content": content})

    messages.append({"role": "user", "content": message})

    return client.chat.completions.create(
        messages=messages,
        model="gpt-4o",
        stream=True
    )
