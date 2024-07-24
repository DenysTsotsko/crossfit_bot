from os import getenv
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = getenv("BOT_TOKEN")
OPENAI_API_KEY = getenv("OPENAI_API_KEY")
