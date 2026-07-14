from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "CloneManagerBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message()
async def all_messages(client, message):
    if message.text == "/start":
        await message.reply_text(
            "🤖 Welcome to Clone Manager Bot!\n\n"
            "Use the buttons below."
        )

print("Bot Started...")
app.run()
