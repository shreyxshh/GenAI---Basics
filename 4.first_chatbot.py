from dotenv import load_dotenv
load_dotenv()
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain.chat_models import init_chat_model

model = init_chat_model("groq:openai/gpt-oss-20b")
history = [SystemMessage(content="you are a funny chatbot, you have to answer in fun way because use iq is low")]

#this keeps the model active
while True:
    prompt = input("human (enter exit to leave) : ")
    history.append(HumanMessage(content=prompt))
    if prompt == "exit":
        break

    res = model.invoke(history)
    history.append(AIMessage(content=res.content))
    print(f"ai : {res.content}")

print("-" * 60)
print("The history stored till now : ")
print(history)