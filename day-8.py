# Configuration using for, if-else condition w.r.t interface and Routing

from netmiko import ConnectHandler
from getpass import getpass

username = input("Enter your username: ")
password = getpass("Enter your password: ")

router_details = {
    'ip': '192.168.145.138',
    'username' : username,
    'password' : password,
    'device_type' : 'cisco_ios'
}

ssh = ConnectHandler(**router_details)
print("Your access to device is now succesfull \n")

user_input = int(input("Enter the number of static routes you wish to use: "))

for i in range(0,user_input):
    network_id = input("Enter the destination network ID: ")
    subnet_mask = input("Enter the destination subnet mask: ")
    nxt_hop = input("Enter the next hop IP address: ")

    commands = [f' ip route {network_id} {subnet_mask} {nxt_hop}']

    static_configs = ssh.send_config_set(commands)
    print(static_configs)

    static_details = ssh.send_command("show run | inc ip route")
    print(static_details)

ssh.save_config()
ssh.disconnect()