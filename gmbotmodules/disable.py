import os
import gmbotmodules
from gmbotmodules.mymodules import logusage, sendMessage, random, re, json, is_user_admin_or_owner
import dataset 
only_messages_with_text = True
moduleName = 'Disable'
helpString = '/disable <command> will disable the command from being ran'
db = dataset.connect(os.getenv('DATABASE_URL'))
allmodules = gmbotmodules.__all__
command = '/disable'
case_sensitive = False
table = db['disabledcommands']


def checkMessage(message):
    if message['text'].strip().casefold().startswith('/disable'.strip().casefold()):
        logusage()
        is_admin, is_owner = is_user_admin_or_owner(message)
        if is_admin or is_owner:
            if len(message['text'].strip().split()) != 2:
                sendMessage(message=message, text='Invalid syntax. Please use /disable <command> to disable a command. Example: /disable egg.')
                return True
            else:
                command = message['text'].strip().split()[1].casefold()
                if command in allmodules:
                    table.upsert({'group_id': message['group_id'], 'command': command}, ['group_id', 'command'])
                    sendMessage(message=message, text=f'Command {command} has been disabled.')
                else:
                    sendMessage(message=message, text=f'Command {command} is not a valid command.')
        else:
            sendMessage(message=message, text='You do not have permission to use this command')
        
        return True
    else: 
        return False


def is_command_disabled(group_id, command):
    if table.find_one(group_id=group_id, command=command.casefold()):
        return True
    else:
        return False