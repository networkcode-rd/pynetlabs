# For configuring multiple interfaces and type of interfaces.
from ncclient import manager
from getpass import getpass

user_usernmae = input("Please type your username: ")
user_passwd = getpass("Please type your password: ")

router_details = {
    'host': "182.66.121.82",
    "username": user_usernmae,
    'password': user_passwd,
    'port': '8830',
    'hostkey_verify': False
}

netconf = manager.connect(**router_details)
print("Netconf Connection was created successfully")

user_inpt = int(input("How many times you wish to configure loopback interfaces?: "))

for int_config in range(0, user_inpt):

    user_2nd_choice = int(input("Do you wish to configure for Physical interface or Loopback Interface. Please type the desired option number shown below: \n1. Physical Interface\n2. Loopback Interface.\n Please select your option: "))

    if user_2nd_choice == 1:
        int_type = "ethernetCsmacd"
    elif user_2nd_choice == 2:
        int_type = "softwareLoopback"
    else:
        break

    int_name = input("Enter the interface name: ")
    int_ip = input("Enter the interface IP address: ")
    int_mask = input("Enter the subnet mask value: ")
    int_desc = input("Enter the interface description: ")

    int_payload = f"""
    <config>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>{int_name}</name>
                <description>{int_desc}</description>
                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:{int_type}</type>
                <enabled>true</enabled>
                <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                    <address>
                        <ip>{int_ip}</ip>
                        <netmask>{int_mask}</netmask>
                    </address>
                </ipv4>
                <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
            </interface>
        </interfaces>
    </config>
    """

    int_configs = netconf.edit_config(int_payload, target = "running")
    print(int_configs)