## This is a just a test client to test the LLM seperately, will be added to client.py after functionality has been tested

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get(""), # Excluded from commit
)

response = client.responses.create(
    model="gpt-5.5",
    instructions="You are an assistant, that gives clear and simple explanation",
    input="Hello, what is MCP?",
)

print(response.output_text)
