import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_metadata(idea):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates YouTube titles, descriptions, and keywords based on a content idea."},
            {"role": "user", "content": f"Generate a title, description, and keywords for this idea: {idea}"}
        ]
    )

    content = response.choices[0].message.content

    return content
