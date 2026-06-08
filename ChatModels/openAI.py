from dotenv import load_dotenv

load_dotenv()

from langchain.chat_models import init_chat_model

# model = init_chat_model("gpt-4.1")

# response = model.invoke("What is the meaning of life?")

# print("================================")
# print(response)
# print("================================")

# response = model.invoke("What is Prime Number?")



# print("================================")
# print(response.content)
# print("================================")

# model = init_chat_model("gpt-5")

# response = model.invoke("What is C-Programming Language?")

# print("================================")
# print(response.content)
# print("================================")


from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-5.4")

response = model.invoke("What is the capital of India?")

print("================================")
print(response.content)
print("================================")