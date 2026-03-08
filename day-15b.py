import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass
import json


asa_username = input("Enter the username: ")
asa_password = getpass("Enter the password: ")

asa_url = "https://10.10.20.65/api/fdm/v6/devices/default/interfaces/3f5eb864-9953-11ec-9b07-f16991e1abaa"

token_url = "https://10.10.20.65/api/fdm/latest/fdm/token"

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


int_payload = {
        "version" : "nttdrbqqkhzze",
    "name" : None,
    "description" : "Pushed_via_RestAPI",
    "hardwareName" : "GigabitEthernet0/2",
    "monitorInterface" : True,
    "ipv4" : {
      "ipType" : "STATIC",
      "defaultRouteUsingDHCP" : False,
      "dhcpRouteMetric" : None,
      "ipAddress" : {
        "ipAddress": "192.168.50.1",
        "netmask": "255.255.255.0",
        "standbyIpAddress": None,
        "type": "haipv4address"
    },
      "dhcp" : False,
      "addressNull" : False,
      "type" : "interfaceipv4"
    },
    "ipv6" : {
      "enabled" : False,
      "autoConfig" : False,
      "dhcpForManagedConfig" : False,
      "dhcpForOtherConfig" : False,
      "enableRA" : False,
      "dadAttempts" : 1,
      "linkLocalAddress" : {
        "ipAddress" : None,
        "standbyIpAddress" : None,
        "type" : "haipv6address"
      },
      "ipAddresses" : None,
      "prefixes" : None,
      "type" : "interfaceipv6"
    },
    "managementOnly" : False,
    "managementInterface" : False,
    "mode" : "ROUTED",
    "linkState" : "UP",
    "mtu" : 1500,
    "enabled" : True,
    "macAddress" : None,
    "standbyMacAddress" : None,
    "pppoe" : None,
    "speedType" : "AUTO",
    "duplexType" : "AUTO",
    "present" : True,
    "tenGigabitInterface" : False,
    "gigabitInterface" : True,
    "id" : "3f5eb864-9953-11ec-9b07-f16991e1abaa",
    "type" : "physicalinterface",
}

int_conf = requests.put(url=asa_url, headers=asa_headers, data=json.dumps(int_payload), verify=False)

print(int_conf.status_code)
print(int_conf.text)