from telethon import TelegramClient
import logging 
import time 



api_id = "1125689"
api_hash = "4772d1792ed194020a8fb06a91ffb8fa"
bot_token = "5816858652:AAHbkUFA_DFDb6fLkalEIDEaFhGOR7DHvXM"

bot = TelegramClient ("vikash_lly_bot" ,api_id, api_hash).start(bot_token = bot_token) 
