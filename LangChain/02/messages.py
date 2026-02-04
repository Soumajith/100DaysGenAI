from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    temperature=0.3,
    max_new_tokens=10000
)

model = ChatHuggingFace(llm=llm)

messages = [SystemMessage(content="This is a intelligent chat bot"),
            HumanMessage(content="Tell me about Human")    
        ]

response = model.invoke(messages)

messages.append(AIMessage(content=response.content))
