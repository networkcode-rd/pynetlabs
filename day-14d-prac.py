# Using Restconf, we configure multiple interfaces using for_loop

import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass
import json
from urllib.parse import quote

csr_username = input("Enter your username: ")
csr_password = getpass("Enter your password: ")


csr_creds = HTTPBasicAuth(username=csr_username, password=csr_password)
csr_headers = {"Content-Type":"application/yang-data+json"}

user_input = int(input("Enter the number of that physcial interface that you wish to configure on the deivce: "))

for i in range(0, user_input):

  int_name = input("Enter the interface name: ")
  int_ip = input("Enter the IP address: ")
  int_mask = input("Enter the subnet mask: ")
  int_desc = input("Enter the interface description. Leave it empty if you do not wish to give any description: ")
  encoded_int = quote(int_name,safe="")
  csr_url = "https://10.10.20.213/restconf/data/ietf-interfaces:interfaces/interface=" + encoded_int
  int_payload = {
    "ietf-interfaces:interface":{
          "name": int_name,
          "type": "iana-if-type:ethernetCsmacd",
          "description": int_desc,
          "enabled": True,
          "ietf-ip:ipv4": {
            "address": [
              {
                "ip": int_ip,
                "netmask": int_mask
              }
            ]
          },
          "ietf-ip:ipv6": {
          }
        }
    }

  int_conf = requests.put(url=csr_url, auth=csr_creds, headers=csr_headers, data=json.dumps(int_payload), verify=False)

  print(int_conf.status_code)
  print(int_conf.text)