from pyrogram import *

async def CheckPrivileges(chat, user, x=[]):
  from Yohoma import app
  x = x if isinstance(x, list) else [x]
  member = await app.get_chat_member(chat, user)
  if member.status in [enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER] and hasattr(member, "privileges"):
    return all(getattr(member.privileges, z, False) for z in list(x)) if x else True
  return False