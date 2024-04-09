from gmbotmodules import logusage, sendMessage
import asyncio
import pyston



only_messages_with_text = True
moduleName = 'Python'
helpString = '/python <script> will return the output'
command = '/python'
case_sensitive = False

async def send_output(script, message):
    client = pyston.PystonClient()
    output = await client.execute("python", [pyston.File(script)])
    sendMessage(message=message, text=str(output))
    return output

def checkMessage(message):
    if message['text'].strip().casefold().startswith('/python'.strip().casefold()):
        logusage()
        output = asyncio.run(send_output(message['text'].strip()[7:], message))
        return True
    else: 
        return False