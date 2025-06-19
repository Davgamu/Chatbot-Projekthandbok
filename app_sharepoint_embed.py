
import streamlit as st
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.chains import RetrievalQA
from pypdf import PdfReader
import os

# Fast API-nyckel (lägg in som hemlighet vid deploy)
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="Projekthandbokens Chatbot", layout="wide")
st.title("💬 Projekthandbokens RAG-Chatbot")
st.markdown("Välkommen! Du kan ställa frågor om innehållet i projekthandboken (PDF).")

# Initiera session
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# PDF-uppladdning
pdf_file = st.file_uploader("📄 Ladda upp projekthandboken (PDF)", type="pdf")
if pdf_file:
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = splitter.split_text(text)

    embeddings = OpenAIEmbeddings()
    db = FAISS.from_texts(texts, embedding=embeddings)

    system_prompt = (
        "Du är en hjälpsam assistent för Göteborg Energis projekthandbok. "
        "Du får inte ange, gissa eller föreslå personlig information om någon person. "
        "Om frågan gäller individer, svara istället: 'Jag kan inte ge personlig information.'"
    )
    prompt = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(system_prompt),
        HumanMessagePromptTemplate.from_template("Kontekst:\n{context}\n\nFråga: {question}")
    ])

    retriever = db.as_retriever()
    llm = ChatOpenAI(model_name="gpt-3.5-turbo")
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt},
        input_key="question"
    )

    fråga = st.chat_input("❓ Ställ din fråga här")
    if fråga:
        st.session_state.chat_history.append(("user", fråga))
        svar = qa.invoke({"question": fråga})
        st.session_state.chat_history.append(("ai", svar))

    for roll, meddelande in st.session_state.chat_history:
        if roll == "user":
            with st.chat_message("👤 Du"):
                st.markdown(meddelande)
        else:
            with st.chat_message("🤖 Assistent"):
                st.markdown(meddelande)
