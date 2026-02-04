from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate([
    ('system' , "This is a intelligent {domain} chatbot"),
    ('human' , "Hi, What is {topic}")
])

prompt = template.invoke({
    "domain" : "cricket",
    "topic" : "no ball"
})

print(prompt)