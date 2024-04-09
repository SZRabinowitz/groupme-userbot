import requests, os
def get_group_members(group_id, token=os.getenv('groupme_api_key')):
    data = {"token": token}
    response = requests.get(url=f"https://api.groupme.com/v3/groups/{group_id}", params = data)
    return response.json()['response']['members']
