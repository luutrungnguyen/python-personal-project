import requests
import json

fp=open('bmt_aps_serial.txt','r+')
lines=fp.readlines()

for i in range(0,len(lines)):
    serial=lines[i].split(",")[0]

    url = "https://api.meraki.com/api/v1/devices/"+serial

    payload = '''{
                "serial": "Q2LD-BFXT-RHBM",
                "mac": "98:18:88:40:80:f7",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF6-AP172",
                }
                {
                "serial": "Q2LD-B78Y-TZVU",
                "mac": "98:18:88:40:9a:2f",
                "tags": [ "trungnl-change-name" ],
                "name": "N-VNCFBMTF8-AP173",
                }
                {
                "serial": "Q2LD-FBQA-3HAB",
                "mac": "98:18:88:40:9b:43",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF8-AP169",
                }
                {
                "serial": "Q2LD-HZEB-8FEZ",
                "mac": "98:18:88:40:9b:f3",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF7-AP163",
                }
                {
                "serial": "Q2LD-JWY5-5U6P",
                "mac": "98:18:88:40:9c:23",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF7-AP171",
                }
                {
                "serial": "Q2LD-ZN8J-WR8V",
                "mac": "98:18:88:40:a0:17",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF7-AP150",
                }
                {
                "serial": "Q2LD-8E37-4PZ9",
                "mac": "98:18:88:40:a1:e7",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF8-AP168",
                }
                {
                "serial": "Q2LD-BEJ9-R3Y5",
                "mac": "98:18:88:40:a2:b1",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF7-AP151",
                }
                {
                "serial": "Q2LD-PDFS-BUAN",
                "mac": "98:18:88:40:a5:d3",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF7-AP155",
                }
                {
                "serial": "Q2LD-PNAQ-7BLF",
                "mac": "98:18:88:40:a5:dd",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF7-AP158",
                }
                {
                "serial": "Q2LD-S6YE-G85Q",
                "mac": "98:18:88:40:a6:6f",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF7-AP159",
                }
                {
                "serial": "Q2LD-UL79-QCZY",
                "mac": "98:18:88:40:a7:1d",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF9-AP165",
                }
                {
                "serial": "Q2LD-VWPX-B9BQ",
                "mac": "98:18:88:40:a7:77",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF9-AP164",
                }
                {
                "serial": "Q2LD-57LS-7E3J",
                "mac": "98:18:88:40:a9:8d",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF7-AP161",
                }
                {
                "serial": "Q2LD-BGEB-R6Y3",
                "mac": "98:18:88:40:ab:43",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF9-AP176",
                }
                {
                "serial": "Q2LD-HD4K-KTY9",
                "mac": "98:18:88:40:ac:c5",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF8-AP167",
                }
                {
                "serial": "Q2LD-PQ7H-NYNU",
                "mac": "98:18:88:40:ae:6b",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF8-AP166",
                }
                {
                "serial": "Q2LD-USB5-8V3V",
                "mac": "98:18:88:40:af:bf",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF8-AP170",
                }
                {
                "serial": "Q2LD-YANG-NQ9T",
                "mac": "98:18:88:40:b0:af",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF6-AP156",
                }
                {
                "serial": "Q2LD-5J8Q-DWN5",
                "mac": "98:18:88:40:c2:c7",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF9-AP174",
                }
                {
                "serial": "Q2LD-AXCM-255F",
                "mac": "98:18:88:40:c4:51",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF6-AP160",
                }
                {
                "serial": "Q2LD-XM6R-NGR5",
                "mac": "98:18:88:40:c9:cf",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF9-AP175",
                }
                {
                "serial": "Q2LD-7EZB-48BC",
                "mac": "98:18:88:40:c3:31",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF6-AP152",
                }
                {
                "serial": "Q2LD-H94L-PMY8",
                "mac": "98:18:88:40:9b:bb",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF3-AP183",
                }
                {
                "serial": "Q2LD-JXWC-EFHN",
                "mac": "98:18:88:40:9c:27",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF3-AP178",
                }
                {
                "serial": "Q2LD-Q5S8-S5PQ",
                "mac": "98:18:88:40:a5:fb",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF5-AP154",
                }
                {
                "serial": "Q2LD-CG9G-GP33",
                "mac": "98:18:88:40:ab:89",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF3-AP180",
                }
                {
                "serial": "Q2LD-CYMJ-R5PQ",
                "mac": "98:18:88:40:ab:bb",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF3-AP177",
                }
                {
                "serial": "Q2LD-DAUQ-UQSP",
                "mac": "98:18:88:40:ab:c5",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF3-AP179",
                }
                {
                "serial": "Q2LD-VC4V-KCRE",
                "mac": "98:18:88:40:af:e5",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF3-AP182",
                }
                {
                "serial": "Q2LD-VXF4-CCHW",
                "mac": "98:18:88:40:b0:0d",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF5-AP184",
                }
                {
                "serial": "Q2LD-C7MP-5CWG",
                "mac": "98:18:88:40:ab:73",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF6-AP162",
                }
                {
                "serial": "Q2LD-VSD3-T6AX",
                "mac": "98:18:88:40:af:fd",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF6-AP157",
                }
                {
                "serial": "Q2LD-NY3N-YLP9",
                "mac": "98:18:88:40:ae:3f",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF1-AP153",
                }
                {
                "serial": "Q2LD-3S2P-HTP3",
                "mac": "98:18:88:40:c2:69",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF1-AP181",
                }
                {
                "serial": "Q2LD-K95M-WZ6M",
                "mac": "98:18:88:4f:d1:e7",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF5-AP185",
                }
                {
                "serial": "Q2LD-CEYW-YZX2",
                "mac": "98:18:88:4f:c7:a9",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF6-AP187",
                }
                {
                "serial": "Q2LD-FX28-9XXM",
                "mac": "98:18:88:4f:c8:7d",
                "tags": ["trungnl-change-name"],
                "name": "N-VNCFBMTF6-AP186",
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