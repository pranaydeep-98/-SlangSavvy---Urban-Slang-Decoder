import streamlit as st
from backend import decode_slang  # ✅ Import function from backend.py

# ✅ Streamlit UI
st.title("🗣 SlangSavvy - Urban Slang Decoder")
st.write("Enter slang words or phrases to decode their meanings.")

# ✅ User Input Field
slang_input = st.text_input("Enter a slang phrase:", "")

# ✅ Call Backend When Button is Clicked
if st.button("Decode"):
    if slang_input.strip():
        decoded_text = decode_slang(slang_input)  # Call API function from backend
        st.success(f" *Meaning:* {decoded_text}")  # ✅ Show result in UI
    else:
        st.warning("Please enter a slang phrase.")