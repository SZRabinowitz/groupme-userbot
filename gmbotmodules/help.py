from gmbotmodules import logusage, sendMessage
from gmbotmodules import __all__

moduleName = 'Help'
helpString = '/help will show this help message'

def checkMessage(message):
    if message['text'].strip().casefold() == '/help'.strip().casefold():
        logusage()
        help_message = "Hi, I am Avalon, a Python GroupMe bot inspired by Lowes Bot, with many functions ported from there.\nHere is what you can do with me: \n\n"
        for module_name in __all__:
            if type(module_name) == str:
                module = __import__(f"gmbotmodules.{module_name}", fromlist=["*"])
                help_message += (f"{module.moduleName}: {module.helpString} \n")
        
        
        
        sendMessage(message=message, text=help_message)
        return 0
    else: 
        return 1