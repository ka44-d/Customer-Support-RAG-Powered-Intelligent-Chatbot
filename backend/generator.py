from groq import Groq
import os
from config import GROQ_API_KEY, LLM_MODEL

client = Groq(api_key=GROQ_API_KEY)

def build_prompt(context, query):

    return f"""Context:
{context}

Question: {query}

Answer:"""


def generate_answer(prompt, temp=0.7, max_tokens=500):

    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful customer support assistant. "
                    "Use only the provided context. "
                    "Be clear and polite. "
                    "Cite sources like [Doc 1]."
                ),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        temperature=temp,
        max_tokens=max_tokens,
    )

    return response.choices[0].message.content.strip()