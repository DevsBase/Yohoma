from pyrogram import *
import logging

async def CheckPrivileges(chat, user, x=[], showMissing=False):
  from Yohoma import app
  x = x if isinstance(x, list) else [x]
  try: member = await app.get_chat_member(chat, user)
  except Exception:
    return logging.info(Exception)
  if member.status in [enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER] and hasattr(member, "privileges"):
    missing = [z for z in x if not getattr(member.privileges, z, False)]
    return (False, missing) if showMissing and missing else not missing
  return (False, x) if showMissing else False