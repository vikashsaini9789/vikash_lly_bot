import asyncio 
import pyttsx3
import os 
from gtts import gTTS 
from .. import bot 
from telethon import TelegramClient 
from telethon import events



@bot.on(events.NewMessage(pattern='/speak')) 

async def handle_text_to_speech(event):
    
    text = event.raw_text.replace('/txtsp ', '')

    
    tts = gTTS(text=text, lang='en')
    audio_file = 'output.mp3'
    tts.save(audio_file)


    
    await event.reply(file=audio_file)

    # Cleanup the temporary audio file
    os.remove(audio_file) 







