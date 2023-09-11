from netmiko import ConnectHandler
from getpass import getpass
username = input("Enter your username: ")
password = getpass()

with open("cisco10_dhcp") as f:
    commnad_list = f.read().splitlines()
with open("ip_nodes") as f:
    ip_list = f.read().splitlines()
    

    
for devices in ip_list:
    print("Connecting to device" + devices)
    ip_add_of_dev = devices
    ios_nodes = {
        "device_type":"cisco_ios",
        "ip":ip_add_of_dev,
        "username":"local-net",
        "password": "cisco"
    }
    
    net_connect = ConnectHandler(**ios_nodes)
    output = net_connect.send_config_set(commnad_list)
    print(output)