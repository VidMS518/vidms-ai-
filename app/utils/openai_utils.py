import streamlit as st
import random

USE_MOCK = True  # Change this to False when you're ready to use the real API

def generate_metadata(idea):
    if USE_MOCK:
         # Simulate a realistic YouTube AI assistant
    idea_snippets = idea.split()
    topic = " ".join(idea_snippets[:4]).title()

    titles = [
        f"{topic} Explained in 60 Seconds!",
        f"Why Everyone's Talking About {topic}",
        f"{topic}: What You Didn't Know!",
        f"{topic} – The Ultimate Breakdown",
        f"Don't Miss This! {topic} Secrets Revealed"
    ]

    descriptions = [
        f"In this video, we dive into the world of {topic}. Whether you're a beginner or expert, there's something new to learn!",
        f"Discover surprising facts and insights about {topic} that might just change the way you think.",
        f"This video breaks down {topic} in a fun and engaging way. Watch till the end for a bonus tip!",
        f"Get ready to explore {topic} like never before. Perfect for creators, learners, and curious minds!",
    ]

    keyword_sets = [
        ["youtube", "viral", "shorts", "trending", topic.lower()],
        ["ai content", "engagement", "growth", topic.lower()],
        ["how to", "educational", "entertainment", topic.lower()],
        ["tips", "secrets", "explained", topic.lower()],
    ]

    return {
        "title": random.choice(titles),
        "description": random.choice(descriptions),
        "keywords": random.choice(keyword_sets)
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

