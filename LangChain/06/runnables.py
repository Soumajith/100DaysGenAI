# Runnables - Unit of Work 
# Follows common interface like invoke(), batch(), stream()
# Easy to connect runnables

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnablePassthrough, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal


load_dotenv()


llm1 = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model1 = ChatHuggingFace(llm=llm1)

llm2 = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.3-70B-Instruct"
)

model2 = ChatHuggingFace(llm=llm2)

prompt1 = PromptTemplate(
    template="Create a joke on {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Explain the joke that is {joke}",
    input_variables=['joke']
)

parser = StrOutputParser()


# Runnable Sequence
chain = RunnableSequence(prompt1, model1, parser, prompt2, model2, parser)
print(chain.invoke({'topic':"AI"}))

# Runnable Passthrough
joke_chain = RunnableSequence(prompt1, model1, parser)
parallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'explaination' : RunnableSequence(prompt2, model2, parser)
})

final_chain = RunnableSequence(joke_chain, parallel_chain)
print(final_chain.invoke({'topic':'AI'}))


# Runnable Lambda -> can convert any function to a runnable

def word_counter(text):
    return len(text.split())

runnableWordCounter = RunnableLambda(word_counter)

print(runnableWordCounter.invoke('Hi this is a text.'))

