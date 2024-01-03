from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

print(os.environ["OPENAI_API_KEY"])

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[{"role": "user", "content": "Olá"}]
)

print(completion.choices[0].message.content)