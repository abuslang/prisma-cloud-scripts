#!/usr/bin/env python3
import requests
import json
import config
import authenticate

# Function to get the list of roles from the API
def list_user_roles(api_endpoint, headers):
    response = requests.get(api_endpoint, headers=headers)
    if response.status_code == 200:
        return response.json()  # Returns a list of roles
    else:
        raise Exception(f"Failed to list user roles: {response.status_code}, {response.text}")

# Function to find the role ID given a role name from the list of roles
def get_role_id_by_name(roles, role_name):
    for role in roles:
        if role['name'] == role_name:
            return role['id']
    return None  # Return None if not found



def find_role_id_for_name(role_name_to_find):
    response = json.loads(authenticate.login())
    JWTtoken = response["token"]
    api_endpoint = config.url + "user/role"
    headers = {
        'Content-Type': 'application/json',
        'x-redlock-auth': JWTtoken
    }

    try:
        # Get all user roles
        roles = list_user_roles(api_endpoint, headers)
        
        # Find the ID for the role name
        role_id = get_role_id_by_name(roles, role_name_to_find)
        
        return role_id  # Return the role ID or None if not found
    except Exception as e:
        print(e)
        return None  # Return None if an exception occurred
