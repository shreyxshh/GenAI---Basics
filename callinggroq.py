from groq import Groq
from rich import print
from dotenv import load_dotenv
import os

#model api key 
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

#writing our query to ask from 
response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[{"role": "user",
               "content": "Who is the current PM of India?"}
            ],
)

#restructing the response from the model 
print(response.choices[0].message.content)

