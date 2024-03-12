import requests
url = "https://hnx.vn/ModuleReportStockETFs/Report_MD_PriceVolatilyti/ListData_Listed"
payload = "pOrderType=ASC&pCurrentPage=1&pRecordOnPage=5000&pIsSearch=0&p_keysearch=&pColOrder=col_a"
headers = {
'Content-Type': "application/x-www-form-urlencoded",
'User-Agent': "PostmanRuntime/7.13.0",
'Accept': "*/*",
'Cache-Control': "no-cache",
'Postman-Token': "1b488ef3-e674-4ab3-a915-1f62612094c7,2fa26e21-4932-40b8-881f-924f60069c98",
'Host': "hnx.vn",
'cookie': "language=vi-VN; ASP.NET_SessionId=jf1shzpxc2qvkaw5rqjisjgq",
'accept-encoding': "gzip, deflate",
'content-length': "89",
'Connection': "keep-alive",
'cache-control': "no-cache"
}
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
