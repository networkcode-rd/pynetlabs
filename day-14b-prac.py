# Using Restconf, we configure loopback

import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass
import json

csr_username = input("Enter your username: ")
csr_password = input("Enter your password: ")

csr_url = "https://192.168.0.110/restconf/data/ietf-interfaces:interfaces"
csr_creds = HTTPBasicAuth(username=csr_username, password=csr_password)
csr_headers = {"Content-Type":"application/yang-data+json"}

int_payload = {
    "interface":{
        "name": "Loopback5",
        "type": "iana-if-type:softwareLoopback",
        "description": "Configured by RestConf",
        "enabled": True,
        "ietf-ip:ipv4": {
          "address": [
            {
              "ip": "101.1.1.1",
              "netmask": "255.255.255.255"
            }
          ]
        },
        "ietf-ip:ipv6": {
        }
      }
}

int_conf = requests.post(url=csr_url, auth=csr_creds, headers=csr_headers, data=json.dumps(int_payload), verify=False)

print(int_conf.status_code)
print(int_conf.text)