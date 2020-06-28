from netmiko import ConnectHandler
from multiprocessing import Process
from device_eve import main as device_list
from ntc_templates.parse import parse_output
from pprint import pprint
from datetime import datetime
from tqdm import tqdm
import sys
import time
def conn(device):
    return ConnectHandler(**device)
def config_int(device):
    telnet=conn(device)
    telnet.enable()
    ############## Cau hinh SSH #######################################
    command_1=[
        "int e0/0",
        "no switchport",
        "ip add dhcp",
        "no shut"
        ]
    command_2=[
        "ip domain-name blackdrag0n.pmk",
        "username admin pass 123",
        "crypto key ge rsa modul 1024",
        "line vty 0 4",
        "login local",
        "password 123",
        "transport input ssh"
    ]
    ####################################################
    telnet.send_config_set(command_1)
    telnet.send_config_set(command_2)
    data=telnet.send_command("show ip int br",delay_factor=15)
    parse_data=parse_output(platform="cisco_ios",command="show ip int br",data=data)
    telnet.disconnect()
    print("Hoan tat Device No."+str(device["port"]+" co IP: "+parse_data[0]["ipaddr"]))
def main():
    list_device=device_list()
    for device in tqdm(list_device):
        time.sleep(0.1)
        my_process=Process(target=config_int,args=(device,))
        my_process.start()
        print(my_process)
    print("Dang lay IP cac thiet bi")
def menu():
    choice='0'
    while choice =='0':
        print("Main Choice: Choose 1 of 5 choices")
        print("Choose 1 for something")
        print("Choose 2 for something")
        print("Choose 3 for something")
        print("Choose 4 for something")
        print("Choose 5 to go to another menu")

        choice = input ("Please make a choice: ")
        if choice == "5":
            print("Go to another menu")
            #second_menu()
        elif choice == "4":
            print("Do Something 4")
if __name__ == "__main__":
    try: 
        menu()
    except KeyboardInterrupt:
        print("\n Keyboard interrupt exception caught")
        sys.exit(0)