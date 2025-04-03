import logging 
from pyrogram import *
import os
from config import *

logging.basicConfig(
  format="[Yohoma] %(name)s - %(message)s",
  handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
  level=logging.INFO,
)

if len(TOKEN) > 100:
  app = Client("Yohoma", session_string=TOKEN, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="Yohoma/plugins"))
else: app = Client("Yohoma", bot_token=TOKEN, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="Yohoma/plugins"))
