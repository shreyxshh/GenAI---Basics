from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

#it automatically identifies the api key in env
model = ChatGroq(model="openai/gpt-oss-20b")
response = model.invoke("What is the capital of India?")
print(response.content)