import os
from openai import AsyncOpenAI

from config_reader import config


client = AsyncOpenAI(
    api_key=config.OPENAI_API.get_secret_value()
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