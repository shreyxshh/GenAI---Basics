from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()
#this automatically finds the api key in env file
model = ChatMistralAI(model="open-mistral-nemo")
response = model.invoke("What is the capital of India?")
print(response.content)