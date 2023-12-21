import inspect
import os
from pathlib import Path


def logusage():
    # Get the caller's stack frame
    caller_frame = inspect.stack()[1]
    
    # Get the path of the file that called this, and extracts its filename without ext.
    modulename = Path(caller_frame[1]).stem
    
    print("Message being handled by " + modulename)
    return True
