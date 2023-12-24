from gmbotmodules import logusage, sendMessage

only_text = True

def checkMessage(message):
    if message['text'].strip().casefold() == 'ping'.strip().casefold():
        logusage()
        sendMessage(message=message, text='pong')
        return True
    else:
        return False