import streamlit as st
from backend import decode_slang 
st.title("🗣 SlangSavvy - Urban Slang Decoder")
st.write("Enter slang words or phrases to decode their meanings.")
slang_input = st.text_input("Enter a slang phrase:", "")
if st.button("Decode"):
    if slang_input.strip():
        decoded_text = decode_slang(slang_input)
        st.success(f" *Meaning:* {decoded_text}") 
    else:
        st.warning("Please enter a slang phrase.")