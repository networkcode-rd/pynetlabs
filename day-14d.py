# Multiple interaces - phycial - RestConf

import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass
import json

csr_username = input("Enter the username: ")
csr_pwd = getpass("Enter your password: ")
ip_value = "182.66.121.82"

csr_headers = {"Accept":"application/yang-data+json",
               "Content-Type": "application/yang-data+json"
               }



user_input = int(input("How many interfaces you wish to configure?: "))

csr_creds = HTTPBasicAuth(username=csr_username, password=csr_pwd)


for int_config in range(0, user_input):

    int_name = input("Enter the interface name: ")
    int_ip = input("Enter the IP address for selected interaface: ")
    int_mask = input("Enter the subnet mask: ")
    int_desc = input("Enter the interaface description: ")

    csr_url = f"https://{ip_value}:8443/restconf/data/ietf-interfaces:interfaces/interface=" + int_name
    int_payload = {
        "ietf-interfaces:interface": {
            "name": int_name,
            "description": int_desc,
            "type": "iana-if-type:ethernetCsmacd",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [
                    {
                        "ip": int_ip,
                        "netmask": int_mask
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
