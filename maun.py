from pyrogram import Client

api_id = 5788656
api_hash = "f10bf7a46ec53542f255c03aba9ffb25"

with Client("my_account", api_id, api_hash) as app:
    app.send_message("me", "Greetings from **Pyrogram**!")
