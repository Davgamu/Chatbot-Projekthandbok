#
# 💬 Projekthandbokens RAG-Chatbot

Detta är en interaktiv Streamlit-baserad chatbot som använder Retrieval-Augmented Generation (RAG) för att besvara frågor om Göteborg Energis projekthandbok i PDF-format.

## 🎯 Syfte

Skapa en användarvänlig chatt som:
- Hjälper projektmedarbetare hitta rätt information i dokument
- Använder företagets egna dokument som kunskapskälla
- Följer integritetsprinciper: ingen personlig information ges

## 🚀 Funktioner

- ✅ Ladda upp valfri PDF (t.ex. "Projekthandbok")
- ✅ Ställ frågor i naturligt språk
- ✅ Få svar direkt från dokumentet, via GPT
- ✅ Chattgränssnitt med historik
- ✅ Sekretessfilter mot personuppgifter

## 🔐 Sekretesspolicy

> "Du får inte ange, gissa eller föreslå personlig information om någon person."

## 🛠 Teknikstack

- **Streamlit** – gränssnitt
- **LangChain** – RAG-pipeline
- **OpenAI** – GPT-svar
- **FAISS** – vektorsökning
- **PyPDF** – PDF-textutdrag

## 🧪 Exempel på frågor

- "Vad ansvarar projektledaren för?"
- "Vilka steg ingår i uppstart av ett projekt?"
- "Hur beskrivs projektavslut i dokumentet?"

## ⚙️ Så kör du appen i Streamlit Cloud

1. Skapa ett GitHub-repo och ladda upp `app.py` och `requirements.txt`
2. Gå till [streamlit.io/cloud](https://streamlit.io/cloud)
3. Koppla ditt GitHub-konto och välj ditt repo
4. Starta appen och dela länken med kollegor!

---

*Utvecklad som en intern prototyp för Göteborg Energi.*  
