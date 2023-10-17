from netmiko import ConnectHandler
from getpass import getpass

username = input("Enter your username: ")
password = getpass("Enter your passwd: ")


ios_nodes = {
        "device_type":"cisco_ios",
        "ip": "192.168.3.43",
        "username": "master-code",
        "password": password,
        "secret": "net-lab",
    }
    
net_connect = ConnectHandler(**ios_nodes)
output = net_connect.send_command("show ip int br")
print(output)


