from netmiko import ConnectHandler
import netmiko
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
from datetime import datetime
from time import strftime
from datetime import date
import time

#define timezone
current_time=datetime.now()
nowtime=current_time.strftime("%Y-%m-%d %H:%M:%S")

#define device from txt
fp=open('./devices/thaodien.txt','r+')
lines=fp.readlines()
for i in range(0,len(lines)):
        if "cisco" in lines[i]:
            ip1=lines[i].split(",")[0]
            username1=lines[i].split(",")[1]
            password1=lines[i].split(",")[2]
            device_type1=lines[i].split(",")[3].rstrip()
#create devices
            dv={'device_type': device_type1,
                'ip': ip1,
                'username': username1,
                'password': password1,
                'secret': password1,
                'verbose': False
                }
#connect device with netmiko            
            net_connect=ConnectHandler(**dv)
            print("Inventory Neighbors Device "+dv['ip']+": Processing!!!!")
            command="show cdp neighbors "
            send_command = net_connect.send_command_timing(command)
            result=(send_command)
#            print(result)
            hostname="show running-config | include hostname"
            send_hostname_command = net_connect.send_command_timing(hostname)       
            source = send_hostname_command.replace('hostname ', '')
            print(source)
            neighbors = result.splitlines()[5].split()
            replace_text = neighbors[0]
            dest = replace_text.replace('.bigc-vietnam.com', '')
#            destionation = neighbors.replace('.bigc-vietnam.com', '')
            neighbors1 = result.splitlines()[6].split()
#            print(destionation)
            print(neighbors1)
            interface_fr = neighbors1[0]
            no_fr = neighbors1[1]
            interface_to = neighbors1[6]
            no_to = neighbors1[7]
            print('Connection define : '+source+' to '+dest)
            print('Link : '+interface_fr+no_fr+' to '+interface_to+no_to)


            with open('./logging/log.txt', 'a') as f:
                f.write('________________Logging Time: '+nowtime+'\n'+send_hostname_command+'\n'+result+'\n\n')
                f.close()
           

'''
fp=open('./inventory_files/thaodienr1.txt','r+')
lines=fp.readlines()

for i in range(0,len(lines)):
    result = stdout.decode('ASCII')
    neib = result.splitlines()[4].split()
    print(neib)

ms = delay.split("/")
                    min = ms[0]
                    avg = ms[1]
                    max = ms[2]

'''

