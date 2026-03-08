# Using Restconf, we configure physical interface

import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass
import json

csr_username = input("Enter your username: ")
csr_password = input("Enter your password: ")

csr_url = "https://10.10.20.213/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1%2F0%2F3"
csr_creds = HTTPBasicAuth(username=csr_username, password=csr_password)
csr_headers = {"Content-Type":"application/yang-data+json"}

int_payload = {
    "interface": [
      {
        "name": "GigabitEthernet1/0/3",
        "type": "iana-if-type:ethernetCsmacd",
        "description": "Modified by RestConf",
        "enabled": True,
        "ietf-ip:ipv4": {
          "address": [
            {
              "ip": "112.1.1.1",
              "netmask": "255.255.255.0"
            }
          ]
        }
      }
    ]
  }


int_conf = requests.put(url=csr_url, auth=csr_creds, headers=csr_headers, data=json.dumps(int_payload), verify=False)

print(int_conf.status_code)
print(int_conf.text)


# import requests
# from requests.auth import HTTPBasicAuth
# from getpass import getpass

# csr_username = input("Enter your username: ")
# csr_password = getpass("Enter your password: ")

# csr_url = "https://10.10.20.213/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1%2F0%2F2"

# csr_headers = {
#     "Content-Type": "application/yang-data+json",
#     "Accept": "application/yang-data+json"
# }

# int_payload = {
#   "ietf-interfaces:interface": {
#         "name": "GigabitEthernet1/0/2",
#         "type": "iana-if-type:ethernetCsmacd",
#         "description": "Modified by RestConf",
#         "enabled": True
#   }
# }

# int_conf = requests.put(
#     url=csr_url,
#     auth=HTTPBasicAuth(csr_username, csr_password),
#     headers=csr_headers,
#     json=int_payload,
#     verify=False
# )

# print(int_conf.status_code)
# print(int_conf.text)