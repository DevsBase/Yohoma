from pyrogram import *
from Yohoma import *

@app.on_message(filters.command("pin"))
async def pin_func(_, m):
  if not m.reply_to_message:
    return await m.reply("You need reply to a message to pin it.")
  elif not await CheckPrivileges(m.chat.id, app.me.id, "can_pin_messages"):
    return await m.reply("I dont have rights")
  elif not await CheckPrivileges(m.chat.id, m.from_user.id, "can_pin_messages") and m.from_user.id not in DEVS:
    return await m.reply("You cannot.")
  await (await m.reply_to_message.pin(both_sides=True)).delete()
  try: await m.delete()
  except: pass
    
MOD_NAME = "Pin"
MOD_HELP = "/pin <reply> - To pin a message."