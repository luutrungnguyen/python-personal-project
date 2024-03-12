import requests
import json

fp=open('tv_aps_serial.txt','r+')
lines=fp.readlines()

for i in range(0,len(lines)):
    serial=lines[i].split(",")[0]

    url = "https://api.meraki.com/api/v1/devices/"+serial

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": "124ba22065f49b42515c3fb34931f29c900a70f2"
    }

    response = requests.request('GET', url, headers=headers, data = payload)
    #print(response.text.encode('utf8'))
    json_data = response.text.encode('utf8')
    json_object = json.loads(json_data)
    f=open('log_ap_infor.txt', 'w')
    json_formatted_str = json.dumps(json_object, indent=2)
    f.write(json_formatted_str)
    f.close()

    print(json_formatted_str)

