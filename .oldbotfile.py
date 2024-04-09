import json
import websockets
import asyncio
import requests
import re
import uuid
import time
import regex_spm
import traceback
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter
import colorama
import time


colorama.init(convert=True)


def parse_zman_requests(text):
    day = "today"
    zip_code = None
    invalid_args = []
    for item in text.split():
        match regex_spm.search_in(item):
            case r"\d{5}": 
                zip_code = item
            case "today":
                day = "today"
            case "tomorrow":
                day = "tomorrow"
            case _: 
                invalid_args.append(item)
    print([day, zip_code, invalid_args])
    return [day, zip_code, invalid_args]


def send_groupme_message(token, group_id, text):
    url = f"https://api.groupme.com/v3/groups/{group_id}/messages"
    headers = {
        "Content-Type": "application/json",
        "X-Access-Token": token,
    }
    
    # Generate a source GUID using the current time, group ID, and a random UUID
    source_guid = f"{int(time.time() * 1000)}_{group_id}_{uuid.uuid4()}"

    data = {
        "message": {
            "source_guid": source_guid,
            "text": text,
        }
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        return "Message sent successfully."
    else:
        return f"Failed to send message. Status code: {response.status_code}, Response: {response.text}"


# Your WebSocket URL
websocket_url = "wss://push.groupme.com/faye"

# Your user ID and token
user_id = "112625035"
token = "lBkC2FbRtoP9ycNIVSccu817XjO3YyqkoB9rXPXs"

async def on_message(websocket, message):
    try:
        message_text = message[0]['data']['subject']['text']
        print(highlight(json.dumps(message[0]['data']['subject'], indent = 4), JsonLexer(), TerminalFormatter()))
        bot_msg = False
        if re.search(r"\b\d{5}\b", message_text):
            if not str(message[0]['data']['subject']['user_id']) == str(user_id):
                result = parse_zman_requests(message_text)
                if result[0] == None:
                    send_groupme_message(token, message[0]['data']['subject']['group_id'], "You must specify Zip Code")
                elif result[2]:
                    print(' '.join(map(str, result[2])))
                    send_groupme_message(token, message[0]['data']['subject']['group_id'], f"Invalid arguements: {', '.join(map(str, result[2]))}")
                else:
                    send_groupme_message(token, message[0]['data']['subject']['group_id'], f"Zip Code: {result[1]}\n Day: {result[0]}")
    except Exception as e:
        print(f"Could not extract text: {e}")
        print(message)
        traceback.print_exc()

async def connect_websocket():
    uri = f'{websocket_url}?access_token={token}'
    async with websockets.connect(uri) as websocket:
        # Perform handshake to obtain client ID
        handshake_message = {'channel': '/meta/handshake', 'version': '1.0', 'supportedConnectionTypes': ['websocket']}
        await websocket.send(json.dumps(handshake_message))
        response = await websocket.recv()
        response_data = json.loads(response)
        
        # Extract client ID from the handshake response
        client_id = None
        if isinstance(response_data, list) and len(response_data) > 0:
            client_id = response_data[0].get('clientId')

        # Subscribe to the user channel using the obtained client ID
        if client_id:
            subscription_path = f'/user/{user_id}'
            subscription_message = {
                'channel': '/meta/subscribe',
                'clientId': client_id,
                'subscription': subscription_path,
                'ext': {'access_token': token}
            }
            await websocket.send(json.dumps(subscription_message))
            response = await websocket.recv()
            print("Ready!")

            while True:
                response = await websocket.recv()
                message = json.loads(response)
                await on_message(websocket, message)

# Start the event loop
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(connect_websocket())
loop.close()





