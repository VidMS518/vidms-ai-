
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_metadata(idea: str) -> dict:
    prompt = f"Generate a YouTube title, description, and 5 keywords for this idea: '{idea}'"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a creative YouTube content assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    content = response['choices'][0]['message']['content']

    # Simple response parsing (can be improved with structured format)
    lines = content.split("\n")
    title = lines[0].replace("Title:", "").strip() if lines else ""
    description = lines[1].replace("Description:", "").strip() if len(lines) > 1 else ""
    keywords = [kw.strip() for kw in lines[-1].replace("Keywords:", "").split(",")] if "Keywords:" in lines[-1] else []

    return {
        "title": title,
        "description": description,
        "keywords": keywords
    }
