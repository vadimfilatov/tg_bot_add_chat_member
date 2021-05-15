from pyrogram import Client, filters

app = Client("my_account")

GROUP_PLATFORM_ID = -563741886
# Команда type
@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    if msg.chat.type == 'group':
        print(msg.chat.id)
        my_platform_id = msg.from_user.id
        chat_members = app.get_chat_members(msg.chat.id, 0, 200, '', 'all')
        for member in chat_members:
            if member.user.id != my_platform_id:
                app.add_chat_members(GROUP_PLATFORM_ID, member.user.id)

app.run()