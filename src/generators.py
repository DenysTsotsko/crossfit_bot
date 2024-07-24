import os
from openai import AsyncOpenAI

from config import OPENAI_API_KEY


client = AsyncOpenAI(
    api_key=OPENAI_API_KEY,
)

async def generating_promt(request: str):
    chat_completion = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": request,
            }
        ],
        model="gpt-3.5-turbo",
    )
    return chat_completion.choices[0].message.content