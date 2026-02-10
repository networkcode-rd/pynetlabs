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

int_payload = """
<config>
	<interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
		<interface>
			<name>Loopback1947</name>
			<description>Pushed-by-RD-Std-1071</description>
			<type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
			<enabled>true</enabled>
			<ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
				<address>
					<ip>101.101.1.1</ip>
					<netmask>255.255.255.255</netmask>
				</address>
			</ipv4>
			<ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
		</interface>
    </interfaces>
</config>
"""

int_configs = netconf.edit_config(int_payload, target = "running")
print(int_configs)