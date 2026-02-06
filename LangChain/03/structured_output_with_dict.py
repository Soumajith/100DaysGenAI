from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from typing import TypedDict ,Annotated
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    temperature=0.3,
    max_new_tokens=10000
)

model = ChatHuggingFace(llm=llm)

class Review(TypedDict):
    summary : Annotated[str, "Brief description for beginner"]
    sentiment : Annotated[str, "Return sentiment like positive, negative or neutral"]

# not supported by HuggingFace and Gemini
structured_model = model.with_structured_output(Review) 

response = structured_model.invoke("""I had a really good experience overall. The setup was simple, and everything worked as expected. A few things could be improved—mainly the speed and some minor UI details—but nothing that breaks the experience. Customer support was responsive, which was a big plus. I’d definitely recommend it to others and would use it again.""")

print(response)