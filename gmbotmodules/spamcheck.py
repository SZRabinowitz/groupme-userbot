import re
from gmbotmodules.mymodules import logusage, sendMessage
from botfunctions.delete_messages import delete_message

only_messages_with_text = True
moduleName = 'spamcheck'
helpString = 'Detects Spam'
command = ''
case_sensitive = False

def checkMessage(message):
    if message['attachments']:
        if is_spam(message['text']):
            logusage()
            if delete_message(message):
                sendMessage(message=message, text='Spam detected and deleted.')
            else:
                sendMessage(message=message, text='Spam detected. If you promote me to admin, I can automatically delete future spam.')
            return True
        else:
            return False


def is_spam(string):
    if not " - " in string or not string.strip().startswith("http") or not any(word in string.casefold() for word in ['essay', 'paper', 'writing', 'hentai', '18+ only']):
        return False
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.search(regex, string)
    if url:
        if url.span()[0] == 0:
            url_end = url.span()[1]
            while len(string) > url_end:
                if string[url_end] == ' ':
                    url_end += 1
                elif string[url_end] == '-':
                    return True
                else:
                    return False
