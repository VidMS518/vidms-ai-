import openai
import streamlit as st

openai.api_key = st.secrets["openai"]["OPENAI_API_KEY"]

def generate_metadata(idea):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that generates YouTube titles, descriptions, and keywords based on a content idea."
            },
            {
                "role": "user",
                "content": f"Generate a title, description, and keywords for this idea: {idea}"
            }
        ]
    )

    return response.choices[0].message.content
