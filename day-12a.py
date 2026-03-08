# Creating Loopback interface = single interface script

from ncclient import manager
from getpass import getpass

user_usernmae = input("Please type your username: ")
user_passwd = getpass("Please type your password: ")
device_mgmt_int_ip = input("Please type the interface IP or device IP for getting SSH access: ")

router_details = {
    'host': device_mgmt_int_ip,
    "username": user_usernmae,
    'password': user_passwd,
    'port': 830,
    'hostkey_verify': False
}

netconf = manager.connect(**router_details)
print("Netconf Connection was created successfully")

int_payload = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>Loopback4</name>
      <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
      <enabled>true</enabled>
      <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
        <address>
          <ip>10.1.1.1</ip>
          <netmask>255.255.255.255</netmask>
        </address>
      </ipv4>
    </interface>
  </interfaces>
</config>
"""

int_config = netconf.edit_config(int_payload, target = "running")
print(int_config)



