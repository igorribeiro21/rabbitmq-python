import requests
from dotenv import load_dotenv
import os

load_dotenv()

def send_telegram_message(message: str) -> None:
    token = os.getenv("BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }

    requests.post(url, data=payload)
