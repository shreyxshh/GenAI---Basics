import os
from dotenv import load_dotenv
from mistralai.client import Mistral

load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))

response = client.chat.complete(
    model="open-mistral-nemo",
    messages=[{"role": "user", "content": "What is the capital of India?"}],
)
print(response.choices[0].message.content)


# Models that work on our plan:
# open-mistral-nemo
# ministral-3b-latest