import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass
import json

csr_username = input("Enter the username: ")
csr_pwd = getpass("Enter your password: ")
ip_value = "182.66.121.82"

csr_url = f"https://{ip_value}:8443/restconf/data/ietf-interfaces:interfaces"

csr_creds = HTTPBasicAuth(username=csr_username, password=csr_pwd)

csr_headers = {"Accept":"application/yang-data+json",
               "Content-Type": "application/yang-data+json"
               }

loop_payload = {
    "ietf-interfaces:interface": {
        "name": "Loopback2001",
        "description": "Created via RESTCONF",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "199.199.199.199",
                    "netmask": "255.255.255.255"
                }
            ]
        }
    }
}

response = requests.post(
    csr_url,
    auth=csr_creds,
    headers=csr_headers,
    data=json.dumps(loop_payload),
    verify=False
)

print("Status Code:", response.status_code)
print(response.text)
