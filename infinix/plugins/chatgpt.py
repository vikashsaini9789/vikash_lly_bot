from telethon import events
from .. import bot,openai_key
import asyncio
import openai 

openai_key = "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"

#openai.api_key = openai_key

@bot.on(events.NewMessage(incoming=True, pattern  ="(?i)/ask"))
async def chatgpt(event): 
  #if event.sender_id==int(818310676):
  await event.reply("Yess!! You are My Devloper you devloped me very well") 
  # else:
   #  await event.reply("You are user: Nice to meet you") 
  