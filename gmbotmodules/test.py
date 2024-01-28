from gmbotmodules import logusage, sendMessage

only_messages_with_text = True
moduleName = 'Test'
helpString = '/test checks if the bot is on'

def checkMessage(message):
    if message['text'] == '/test':
        logusage()
        # This shows two ways to send a message. You can either pass the full message (json) or pass a group_id. If you pass a message, the sendMessage will automatically extract the group_id.
        sendMessage(text='Test Received', message=message)
        #sendMessage(text='Test Received', group_id=message['group_id'])
        return True
    else: 
        return False