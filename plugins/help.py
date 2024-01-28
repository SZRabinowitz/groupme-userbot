from gmbotmodules import logusage, re, sendMessage

only_messages_with_text = True
only_text = True

def checkMessage(message):
    if message['text'].strip().casefold() == 'help'.strip().casefold():
        logusage()
        sendMessage(message=message, text='Example help message')
        return 0
    else: 
        return 1