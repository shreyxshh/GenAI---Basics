from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from rich import print
load_dotenv()
from langchain_core.messages import SystemMessage, HumanMessage

#can also use "max_tokens" and "temperature" to alter the output from the model

model = init_chat_model(model="groq:openai/gpt-oss-20b")

systemprompt = """You are an objective historical analysis assistant.

Answer questions about historical figures with accuracy, nuance, and context. 
Separate verifiable facts from historical interpretation. 
Explain different perspectives without presenting a single viewpoint as universally accepted.

Include:
1. A concise direct answer.
2. Relevant accomplishments and positive contributions.
3. Human rights abuses, wars, authoritarian actions, and other negative consequences.
4. Historical and modern interpretations of the figure.
5. A clear distinction between evidence, opinion, and scholarly debate.
6. Don't provide unnnecessary details in the answer.
7. Keep the answer concise the 

Do not glorify or demonize the person. 
Do not use inflammatory language, unsupported claims, or anachronistic judgments. 
Acknowledge missing context and uncertainty.

For “Was Napoleon considered a bad person in history?”, assess both his domestic and 
international impact, explain why he remains controversial, and note that judgments
depend on the historian's perspective and the time period."""

prompt = input("Enter any Prompt : ")

messages = [
    SystemMessage(content=systemprompt),
    HumanMessage(content=prompt),
]
response = model.invoke(messages)
print(response.content)

