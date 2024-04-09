from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter
import json
from colorama import init
from plugins.LogModuleUsage import logusage 
import gmbotmodules
import os
from types import ModuleType
import importlib

#def formattedMessage(message):

#This fixes issues on Windows machines with raw Ascii characters showing
if os.name == 'nt':
    init(convert=True)
modules = {}
all_commands = []
for module_name in gmbotmodules.__all__:
    modules[module_name] = (moduleobject:=importlib.import_module(f"gmbotmodules.{module_name}"), moduleobject.command, moduleobject.case_sensitive)

    # if type(module_name) == str:
    #     importlib.import_module(f"gmbotmodules.{module_name}")        
    #     all_commands.append(module_name.command.casefold())
    # elif type(module_name) == ModuleType:
    #     all_commands.append(module_name)
    print(f'Added Module: {module_name}')
def on_message(message):
    log_message_mode = os.getenv('log_messages')
    if log_message_mode == 'JSON':
        print(highlight(json.dumps(message, indent=2), JsonLexer(), TerminalFormatter()))
    if message['text']:
        for module_name, module in modules.items():
            if module[2]:
                if message['text'].strip().startswith(module[1]):
                    if not modules['disable'][0].is_command_disabled(message['group_id'], module_name):
                        module[0].checkMessage(message)
            else:
                if message['text'].strip().casefold().startswith(module[1].casefold()):
                    if not modules['disable'][0].is_command_disabled(message['group_id'], module_name):
                        module[0].checkMessage(message)

