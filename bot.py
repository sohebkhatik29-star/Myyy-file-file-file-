from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from plugins.start import register_handlers

app = Client(
    "CloneManagerBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

register_handlers(app)

print("✅ Clone Manager Bot Started...")

app.run()
