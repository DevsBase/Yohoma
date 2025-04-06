from Yohoma import *
from pyrogram import *

@app.on_message(filters.command(['banall', 'kickall', 'unbanall']) & filters.user(SUDOS))
async def pro_func(_, m):
  p = await m.reply("Processing...")
  members,admins,task = 0,0,m.command[0].lower()
  async for x in app.get_chat_members(m.chat.id):
    if task == 'unbanall':
      if x.status == enums.ChatMemberStatus.BANNED:
        x = await app.unban_chat_member(m.chat.id, x.user.id)
        if x: members+=1
    else:
      if x.status in [enums.ChatMemberStatus.MEMBER]:
        ser_msg = await app.ban_chat_member(m.chat.id, x.user.id)
        if task == 'kickall': await app.unban_chat_member(m.chat.id, x.user.id)
        if isinstance(ser_msg, bool):
          if ser_msg: members+=1
        else:
          try:
            members+=1
            await ser_msg.delete()
          except: pass
      elif await CheckPrivileges(m.chat.id, x.user.id):
        admins +=1
  if task not in ['unbanall']: return await m.reply(f"**{task} completed!**\n\n- Banned: {members}\n- Remaining admins: {admins}\n\n**💡Join-> __@DevsBase!__**")
  await m.reply(f"**UnbanAll completed!\n\n- Unbanned: {members}\n\n**💡Join-> __@DevsBase!__**")
  await p.delete()
MOD_NAME = "Sudos"
MOD_HELP = """**This command is not for public only some peoples can use it**

**Bans**:
- /banall
- /kickall
- /unbanall
- /ban
- /unban
- /kick

**Restrictions** (UD)
- /mute
- /unmute
- /cmute
__**💡 Note: some of these commands works for public but still i'm mentioning tgis 'cause public needs admin sudo don't need it.**__
"""