# Doing Interface configuration, static Routing and dynamic Routing configuration

from netmiko import ConnectHandler
from getpass import getpass

username = input("Enter your username: ")
password = getpass("Enter your password: ")

router_details = {
    'ip': "192.168.79.128",
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


elif user_config_welcome_msg == 3:
    print("You have select Dynamic Routing- EIGRP configuraiton, please provide the requested information.")
    eigrp_as = int(input("Please put the EIGRP AS number: "))
    user_eigrp_input_routes = int(input("Please enter the number of networks that you wish to configure: "))
    
    for i in range(0, user_eigrp_input_routes):
        network_id = input("Enter the network ID: ")
        wildcard_m = input("Enter the wildcard mask: ")

        commands = [f" router eigrp {eigrp_as}", "no auto-summary", f"network {network_id} {wildcard_m}"]
        eigrp_cmds = ssh.send_config_set(commands)
        print(eigrp_cmds)

    eigrp_details = ssh.send_command("show run | sec eighrp")
    print(eigrp_details)


elif user_config_welcome_msg == 4:
    print("You have select Interface configuraiton, please provide the requested information.")

    ospf_process_id = input("Enter the OSPF process ID: ")
    no_of_routes_to_announce = int(input("Enter the number of networks you wish to advertise using OSPF: "))

    for ospf_ntwk in range(0, no_of_routes_to_announce):
        area_id = input("Enter the area ID: ")
        network_id = input("Enter the Network ID: ")
        wildcard_m = input("Enter the wildcard mask: ")

        ospf_commands = [f"router ospf {ospf_process_id}", 
                         f"network {network_id} {wildcard_m} area {area_id}"
                         ]
        push_ospf_config = ssh.send_config_set(ospf_commands)
        print(push_ospf_config)

        ospf_config_verification = ssh.send_command("show run | sec router ospf")
        print(ospf_config_verification)
        

else:
    print("You have provided wrong input. Please try again.")

ssh.save_config()