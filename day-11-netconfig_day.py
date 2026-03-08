from ncclient import manager
from getpass import getpass
from xml.dom.minidom import parseString

csr_username = input("Enter your username: ")
csr_password = getpass("Enter your password: ")

router_details = {
    'host': "192.168.0.106",
    "username": csr_username,
    'password': csr_password,
    'port': '830',
    'hostkey_verify': False,
    # device_params={'name': 'iosxe'}
}

netconf = manager.connect(**router_details)
print("Netconf Connection was created successfully")

running_config = netconf.get_config(source = "running")
pretty_running_conf = parseString(running_config.xml).toprettyxml()

myfile = open(r"D:\01-C.O.D.E\Pynetlabs\output.xml",'w')
myfile.write(pretty_running_conf)

print("Output is now extracted in the mentioned path")