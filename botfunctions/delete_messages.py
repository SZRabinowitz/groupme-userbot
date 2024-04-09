import os
import requests

def delete_message(message, token=os.getenv('groupme_api_key')):
    message_id = message['id']
    group_id = message['group_id']
    data = {"token": token}
    response = requests.delete(url=f"https://api.groupme.com/v3/conversations/{group_id}/messages/{message_id}", params = data)
    return response.status_code == 204

