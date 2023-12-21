#credit https://stackoverflow.com/a/47473360
from os.path import dirname, basename, isfile
import glob
from plugins.LogModuleUsage import logusage 
from botfunctions.send_message import sendMessage 
modules = glob.glob(dirname(__file__)+"/*.py")
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

def getallcommands():
    print(all)
    return __all__
