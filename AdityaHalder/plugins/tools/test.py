from ... import *
from datetime import datetime

@app.on_message(cdx("status"))
@sudo_users_only
async def get_call_stats(client, message):
    chat_id = message.chat.id
    calls = await call.calls
    chat_call = await calls.get(chat_id)
    print(chat_call)
    # await m.edit(f"**🤖 Pinged !\nLatency:** `{ms}` ms")



__NAME__ = "status"
__MENU__ = """
`.ping` - **Check call status
Of Your Userbot Server.**
"""
