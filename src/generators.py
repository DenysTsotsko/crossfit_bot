import os

from groq import AsyncGroq
from config_reader import config


client = AsyncGroq(
    api_key=config.GROQ_API_KEY.get_secret_value(),
)

async def generating_promt(request: str):
    chat_completion = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": request,
            }
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content