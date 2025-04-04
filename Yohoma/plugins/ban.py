from pyrogram import *
from Yohoma import *

@app.on_message(filters.command("ban"))
async def ban_func(_, m):
  if not m.reply_to_message:
    return await m.reply("You need reply to a message to ban them.")
  elif not await CheckPrivileges(m.chat.id, app.me.id, "can_restrict_members"):
    return await m.reply("I'm missing rights of 'can_restrict_members'") if await CheckPrivileges(m.chat.id, app.me.id, checkAdmin=True) else await m.reply("I cannot.")
  elif not await CheckPrivileges(m.chat.id, m.from_user.id, "can_restrict_members") and m.from_user.id not in DEVS:
    return await m.reply("You cannot.")
  if not m.reply_to_message:
    try: target = await app.get_users(" ".join(m.command[1:]))
    except: return await m.reply("User not found.") 
  else: target = m.reply_to_message.from_user
  if await CheckPrivileges(m.chat.id, target, checkAdmin=True):
    return await m.reply("Cannot ban a admin/creator.")
  try: r = await ban_chat_member(m.chat.id, target)
  except Exception: return await m.reply(f"Failed: {Exception}")
  if isinstance(r, types.Message) or r is True:
    await m.reply("Banned!")
  else:
    await m.reply(f"Failed: {r}")
    
MOD_NAME = "Ban"
MOD_HELP = "/ban <reply / userid> - To ban a them."