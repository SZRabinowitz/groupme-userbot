from gmbotmodules import logusage, sendMessage, get_message, re
import profanity_check

only_messages_with_text = True
moduleName = 'Profanity Filter'
helpString = 'Automatically Reply to messages with profanity'
command = ''
case_sensitive = False

def checkMessage(message):
    if profanity_check.predict([message['text']])[0]:
        logusage()
        sendMessage(text='Please Don\'t use profane language, thanks!', message=message, replyto=message)
        return 0
    return 1
