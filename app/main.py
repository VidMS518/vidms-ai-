
import streamlit as st
from utils.openai_utils import generate_metadata

st.set_page_config(page_title="VidMs AI Tool", layout="centered")

st.title("VidMs - AI Title, Description & Keyword Generator")

idea = st.text_area("Enter your video idea or topic:", height=150)

if st.button("Generate Metadata"):
    if idea.strip():
        with st.spinner("Generating..."):
            metadata = generate_metadata(idea)
            st.subheader("Title")
            st.write(metadata['title'])
            st.subheader("Description")
            st.write(metadata['description'])
            st.subheader("Keywords")
            st.write(", ".join(metadata['keywords']))
    else:
        st.warning("Please enter an idea.")
