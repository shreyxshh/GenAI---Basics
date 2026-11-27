from dotenv import load_dotenv
from rich import print
load_dotenv()
from langchain.chat_models import init_chat_model

model = init_chat_model("groq:openai/gpt-oss-20b")
state = input('Enter a state : ')

#0. using normal "python"
response = model.invoke(f'what is the capital of {state}')
print(response.content)

#1. using langchain's "PrompTemplate.from_template" 
from langchain_core.prompts import PromptTemplate
template = PromptTemplate.from_template("what is the capital of {state}")
prompt = template.invoke({"state" : state})
res = model.invoke(prompt)
print(res.content)

#2. using langchain's "CHatPromptTemplate.from_template"
from langchain_core.prompts import ChatPromptTemplate
template = ChatPromptTemplate.from_template("what is the capital of {state}")
prompt = template.invoke({"state": state})
res = model.invoke(prompt)
print(res.content)

#3. using langchain's "ChatPromptTemplate.from_message"
from langchain_core.prompts import ChatPromptTemplate
template = ChatPromptTemplate.from_messages([
    ("system","answer is one word"),
    ("human","what is the capital of {state}")
])
prompt = template.invoke({'state':state})
res = model.invoke(prompt)
print(res.content)