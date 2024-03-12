import requests
import json

payload = None
netid=''
serial=''
ipaddress=''
name=''
model=''
firm=''
netid=input("*********** Enter NETWORK ID ***************\n")
print('..................Loading..................\n')
url = "https://api.meraki.com/api/v1/networks/"+netid+"/devices"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "124ba22065f49b42515c3fb34931f29c900a70f2"
}
response = requests.request('GET', url, headers=headers, data = payload)
#print(response.text.encode('utf8'))
json_data = response.text.encode('utf8')
json_object = json.loads(json_data)
f=open('log.txt', 'w')
json_formatted_str = json.dumps(json_object, indent=2)
f.write(json_formatted_str)
f.close()

f=open('log.txt','r')
lines=f.readlines()
for i in range(0,len(lines)):
  if "name" in lines[i]:
    name=lines[i].split(":")[1]
    print('Name of AP: '+name)
  if "model" in lines[i]:
    model=lines[i].split(":")[1]
    print('Model of AP: '+model)
  if "firmware" in lines[i]:
    firm=lines[i].split(":")[1]
    print('Firmware of AP: '+firm)
  if "lanIp" in lines[i]:
    ipaddress=lines[i].split(":")[1]
    print('IP Address of AP: '+ipaddress)
  if "serial" in lines[i]:
    serial=lines[i].split(":")[1]
    print('Serial Number: '+serial)
    print('==============================')
