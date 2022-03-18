import streamlit as st
from runner import run_rotator

st.title("Welcome to the Point Rotator!")

uploaded_file = st.file_uploader("")
if uploaded_file is not None:
    output = run_rotator(uploaded_file)
    st.download_button("Download output file", output)