import requests
import json

payload = None
netid=''
ssid=''
day1=''
day2=''
day3=''
client1=''
netid=input("*********** Enter NETWORK ID *************\n\n")
print('..................Loading..................\n')
print("ssid number 1: GO!Guest\nssid number 2: CGV\nssid number 3: CGV-BOD\nssid number 4: CGV-MGNT\nssid number 5: CGV-APP\n")
ssid=input("*********** Select SSID Number for Query *************\n")
url = "https://api.meraki.com/api/v1/networks/"+netid+"/wireless/clientCountHistory?ssid="+ssid+"&timespan=2678400"
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
print(ssid)
#if 1 in ssid:
#  print("Thống kê client truy cập wifi GO! Guest")

#if ssid is 2:
#  print('Thống kê client truy cập wifi CGV')
#  print('Ngày'+day1.replace('T00', '"')+'\n')
#if ssid is 3:
#  print('Thống kê client truy cập wifi CGV-BOD')
#  print('Ngày'+day1.replace('T00', '"')+'\n')
#if ssid is 4:
#  print('Thống kê client truy cập wifi CGV-MGNT')
#  print('Ngày'+day1.replace('T00', '"')+'\n')
#if ssid is 5:
#  print('Thống kê client truy cập wifi CGV-APP')
#  print('Ngày'+day1.replace('T00', '"')+'\n')
for i in range(0,len(lines)):
 if "startTs" in lines[i]:
  day1=lines[i].split(":")[1]
  #day2=lines[i].split(",")[1]
  #day3=lines[i].split(",")[2]
  print('Ngày'+day1.replace('T00', '"')+'\n')

 if "clientCount" in lines[i]:
   client1=lines[i].split(":")[1]
   print('Client Count ='+client1+'\n----------------------------------------------')




#if ("startTs" in json_formatted_str):
# print (send_Filename)
#print(json_formatted_str)
