from dotenv import load_dotenv
load_dotenv() 

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    temperature=1,
    max_new_tokens=100,
)

chat_model = ChatHuggingFace(llm=llm)

response = chat_model.invoke("Write a 4 line poem about the sea.")
print(response.content)
