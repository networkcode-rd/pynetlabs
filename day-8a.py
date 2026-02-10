from netmiko import ConnectHandler
from getpass import getpass

username = input("Enter your username: ")
password = getpass("Enter your password: ")

router_details = {
    'ip': "192.168.145.138",
    'username': username,
    'password': password,
    'device_type': 'cisco_ios'
}

ssh = ConnectHandler(**router_details)
print("SSH Connection is now successfully established \n")

user_config_welcome_msg = int(input('''Welcome to Router Configuration console!\nPlease select the mention the option number that you would like to proceed\n
                                    1. Interface configuration
                                    2. Static Routing
                                    3. Dynamic Routing - EIGRP
                                    4. Dynamic Routin - OSPF\n
'''))

# print(user_config_welcome_msg)
if user_config_welcome_msg == 1:
    print("You have select Interface configuraiton, please provide the requested information.")

    user_input = int(input("How many interface you wish to configure?: "))

    for i in range(0,user_input):
        int_name = input("Enter the interface name: ")
        int_ip = input("Enter the interface IP address: ")
        int_mask = input("Enter the IP mask value: ")
        int_desc = input("Provide a name to define the interface: ")

        commands = [f"interface {int_name}", f"ip address {int_ip}", "no shut", f"description {int_desc}"]
        int_configs = ssh.send_config_set(commands)
    
    int_show_output = ssh.send_command("show ip int br")
    print(int_show_output)


elif user_config_welcome_msg == 2:
    print("You have select Static Routing configuraiton, please provide the requested information.")
    user_static_input = int(input("Please enter the number of static routes you wish to configure: "))

    for i in range(0,user_static_input):
        network_id = input("Please enter the Network Address you wish to reach: ")
        dst_sub_mask = input("Please enter the Subnet Mask value for the previously provided Network address: ")
        nxt_hop = input("Where do you want this destination route to point to?: ")
        cmds = [f"ip route {network_id} {dst_sub_mask} {nxt_hop} "]
        static_dtls = ssh.send_config_set(cmds)
    shw_static_config = ssh.send_command("show run | inc ip route")
    print(shw_static_config)


# elif user_config_welcome_msg == 3:
#     print("You have select Dynamic Routing- EIGRP configuraiton, please provide the requested information.")
#     eigrp_as = int(input("Please put the EIGRP AS number: "))
#     user_eigrp_input = input("Please enter the number of networks that you wish to configure: ")
#     for i in range()


# elif user_config_welcome_msg == 4:
#     print("You have select Interface configuraiton, please provide the requested information.")

else:
    print("You have provided wrong input. Please try again.")