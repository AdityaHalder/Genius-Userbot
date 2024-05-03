from ... import *
from datetime import datetime

@app.on_message(cdx("status"))
@sudo_users_only
async def get_call_stats(client, message):
    calls = await call.calls()
    print(calls)
    # await m.edit(f"**🤖 Pinged !\nLatency:** `{ms}` ms")



__NAME__ = "status"
__MENU__ = """
`.ping` - **Check call status
Of Your Userbot Server.**
"""
