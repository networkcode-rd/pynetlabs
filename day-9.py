# Configuring multiple Routers

from netmiko import ConnectHandler
from getpass import getpass

username = input("Enter your username: ")
password = getpass("Enter your password: ")

R03 = "192.168.145.140"
R04 = "192.168.145.141"
R05 = "192.168.145.142"

routers = [R03, R04, R05]

for devices in routers:
    device = {
        "ip" : devices,
        "username": username,
        "password": password,
        "device_type": "cisco_ios"
    }

    ssh = ConnectHandler(**device)
    print("The Connection is now successful" + devices)

    user_input = int(input("Enter the number of interfaces that you would like to configure: "))
    for i in range(0,user_input):
        int_name = input("Enter the interaface name: ")
        int_ip = input("Enter the IP address you wish to configure: ")
        int_mask = input("Enter the subnet mask value: ")
        int_desc = input("Enter the description you wish to use: ")
        
        commands = [f"interface {int_name}", f"ip address {int_ip} {int_mask}", f"description {int_desc}"]

        int_configuration =  ssh.send_config_set(commands)
    
    shw_int_details = ssh.send_command("show ip int br")
    print(shw_int_details)