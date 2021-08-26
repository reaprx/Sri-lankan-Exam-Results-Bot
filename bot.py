from pyrogram import Client

app = Client(
    "my_bot",
    bot_token=config.BOT_TOKEN,
)

async def main():
    async with app:
        await app.send_message("me", "Hi!")


app.run()
