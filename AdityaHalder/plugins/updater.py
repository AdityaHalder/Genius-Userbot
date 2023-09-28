import os
import sys
import asyncio

from .. import *
from git import *
from git.exc import *
from pyrogram import *
from pyrogram.types import *


UPSTREAM_REPO = "https://github.com/AdityaHalder/Genius-Userbot"
UPSTREAM_BRANCH = "aditya"


def gen_chlog(repo, diff):
    upstream_repo_url = Repo().remotes[0].config_reader.get("url").replace(".git", "")
    ac_br = repo.active_branch.name
    ch_log = ""
    tldr_log = ""
    ch = f"<b>updates for <a href={upstream_repo_url}/tree/{ac_br}>[{ac_br}]</a>:</b>"
    ch_tl = f"updates for {ac_br}:"
    d_form = "%d/%m/%y || %H:%M"
    for c in repo.iter_commits(diff):
        ch_log += (
            f"\n\n💬 <b>{c.count()}</b> 🗓 <b>[{c.committed_datetime.strftime(d_form)}]</b>\n<b>"
            f"<a href={upstream_repo_url.rstrip('/')}/commit/{c}>[{c.summary}]</a></b> 👨‍💻 <code>{c.author}</code>"
        )
        tldr_log += f"\n\n💬 {c.count()} 🗓 [{c.committed_datetime.strftime(d_form)}]\n[{c.summary}] 👨‍💻 {c.author}"
    if ch_log:
        return str(ch + ch_log), str(ch_tl + tldr_log)
    return ch_log, tldr_log


def updater():
    try:
        repo = Repo()
    except InvalidGitRepositoryError:
        repo = Repo.init()
        origin = repo.create_remote("upstream", UPSTREAM_REPO)
        origin.fetch()
        repo.create_head("UPSTREAM_BRANCH", origin.refs.UPSTREAM_BRANCH)
        repo.heads.UPSTREAM_BRANCH.set_tracking_branch(origin.refs.UPSTREAM_BRANCH)
        repo.heads.UPSTREAM_BRANCH.checkout(True)
    ac_br = repo.active_branch.name
    if "upstream" in repo.remotes:
        ups_rem = repo.remote("upstream")
    else:
        ups_rem = repo.create_remote("upstream", UPSTREAM_REPO)
    ups_rem.fetch(ac_br)
    changelog, tl_chnglog = gen_chlog(repo, f"HEAD..upstream/{ac_br}")
    return bool(changelog)


@app.on_message(commandx(["update"]) & SUPUSER)
async def update_userbot(client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    await message.edit("**🔄 Checking Updates ✨...**")
    update_avail = updater()
    if update_avail:
        await message.edit("**🥳 New Update Available\nFor Genius-Userbot❗**")
        asyncio.sleep(0.5)
        await message.edit("**🔃 Updating ...**")
        os.system("git pull -f && pip3 install -r Installer")
        await message.edit("**💕 Updated, Now Please\nWait Untill Restart. ✨**")
        os.system(f"kill -9 {os.getpid()} && python3 -m AdityaHalder")
        return
    else:
        await message.edit(f"**🥀 Genius Userbot Already\nUpdated To Latest 🔥 ...\n\n💕 For Any Query › Contact\nTo » @AdityaHalder ✨ ...**")

__NAME__ = "Update"
__MENU__ = f"""
**🥀 Use This Plugin To Update
Your Genius Userbot.**

**🇮🇳 Command :**
`.update` - Update Your Userbot
To Latest Version.
"""
