import inspect
import os
from pathlib import Path


def logusage():
    calling_module = inspect.getmodule(inspect.getouterframes(inspect.currentframe())[1][0])    
    
    print("Message being handled by " + str(calling_module.moduleName))



