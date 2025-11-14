import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
#from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv(override=True)


#-----------------------------------------------------
# Streamlit page setup


st.set_page_config(
    page_title="Achivements Finder",
    page_icon="👋",
)

st.title("Find key achivments using langchain + ollama")

st.write(" Enter Person name to get the key achivements in 4 bulluleted points")

#--------------------------------------------------------------------

# User input section

person = st.text_input("Enter Person Name")

#  Button to trigger the LLM

if st.button("Get Achivements "):
    if not person:
        st.warning("Please enter a person name.")
    else:
        with st.spinner("Finding Achivements..."):
            # Call the function to get the LLM response
            prompt = ChatPromptTemplate.from_messages(
                [
                    ("system", "You are an expert in finding achivements of a person"),
                    ("user", "Tell me the key achivements of {person} in 4 bulleted points, If you don;t know the answer please say I don't know/ I don't have any information"),
                ]
            )

            #llm = ChatOllama(model="llama3.2:latest")
            llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.0)
            chain = prompt | llm

            response = chain.invoke({"person": person})

            st.write(response.content)





