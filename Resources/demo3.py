import requests
import json
url = "http://apiv2.angogotech.net/CutoutTemplate/config/cutoutTemplateList?pageSize=100&pageAnchor=0&categoryId=1&requestAll=true&todayFirst=true"
url1 = "http://apiv2.angogotech.net/CutoutTemplate/category/allCutoutTemplateCategory"
payload={}
headers = {
    'traceid': 'a4e33b09-e878-4801-843d-c699fa1bc32f',
    'appType': 'android',
    'appVersionCode': '341',
    'deviceType': 'MI 4LTE',
    'deviceSystemVersion': '6.0.1',
    'language': 'zh_CN',
    'userName': '4b4a50f3-4cbd-4c78-a6d1-14818b504dca',
    'cookie':'',
    'channel':'10012190',
    'requestTime': '1619336632232',
    'initialOnlineTime': '1619323063000',
    'userType': '1',
    'Accept-Encoding': 'gzip',
    'User-Agent': '',
    'Connection': ''
}




response = requests.request("GET", url1, headers=headers, data=payload).text
dict = json.loads(response)
print(dict)
data = dict["data"]
for i in range(3, len(data)):
    id = data[i]["id"]
