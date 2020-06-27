from getpass import getpass
import sys
#from pprint import pprint # for troubleshoot
def main():
    server=input("IP cua Server EVE-ng: ")
    sl=int(input("So luong thiet bi co trong he thong: "))
    device_list=create_list_device(sl,device_info(server))
    #pprint(device_list)# for troubleshoot
    return device_list
def device_info(server):
    Sw = {
        "device_type":"cisco_ios_telnet",
        "ip":server,
        "port":"32769",
        "secret":"321",
    }
    return Sw
def create_list_device(sl,device):
    system=[device]
    for i in range (1,sl):                          # Tao list danh sach thiet bi                              #
        Sw_copy=device.copy()                       #
        Sw_copy["port"]=str(int(device["port"])+i)  #
        system.append(Sw_copy)                      #
    return system
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n Keyboard interrupt exception caught")
        sys.exit(0)

