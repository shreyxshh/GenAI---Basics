from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import ChatPromptTemplate
from langchain.chat_models import init_chat_model
from rich import print


model = init_chat_model(model="groq:openai/gpt-oss-20b")

multi_template = ChatPromptTemplate.from_messages([
    ("system", "You are an expert {profession} with a {tone} tone. Answer strictly in 2 lines."),
    ("human", "Explain the concept of {concept} to a {audience_level} student.")
])

profession = input("Enter profession (e.g. Physicist / Chef / Doctor): ")
tone = input("Enter tone (e.g. funny / serious / sarcastic): ")
concept = input("Enter concept (e.g. Gravity / Photosynthesis): ")
audience_level = input("Enter audience level (e.g. 5-year-old / college): ")

prompt_val = multi_template.invoke({
    "profession": profession,
    "tone": tone,
    "concept": concept,
    "audience_level": audience_level
})
response = model.invoke(prompt_val)
print(response.content)