
import streamlit as st
import requests

st.title("Demo App")

prompt = st.text_input("Enter your prompt:")
if st.button("Generate Response"):
    if prompt:
        try:
            response = requests.post("http://localhost:8000/generate", json={"prompt": prompt})
            if response.status_code == 200:
                st.success(f"Response: {response.json()['response']}")
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"Error connecting to FastAPI server: {e}")
    else:
        st.warning("Please enter a prompt before generating a response.")
