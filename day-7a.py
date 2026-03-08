# Configuring using input function

from netmiko import ConnectHandler

router_username = input("please put the username to login: ")
password_router = input("please use the password as next step: ")

router_details = {"ip": "192.168.145.137", "username" : router_username, "password": password_router, "device_type" : "cisco_ios"}

ssh = ConnectHandler(**router_details)
print("You have logged in successfully.")
test = input("Use a show command to verify the interface name: or numeric: ")
int_details = ssh.send_command(test)
print(int_details)

int_name = input ("Put a interface that you would like to configure in configuraiton interface mode: ")
int_ip = input ("Enter the interface IP: ")
int_mask = input("Enter the subnet mask: ")
int_des = input("Enter any specific name you would like to name this interface used for: ")


commands = [f"interface {int_name}", f"ip address {int_ip} {int_mask}", f"description {int_des}", "no shut"]
int_configs = ssh.send_config_set(commands)
print(int_configs)

updated_interfaces = input ("Enter the interface details to see the newly reflected change: ")
print(updated_interfaces)

ssh.save_config()
ssh.disconnect()