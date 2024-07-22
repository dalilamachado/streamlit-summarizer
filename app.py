import streamlit as st
from transformers import pipeline

# Configuração do pipeline de sumarização da Hugging Face
summarizer = pipeline("summarization")

# Função para resumir o texto
def summarize_text(text):
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return summary[0]['summary_text']

# Aplicativo Streamlit
st.title("Sumarizador de Artigos")

st.write("Insira o texto do artigo abaixo para obter um resumo conciso:")

# Caixa de entrada de texto para o usuário
article_text = st.text_area("Texto do Artigo", height=300)

# Botão para gerar o resumo
if st.button("Gerar Resumo"):
    if article_text:
        summary = summarize_text(article_text)
        st.subheader("Resumo:")
        st.write(summary)
    else:
        st.warning("Por favor, insira o texto do artigo.")
