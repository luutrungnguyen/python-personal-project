import requests
import json

fp=open('01_bmt_api.txt','r+')
lines=fp.readlines()

for i in range(0,len(lines)):
    serial=lines[i].split(",")[0]

    url = "https://api.meraki.com/api/v1/devices/"+serial

    payload = '''{
                "serial": "Q2LD-BFXT-RHBM",
                "mac": "98:18:88:40:80:f7",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF6-AP172",
                }'''

    headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Cisco-Meraki-API-Key": "124ba22065f49b42515c3fb34931f29c900a70f2"
        }

    response = requests.request('PUT', url, headers=headers, data = payload)
    #print(response.text.encode('utf8'))
    json_data = response.text.encode('utf8')
    json_object = json.loads(json_data)
    f=open('log_ap_infor.txt', 'w')
    json_formatted_str = json.dumps(json_object, indent=2)

    print(json_formatted_str)