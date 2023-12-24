import requests
import os
import time
import uuid


def sendMessage(token=os.getenv('groupme_api_key'), group_id=None, text=None, message=None, images=None):
    if text is None and images is None:
        print("Must provide text...")
        return 1
    if message is None:
        if group_id is None:
            print("Invalid args provided. No Group_id or message specified")
            return 1
    
    else: 
        group_id = message['group_id']

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
            "attachments": []
        }
    }
    
    if images: 
        if type(images) == str:
            images = [images]



        for image in images:
            attachment = {
            "type": "image",
            "url": image,
            }
            data['message']['attachments'].append(attachment)
        
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        return "Message sent successfully."
    else:
        return f"Failed to send message. Status code: {response.status_code}"
