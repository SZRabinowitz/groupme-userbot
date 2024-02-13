import requests
import os

def get_message(group_id, message_id, token=os.getenv('groupme_api_key')):
    data = {"token": token}
    response = requests.get(url=f"https://api.groupme.com/v3/groups/{group_id}/messages/{message_id}", params = data)
    return response.json()['response']['message']
