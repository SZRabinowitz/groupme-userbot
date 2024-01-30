import requests
import os

class GroupMeMessage:
    def __init__(self, **kwargs):
        # Set attributes dynamically based on provided keyword arguments
        for key, value in kwargs.items():
            setattr(self, key, value)

def get_message(group_id, message_id, token=os.getenv('groupme_api_key')):
    # Constructing the data payload with the token
    data = {"token": token}
    
    # Making an HTTP GET request to the GroupMe API
    response = requests.get(url=f"https://api.groupme.com/v3/groups/{group_id}/messages/{message_id}", params=data)
    
    # Extracting data from the JSON response
    message_data = response.json()['response']['message']
    
    # Creating a GroupMeMessage object with dynamic attributes
    message_object = GroupMeMessage(**message_data)
    
    # Returning the created object
    return message_object