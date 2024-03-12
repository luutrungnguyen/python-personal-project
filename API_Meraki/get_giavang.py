import requests
from bs4 import BeautifulSoup
import codecs
import json
import pandas as pd

import xlsxwriter

def api():
    url = 'https://tygia.com/json.php?ran=0&rate=0&gold=1&bank=VIETCOM&date=now'
    # Search GitHub's repositories for requests
    resp = requests.get(url)
    #print(resp.content.decode('utf-8'))
    resp.encoding='utf-8-sig'
    content = resp.text.encode().decode('utf-8-sig')
    return json.loads(content)
a = api()
#print(a)
#print(a["golds"])
b = a["golds"]
#print(type(b[0])) => dict
c = b[0]
#print(c['value'])
d = c['value']
#print(type(d))
#print(d)
#print(e)
for i in d :
    #print(i)
    print ("Gia Mua :  {0}  Giá bán:{1} , Loại Vàng : {2} , Cập nhật lúc {3} tại {4}".format(i['buy'],i['sell'],i['type'],i['updated'],i['brand']))
