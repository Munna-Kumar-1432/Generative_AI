from dotenv import load_dotenv
load_dotenv()
from langchain.chat_models import init_chat_model
model = init_chat_model("google_genai:gemini-2.5-flash-lite")

response = model.invoke("What is the capital of India?")

print("================================")
print(response.content)
print("================================")





from langchain_google_genai import ChatGoogleGenerativeAI

model1 = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")


response1 = model1.invoke("What is Machine Learning?")

print("================================")
print(response1.content)
print("================================")