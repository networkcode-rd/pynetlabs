# Configuring multiple Routers but with an option one Router at a time from a given list/dictionary

from netmiko import ConnectHandler
from getpass import getpass


router_dictionary = {
    "R03" : "192.168.145.145",
    "R04" : "192.168.145.144",
    "R05" : "192.168.145.143"
}

user_choice = input("Which router would you like to configure?: ")
user_choice = user_choice.upper()

router_ip = router_dictionary[user_choice]

username = input("Enter your username: ")
password = getpass("Enter your password: ")

device = {
    "ip" : router_ip,
    "username": username,
    "password": password,
    "device_type": "cisco_ios"
}

ssh = ConnectHandler(**device)
print(f"The Connection is now successful {user_choice}")

user_input = int(input("Enter the number of interfaces that you would like to configure: "))
for i in range(0,user_input):
    int_name = input("Enter the interaface name: ")
    int_ip = input("Enter the IP address you wish to configure: ")
    int_mask = input("Enter the subnet mask value: ")
    int_desc = input("Enter the description you wish to use: ")
    
    commands = [f"interface {int_name}", f"ip address {int_ip} {int_mask}", f"description {int_desc}", "no shut"]

    int_configuration =  ssh.send_config_set(commands)

shw_int_details = ssh.send_command("show ip int br")
print(shw_int_details)