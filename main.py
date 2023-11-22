import os
import openai
import streamlit as st

# Impostazione temporanea per scopi di debug
os.environ["OPENAI_API_KEY"] = "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"

# Imposta la chiave API di OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Definizione della funzione process_file
def process_file(uploaded_file):
    if uploaded_file is not None:
        content = uploaded_file.getvalue().decode("utf-8")
        return content

def get_openai_chat_response(text, assistant_id):
    try:
        st.info("Elaborazione in corso...")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": text}]
        )
        st.success("Elaborazione completata!")
        return response.choices[0].message['content']
    except Exception as e:
        st.error(f"Si è verificato un errore: {str(e)}")
        return None

st.title("Carica e Ottieni Risposte dalla HireFast AI")

# Campo per scrivere una domanda
user_input = st.text_input("Scrivi una domanda")

# Caricamento del file
uploaded_file = st.file_uploader("O carica un documento", type=['txt'])

# Bottone per elaborare la richiesta
if st.button("Processa e Ottieni Risposta"):
    if user_input:
        openai_response = get_openai_chat_response(user_input, "asst_Yy83iZ6Qrqppk4bu7954P2sl")
        if openai_response:
            st.write(openai_response)
    elif uploaded_file is not None:
        file_content = process_file(uploaded_file)
        st.write("Contenuto del File:")
        st.text(file_content)

        st.write("Ottenere una risposta dall'assistente OpenAI:")
        openai_response = get_openai_chat_response(file_content, "asst_Yy83iZ6Qrqppk4bu7954P2sl")
        if openai_response:
            st.write(openai_response)
    else:
        st.error("Per favore inserisci una domanda o carica un file prima di procedere.")
