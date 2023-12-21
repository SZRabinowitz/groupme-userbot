import os
from groupme_push.client import PushClient, logger
from config import botconfig
from botfunctions import handle_messages
import signal
import time
import logging 


def signal_handler(sig, frame):
    print("\nStopping bot...")
    client.stop()
    sys.exit(0)


def get_user_info():
    api_key = os.getenv('groupme_api_key')
    user_id = os.getenv('groupme_user_id')
    ignore_self = (os.getenv('ignore_self', 'False') == 'True')
    logger.debug("Ignoring Own Messages: " + str(ignore_self))
    return api_key, user_id, ignore_self

def initializebot():
    api_key, user_id, ignore_self = get_user_info()
    client = PushClient(access_token=api_key, on_message=handle_messages.on_message, disregard_self=ignore_self)
    signal.signal(signal.SIGINT, signal_handler)
    try:
        client.start()
        print("Bot started successfully")
        while True:
            time.sleep(1)
    except Exception:
        client.stop()
        
def setLoggingLevel():
    if os.getenv('include_debug_logs') == 'True':
        logging.basicConfig(level=logging.DEBUG)
