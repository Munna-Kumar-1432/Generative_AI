
from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model="mistral-small-latest", temperature=0.7,max_tokens=20)

response = model.invoke("Write a poem about the beauty of nature.")

print("================================")
print(response.content)
print("================================")