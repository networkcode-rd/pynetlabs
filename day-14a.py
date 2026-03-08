import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

csr_username = input("Enter the username: ")
csr_pwd = getpass("Enter your password: ")
ip_value = "182.66.121.82"

csr_url = f"https://{ip_value}:8443/restconf/data/ietf-interfaces:interfaces"

csr_creds = HTTPBasicAuth(username=csr_username, password=csr_pwd)

csr_headers = {"Accept":"application/yang-data+json"}

int_details = requests.get(url=csr_url, auth = csr_creds, headers=csr_headers,verify=False)

print(int_details.text)
print(int_details.status_code)