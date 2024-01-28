from gmbotmodules import logusage, re, sendMessage
import json, random

moduleName = 'Egg'
helpString = '/egg'

def checkMessage(message):
    if re.search(r'^/egg', message['text'], re.IGNORECASE):
        logusage()
        with open('res/eggs.json', 'r') as file:
            eggs = json.load(file)['paths']

        randomegg = random.choice(eggs)
        
        sendMessage(message=message, text='egg', images=randomegg)

        return True
    else:
        return False