import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass
import json

csr_username = input("Enter the username: ")
csr_pwd = getpass("Enter your password: ")
ip_value = "182.66.121.82"

csr_url = f"https://{ip_value}:8443/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet3"

csr_creds = HTTPBasicAuth(username=csr_username, password=csr_pwd)

csr_headers = {"Accept":"application/yang-data+json",
               "Content-Type": "application/yang-data+json"
               }

int_payload = {
    "ietf-interfaces:interface": {
        "name": "GigabitEthernet3",
        "description": "Configured via RESTCONF",
        "type": "iana-if-type:ethernetCsmacd",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "10.10.10.1",
                    "netmask": "255.255.255.0"
                }
            ]
        }
    }
}

response = requests.put(
    csr_url,
    auth=csr_creds,
    headers=csr_headers,
    data=json.dumps(int_payload),
    verify=False
)

print("Status Code:", response.status_code)
print(response.text)
