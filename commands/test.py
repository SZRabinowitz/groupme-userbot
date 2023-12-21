import time
import asyncio
from commands import logusage, sendMessage


def checkMessage(message):
    if message['text'] == 'test':
        logusage()
        sendMessage(text='Test Received', message=message)
        return True
    else: 
        return False