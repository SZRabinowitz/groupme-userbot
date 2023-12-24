from gmbotmodules import logusage, re, sendMessage
import json, random

only_text = True

def checkMessage(message):
    if message['text'] and re.search(r'^/egg', message['text'], re.IGNORECASE):
        logusage()
        with open('res/eggs.json', 'r') as file:
            eggs = json.load(file)['paths']

        randomegg = random.choice(eggs)
        
        sendMessage(message=message, text='egg', images=randomegg)

        return True
    else:
        return False