from netmiko import ConnectHandler
from multiprocessing import Process
from device_eve import main as device_list
from ntc_templates.parse import parse_output
from pprint import pprint
from datetime import datetime
from tabulate import tabulate
import sys
def conn(device):
    return ConnectHandler(**device)
def config_int(device):
    telnet=conn(device)
    telnet.enable()
    #Cau hinh SSH
    command_1=["int e0/0","no switchport","ip add dhcp","no shut"]
    command_2=["ip domain-name blackdrag0n.pmk","username admin pass 123","crypto key ge rsa modul 1024","line vty 0 4"
    ,"login local","password 123","transport input ssh"]
    #############
    telnet.send_config_set(command_1)
    telnet.send_config_set(command_2)
    data=telnet.send_command("show ip int br",delay_factor=15)
    parse_data=parse_output(platform="cisco_ios",command="show ip int br",data=data)
    telnet.disconnect()
    print("Hoan tat Device No."+str(device["port"]+" co IP: "+parse_data[0]["ipaddr"]))
def main():
    list_device=device_list()
    for device in list_device:
        my_process=Process(target=config_int,args=(device,))
        my_process.start()
if __name__ == "__main__":
    try: 
        main()
    except KeyboardInterrupt:
        print("\n Keyboard interrupt exception caught")
        sys.exit(0)