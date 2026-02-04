from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import load_prompt

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    temperature=0.1,
    max_new_tokens=10000
)

chatModel = ChatHuggingFace(llm=llm)

st.header("Research Tool")

# user_input = st.text_input("Enter your prompt")

paper_input = st.selectbox("Select Research Paper", 
                           ["Attention is all you need",
                            "BERT: Pre training of Deep Bidirectional Transformer",
                            "GPT-3 : Language Models are few shot learners",
                            "Diffusion Models beat on GANs on Image synthesis"])

style_input = st.selectbox("Select the style", ["Beginner-Friendly",
                                                "Technical",
                                                "Code-Oriented",
                                                "Mathematical"])

length_input = st.selectbox("Select the length",["Short",
                                                 "Mid",
                                                 "Long"])




template = load_prompt('template.json')

if st.button("Summarise"):
    
    chain = template | chatModel
    
    response = chain.invoke({
        'paper_input' : paper_input,
        'style_input' : style_input,
        'length_input' : length_input
    })
    
    st.write(response.content)

