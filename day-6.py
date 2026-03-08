# installed netmiko using <python.exe -m pip install --upgrade netmiko>

# using SSH

from netmiko import ConnectHandler

router_details = {"ip":"192.168.145.136",
                  "username": "admin",
                  "password": "cisco",
                  "device_type": "cisco_ios"
                  }

ssh = ConnectHandler(**router_details)
print("SSH Connection established")

commands = ["interface loopback 0","ip address 192.168.0.1 255.255.255.0", "description cofig_using_Netmiko_program"]
int_configs = ssh.send_config_set(commands)
print(int_configs)

int_details = ssh.send_command("show ip int br")
print(int_details)

ssh.save_config()

ssh.disconnect()