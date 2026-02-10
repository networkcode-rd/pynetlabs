from ncclient import manager
from getpass import getpass
from xml.dom.minidom import parseString

csr_username = input("Enter your username: ")
csr_password = getpass("Enter your password: ")

router_details = {
    'host': "182.66.121.82",
    "username": csr_username,
    'password': csr_password,
    'port': '8830',
    'hostkey_verify': False
}

netconf = manager.connect(**router_details)
print("Netconf Connection was created successfully")

running_config = netconf.get_config(source = "running")
pretty_running_conf = parseString(running_config.xml).toprettyxml()

myfile = open(r"D:\01 C.O.D.E\PyNetLabs_Demos\output.xml",'w')
myfile.write(pretty_running_conf)

print("Output is now extracted in the mentioned path")