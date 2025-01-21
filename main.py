import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv(override=True)

llm = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

prompt = ChatPromptTemplate.from_messages([("system", "You are a translator that translates {input_lang} to {output_lang}. Translate the user sentence."),("human","{input}")])


def main():
    st.title("AI translator")
    
    input_lang = st.text_input("Input language")
    output_lang = st.text_input("Output language")
    input_text = st.text_input("Input Text")

    if st.button("Translate"):
        chain = prompt | llm

        resp = chain.invoke({"input_lang":input_lang, "output_lang":output_lang,"input":input_text })

        st.subheader("Translated Text")

        st.write(resp.content)


if __name__ == "__main__":
    main()