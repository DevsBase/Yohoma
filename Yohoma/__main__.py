from Yohoma import *
import asyncio
from pyrogram import *

async def start():
  await app.start()
  await idle()

if __name__ == "__main__":
  asyncio..get_event_loop().run_until_complete(start())
