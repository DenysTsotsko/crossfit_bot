import os

from groq import AsyncGroq
from config_reader import config

from utils.text import llm_behaviour

client = AsyncGroq(
    api_key=config.GROQ_API_KEY.get_secret_value(),
)

async def generating_promt(request: list):
    string_bot = "\n".join(request)
    chat_completion = await client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": llm_behaviour,
            }, 
            {
                "role": "user", 
                "content": string_bot,
            }
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content