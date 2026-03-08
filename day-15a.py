# Importing FTD interface information via Rest API
import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

asa_username = input("Enter the username: ")
asa_password = getpass("Enter the password: ")

ftd_mgmt_ip = "10.10.20.65"

# asa_creds = HTTPBasicAuth(username=asa_username, password=asa_password)

token_url = f"https://{ftd_mgmt_ip}/api/fdm/latest/fdm/token"

payload = {
    "grant_type" : "password",
    "username" : asa_username,
    "password" : asa_password
}

token_headers = {
    "Content-Type": "application/json"
}
token_response = requests.post(token_url, json=payload, headers=token_headers, verify=False)

access_token = token_response.json()['access_token']

asa_headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {access_token}"
}

asa_url = "https://10.10.20.65/api/fdm/v6/devices/default/interfaces"
device_int = requests.get(url=asa_url, headers=asa_headers, verify=False)

print(device_int.status_code)
print(device_int.text)