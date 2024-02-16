from gmbotmodules import logusage, sendMessage, random
import json


only_messages_with_text = True
moduleName = 'meme'
helpString = 'the bot will send a meme when you send /meme. Most of the memes are for programmers.'

def checkMessage(message):
    if message['text'].strip().casefold() == '/meme'.strip().casefold():
        logusage()
        meme = random.choice(memeArray)
        sendMessage(message=message, text=meme['text'], images=[meme['image']], replyto=message)
        return True
    else:
        return False
    
with open('res/memeArray.json', 'r', encoding='utf-8') as file:
    memeArray = json.load(file)