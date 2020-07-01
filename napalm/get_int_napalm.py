import sys
import time
from napalm import get_network_driver
import os
from pprint import pprint
#dev_type = 'ios'
dev_creds={
   'dev_type':'ios',
   'hostname': '10.215.26.233',
   'username': 'admin',
   'password': '123',
   'optional_args': {'secret': '321'}
 } # Use a dictionary for the login parameters
  

conn = get_network_driver(**dev_creds)
conn.open()
output = conn.get_interfaces()
pprint(output)
'''
sw2 = {
    "device_type":"cisco_ios",
    "ip":"10.215.26.234",
    "username":"admin",
    "password":"123",
    "secret":"321"
    }
'''