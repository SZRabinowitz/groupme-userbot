from gmbotmodules import logusage, sendMessage

only_messages_with_text = True
moduleName = 'Ping'
helpString = '/ping'
command = '/ping'
case_sensitive = False

def checkMessage(message):
    if message['text'].strip().casefold() == '/ping'.strip().casefold():
        logusage()
        sendMessage(message=message, text='pong')
        return True
    else:
        return False