from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def register_handlers(app):

    @app.on_message(filters.command("start"))
    async def start_cmd(client, message):

        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🤖 Create Clone",
                        callback_data="create_clone"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📂 My Clones",
                        callback_data="my_clones"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ℹ️ About",
                        callback_data="about"
                    ),
                    InlineKeyboardButton(
                        "❓ Help",
                        callback_data="help"
                    )
                ]
            ]
        )

        await message.reply_text(
            "👋 Welcome To Clone Manager Bot",
            reply_markup=buttons
        )
