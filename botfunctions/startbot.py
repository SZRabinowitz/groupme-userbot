import json
import os
from groupme_push.client import PushClient
from config import botconfig
from botfunctions import handle_messages
import signal
import time
import logging 
import sys
import requests

logger = logging.getLogger("gmpush-example")


def signal_handler(client, sig, frame):
    print("\nStopping bot")
    client.stop()
    sys.exit(0)


def get_user_info():
    api_key = os.getenv('groupme_api_key')
    ignore_self = (os.getenv('ignore_self', 'False') == 'True')
    logger.debug("Ignoring Own Messages: " + str(ignore_self))
    headers = {"X-Access-Token": api_key}
    resp = requests.get(
        "https://api.groupme.com/v3/users/me",
        headers=headers,
        timeout=5,
    )
    user = json.loads(resp.text)
    username = user["response"]["name"]

    return api_key, ignore_self, username

def initializebot():
    general_debug_logs = os.getenv('logging_method')
    if general_debug_logs == 'console':
        logging.basicConfig(level=logging.DEBUG)
    elif general_debug_logs == 'file':
        logging.basicConfig(filename='gmbot.log', level=logging.DEBUG)
    logger.setLevel(logging.INFO)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    logger.addHandler(console_handler)
    api_key, ignore_self, username = get_user_info()
    client = PushClient(access_token=api_key, on_message=handle_messages.on_message, disregard_self=ignore_self, reconnect=20)
    signal.signal(signal.SIGINT, lambda signal, frame: signal_handler(client, signal, frame))
    try:
        client.start()
        logger.info(f"Bot started successfully under account {username}")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        client.stop()
