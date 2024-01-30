from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter
import json
from colorama import init
from plugins.LogModuleUsage import logusage 
from gmbotmodules import __all__
import os
from types import ModuleType

#This fixes issues on Windows machines with raw Ascii characters showing
if os.name == 'nt':
    init(convert=True)

all_commands = []
for module_name in __all__:
    if type(module_name) == str:
        module = __import__(f"gmbotmodules.{module_name}", fromlist=["*"])
        all_commands.append(module)
    elif type(module_name) == ModuleType:
        all_commands.append(module_name)
    print(f'Added Module: {module_name}')
def on_message(message):
    log_message_mode = os.getenv('log_messages')
    if log_message_mode == 'JSON':
        print(highlight(json.dumps(message, indent=2), JsonLexer(), TerminalFormatter()))
    if message['text']:
        for module in all_commands:
            module.checkMessage(message)
    else: 
        for module in all_commands:
            if f"{module}.only_messages_with_text" in locals() and module.only_messages_with_text:
                continue

