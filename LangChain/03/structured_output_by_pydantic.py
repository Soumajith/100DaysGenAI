from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-pro-preview", temperature=0)
# not supported with HuggingFace

class Review(BaseModel):
    keythemes : list[str] = Field(description= "Write down all the key themes discussed")
    summary : str = Field(description="Brief summary about it")
    sentiment : str = Field(description="Good, bad or neutral")
    pros: Optional[list[str]] = Field(default=None , description="Any Pros points")
    cons : Optional[list[str]] = Field(default=None, description="Any cons points")



structured_model = model.with_structured_output(Review) 

response = structured_model.invoke("""I had a really good experience overall. The setup was simple, and everything worked as expected. A few things could be improved—mainly the speed and some minor UI details—but nothing that breaks the experience. Customer support was responsive, which was a big plus. I’d definitely recommend it to others and would use it again.""")

print(response.content)