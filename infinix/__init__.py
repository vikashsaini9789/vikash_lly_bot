from telethon import TelegramClient
import logging 
import time 

openai_key = "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"

api_id = "1125689"
api_hash = "4772d1792ed194020a8fb06a91ffb8fa"
bot_token = "5816858652:AAHbkUFA_DFDb6fLkalEIDEaFhGOR7DHvXM"

bot = TelegramClient ("vikash_lly_bot" ,api_id, api_hash).start(bot_token = bot_token) 