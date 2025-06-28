import streamlit as st
import requests

st.title("El mejor extractor de texto by: Aleja")

uploaded_file = st.file_uploader("Sube una imagen", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    if st.button("Procesar imagen"):
        files = {"archivo": uploaded_file.getvalue()}
        response = requests.post("http://127.0.0.1:8000/ocr", files={"archivo": uploaded_file})

        if response.status_code == 200:
            resultado = response.json()
            texto_detectado = resultado.get("texto_detectado", [])
            st.subheader("Texto detectado:")
            for linea in texto_detectado:
                st.write(linea)
        else:
            st.error("Hubo un error al procesar la imagen.")
