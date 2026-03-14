from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

llm1 = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)
llm2 = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.3-70B-Instruct"
)


model1 = ChatHuggingFace(llm=llm1)
model2 = ChatHuggingFace(llm=llm2)

parser = StrOutputParser()

class FeedBack(BaseModel):
    sentiment : Literal['positive', 'negative'] = Field(description="Give me the sentiment of the following text")


parser2 = PydanticOutputParser(pydantic_object=FeedBack)

prompt1 = PromptTemplate(
    template="Classify the sentiment of the follwoing feedback text into positive and negative \n {text} \n {format_instructions}",
    input_variables=['text'],
    partial_variables={'format_instructions' : parser2.get_format_instructions()}
)

classifer_chain = prompt1 | model1 | parser2

# for positive
prompt2 = PromptTemplate(
    template='Write an appropiate feedback to this positive feedback\n{text}',
    input_variables=['text']
)

# negative feedback
prompt3 = PromptTemplate(
    template='Write an appropiate feedback to this negative feedback\n{text}',
    input_variables=['text']
)

branch_chain = RunnableBranch(
    # (condition , chain) 
    (lambda x: x.sentiment == 'positive', prompt2 | model1 | parser),
    (lambda x: x.sentiment == 'negative', prompt3 | model2 | parser),
    RunnableLambda(lambda x:"could not find the sentiment")
)

chain = classifer_chain | branch_chain

print(chain.invoke({'text' : "This is a horrible phone"}))

chain.get_graph().print_ascii()