# from dotenv import load_dotenv
# load_dotenv()

# from langchain.chat_models import init_chat_model

# model = init_chat_model(
#     "microsoft/Phi-3-mini-4k-instruct",
#     model_provider="huggingface",
#     temperature=0.7,
# )

# response = model.invoke("Happy Birthday wishes for my friend?")

# print("================================")
# print(response.content)
# print("================================")


from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-4B-Instruct",
    temperature=0.7,
    max_new_tokens=512,
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("What is the capital of India?")
print(response.content)