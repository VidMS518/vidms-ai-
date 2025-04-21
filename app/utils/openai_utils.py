import streamlit as st

USE_MOCK = True  # Change this to False when you're ready to use the real API

def generate_metadata(idea):
    if USE_MOCK:
        return {
            "title": f"🔥 Must Watch: {idea[:40]}",
            "description": f"This is a mock description for your video idea: {idea}.",
            "keywords": ["mock", "testing", "YouTube", "title", "description"]
        }
    else:
        import openai
        openai.api_key = st.secrets["openai"]["OPENAI_API_KEY"]
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant..."},
                {"role": "user", "content": idea},
            ]
        )
        content = response.choices[0].message.content
        # Parse or return based on your formatting
        return eval(content)

