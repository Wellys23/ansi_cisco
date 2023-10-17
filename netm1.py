from netmiko import ConnectHandler
from getpass import getpass

username = input("Enter your username: ")
password = getpass()

SW1_nodes = {
    "device_type":"cisco_ios",
    "ip":"192.168.3.99",
    "username":"master-code",
    "password": password,
    "secret": 'net-lab'
}
    
SW2_nodes = {
    "device_type":"cisco_ios",
    "ip":"192.168.3.43",
    "username":"master-code",
    "password": password,
    "secret": 'net-lab'
}

for nodes in SW1_nodes,SW2_nodes:
    net_connect = ConnectHandler(**nodes)
    output = net_connect.send_command("show ip int br")
    print(output)