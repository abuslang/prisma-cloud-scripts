#!/usr/bin/env python3
import authenticate
import json

response = json.loads(authenticate.login())
JWTtoken = response["token"]
print("logging in ...\n")
print("getting JWT token ...\n")
print(JWTtoken)