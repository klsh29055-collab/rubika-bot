import requests
import time
import random

TOKEN = "توکن_ربات_خودت"

URL = f"https://botapi.rubika.ir/v3/{TOKEN}/"

offset = 0

def send(chat_id, text):
    requests.post(URL + "sendMessage", json={
        "chat_id": chat_id,
        "text": text
    })

while True:
    try:
        res = requests.post(URL + "getUpdates", json={
            "offset": offset
        }).json()

        for msg in res.get("data", {}).get("updates", []):
            offset = msg.get("update_id", offset) + 1

            chat_id = msg["message"]["chat_id"]
            text = msg["message"].get("text", "")

            if text == "/start":
                send(chat_id, "سلام 👋 ربات آماده است")

            elif text == "سنگ" or text == "کاغذ" or text == "قیچی":
                bot = random.choice(["سنگ", "کاغذ", "قیچی"])
                send(chat_id, f"انتخاب تو: {text}\nانتخاب من: {bot}")

        time.sleep(1)

    except Exception:
        time.sleep(3)
