from pyrogram import *
from Yohoma import *

@app.on_message(filters.command("ban"))
async def ban_func(_, m):
  if not m.reply_to_message and len(m.command) < 2:
    return await m.reply("You need reply a user or give thier username to ban them.")
  elif not await CheckPrivileges(m.chat.id, app.me.id, "can_restrict_members"):
    return await m.reply("I'm missing rights of 'can_restrict_members'") if await CheckPrivileges(m.chat.id, app.me.id, checkAdmin=True) else await m.reply("I cannot.")
  elif not await CheckPrivileges(m.chat.id, m.from_user.id, "can_restrict_members") and m.from_user.id not in SUDOS:
    return await m.reply("You cannot.")
  if not m.reply_to_message:
    try: target = (await app.get_users(" ".join(m.command[1:]))).id
    except: return await m.reply("User not found.") 
  else: target = m.reply_to_message.from_user.id
  if await CheckPrivileges(m.chat.id, target):
    return await m.reply("Cannot ban a admin/creator.")
  try: r = await app.ban_chat_member(m.chat.id, target)
  except Exception as e:
    return await m.reply(f"Failed: {str(e)}")
  await m.reply("Banned!")

@app.on_message(filters.command("unban"))
async def unban_func(_, m):
  if not m.reply_to_message and len(m.command) < 2:
    return await m.reply("You need reply a user or give thier username to unban them.")
  elif not await CheckPrivileges(m.chat.id, app.me.id, "can_restrict_members"):
    return await m.reply("I'm missing rights of 'can_restrict_members'") if await CheckPrivileges(m.chat.id, app.me.id, checkAdmin=True) else await m.reply("I cannot.")
  elif not await CheckPrivileges(m.chat.id, m.from_user.id, "can_restrict_members") and m.from_user.id not in SUDOS:
    return await m.reply("You cannot.")
  if not m.reply_to_message:
    try: target = (await app.get_users(" ".join(m.command[1:]))).id
    except: return await m.reply("User not found.") 
  else: target = m.reply_to_message.from_user.id  
  if (await app.get_chat_member(m.chat.id, target)).status not in [enums.ChatMemberStatus.BANNED]:
    return await m.reply("User is not banned.")
  try: r = await app.unban_chat_member(m.chat.id, target)
  except Exception as e:
    return await m.reply(f"Failed: {str(e)}")
  await m.reply("Unbanned!")
  
MOD_NAME = "Ban"
MOD_HELP = "/ban <reply/userid> - To ban a them.\n/unban <reply/userid> - To unban them."