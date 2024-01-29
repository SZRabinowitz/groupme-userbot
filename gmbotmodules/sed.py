from gmbotmodules import logusage, sendMessage, get_message, re
import plugins.sed as PythonSed
from io import StringIO

only_messages_with_text = True
moduleName = 'sed'
helpString = 'reply to a message with sed <sed str> and it will parse it using gnu sed'

def checkMessage(message):
    if re.search(r'^sed ([\'"])*s.{2,}([\'"])*\s*$', message['text']):
        if message['attachments']:
            if 'reply_id' in message['attachments'][0]:
                logusage()
                quoted_message = get_message(message['group_id'], message['attachments'][0]['reply_id'])
                sed = PythonSed.Sed()
                repl = message['text'][4:].replace("'", '').replace('"', '').replace("'", '').replace("'", '')
                sed.load_string(repl)
                out = sed.apply(StringIO(quoted_message['text']))

            if type (out) is str:
                message_to_send = out
            else:
                message_to_send = ' '.join(out).replace('\n ', '\n') #Make sure we dont add a space in beginning of newline


            sendMessage(message=message, text=message_to_send, replyto=quoted_message['id'])
            return True

    return False