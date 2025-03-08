import streamlit as st
import requests

st.title("CodeTap AI")

code = st.text_area("Enter your code:")
if st.button("Check Code"):
    response = requests.post("https://codetrapai.onrender.com/predict/", json={"code": code})
    result = response.json().get("result", "Error")
    st.success(f"Result: {result}")
