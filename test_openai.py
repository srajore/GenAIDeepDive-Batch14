from openai import OpenAI
import os

#from dotenv import load_dotenv

#load_dotenv(override=True)

key = os.getenv("OPENAI_API_KEY")

print(key)

client = OpenAI()

response = client.responses.create(
    model="gpt-5-nano",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)