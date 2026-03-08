# From XML to dictionary:-

# Filtering interface information from the running configuration:-

# This script is only to address static configuration.

from ncclient import manager
from getpass import getpass
from xml.dom.minidom import parseString
from xmltodict import parse
from pprint import pprint

device_ip = input('Enter the IP address of the Network device: ')
username = input("Please use your username: ")
pswd = getpass("Use the password: ")

router_details = {
    'host' : device_ip,
    'username' : username,
    'password' : pswd,
    'port' : '830',
    'hostkey_verify' : False
}

netconf_inputs = manager.connect(**router_details)
print("You have now logged in the device successfully.\n")

int_filter = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    </interfaces>
</filter>

"""

running_config = netconf_inputs.get_config(filter = int_filter, source = "running")
pretty_running_conf = parseString(running_config.xml).toprettyxml()
int_dict = parse(pretty_running_conf)
int_list = int_dict["rpc-reply"]['data']["interfaces"]["interface"]


for int_details in int_list:
    print(int_details['name'])
    try:
        int_ip = int_details["ipv4"]["address"]["ip"]
    except:
        int_ip = "not_configured"
    print("The IP address for the above mentioned interface is " + int_ip)



