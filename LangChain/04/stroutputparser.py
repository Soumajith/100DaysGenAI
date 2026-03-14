from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

# 1st prompt Report
template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=['topic']
)


# 2nd prompt Summary
template2 = PromptTemplate(
    template="Write a 5 lines summary on {topic}",
    input_variables=['topic']
)


# prompt1 = template1.invoke({'Topic' : 'Black Hole'})

# result1 = model.invoke(prompt1)

# prompt2 = template2.invoke({'Topic' : result1.content})

# result2 = model.invoke(prompt2)

# print(result2.content) 

parser = StrOutputParser()


chain = template1 | model |  parser | template2 | model | parser

result = chain.invoke({'topic' : 'Black Hole'})

print(result)