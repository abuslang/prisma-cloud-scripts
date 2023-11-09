#!/usr/bin/env python3
import requests
import json
import authenticate
import config

# Endpoint URL for adding a user
#url = "https://api2.prismacloud.io/v3/user"
api_endpoint = config.url + "v3/user"


response = json.loads(authenticate.login())
JWTtoken = response["token"]

headers = {
    "Content-Type": "application/json",
    "x-redlock-auth": JWTtoken
}

# Request body for adding a new user account
# if we had a list of emails we could feed it in and have this script create a user for each unique email
data = {
    "email": "asquadri1@gmail.com",
    "firstName": "Abdus [test]",
    "lastName": "Quadri",
    "roleIds": ["1a7ebc2d-7dd9-4218-897f-1bcf43cba149"],
    "defaultRoleId": "1a7ebc2d-7dd9-4218-897f-1bcf43cba149",
    "timeZone": "America/Los_Angeles",
    "type": "USER_ACCOUNT"
}

# Convert the Python dictionary to a JSON string
json_data = json.dumps(data)

# Make the POST request
response = requests.post(api_endpoint, headers=headers, data=json_data)

# Check if the request was successful
if response.status_code == 200:
    print("User created successfully!")
else:
    print("Failed to create user:", response.text)

