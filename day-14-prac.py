# Using Restconf, we get / pull interface configuration

import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

csr_username = input("Enter your username: ")
csr_password = getpass("Enter your password: ")

csr_url = "https://10.10.20.213/restconf/data/ietf-interfaces:interfaces"

csr_creds = HTTPBasicAuth(username=csr_username, password=csr_password)

csr_headers = {"Accept":"application/yang-data+json"}

int_details = requests.get(url=csr_url, auth=csr_creds, headers=csr_headers, verify=False)

print(int_details.status_code)
print(int_details.text)