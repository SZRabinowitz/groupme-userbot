from botfunctions.group_functions import get_group_members
import os

def is_user_admin_or_owner(message=None, user_id=None, group_id=None, token=os.getenv('groupme_api_key')):
    if not message and (not user_id or not group_id):
        raise Exception('Missing parameters')
    if message:
        user_id = message['user_id']
        group_id = message['group_id']
    group_members = get_group_members(group_id, token)
    for member in group_members:
        if member['user_id'] == user_id:
            return 'admin' in member['roles'], 'owner' in member['roles']
        

    
