from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter
import json
from colorama import init
from plugins.LogModuleUsage import logusage 
from gmbotmodules import __all__
import os

#This fixes issues on Windows machines with raw Ascii characters showing
if os.name == 'nt':
    init(convert=True)

all_commands = []
for module_name in __all__:
    module = __import__(f"gmbotmodules.{module_name}", fromlist=["*"])
    all_commands.append(module)
    print(f'Added Module: {module_name}')

def on_message(message):
    log_message_json = (os.getenv('log_message', 'False') == 'JSON')
    if log_message_json:
        print(highlight(json.dumps(message, indent=2), JsonLexer(), TerminalFormatter()))
    for module in all_commands:
        module.checkMessage(message)
