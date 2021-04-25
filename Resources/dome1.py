import requests
import os

dict = {
    "message": "操作成功" ,
    "code": 0 ,
    "data": [{
        "id": 1205 ,
        "title": "平安健康" ,
        "description": "" ,
        "smallImage": "http://imgvip.angogotech.net/upfiles/image/20210115/20210115153429_8240.jpg" ,
        "thumbImage": "http://imgvip.angogotech.net/upfiles/image/20210115/20210115153434_7069.jpg" ,
        "foregroundImage": "http://imgvip.angogotech.net/upfiles/image/20210115/20210115153437_1365.jpg" ,
        "backgroundImage": "http://imgvip.angogotech.net/upfiles/image/20210115/20210115153441_5975.jpg" ,
        "templateFile": "http://imgvip.angogotech.net/upfiles/ThemeRAR/20210115/20210115153444_9490.zip" ,
        "highLevel": 1 ,
        "recommend": "0" ,
        "useVersionS": "0" ,
        "useVersionE": "99999999" ,
        "remark": "" ,
        "isEnable": True ,
        "fileVersion": 1 ,
        "bgType": 0 ,
        "currentCategoryId": 140 ,
        "currentCategoryName": "问候" ,
        "locationInCurrentCategory": 32 ,
        "rownum": 33 ,
        "downloadCount": 20814 ,
        "templateFileName": "20210115153444_9490.zip" ,
        "templateFileSize": "1097204" ,
        "collect": False
    } , {
        "id": 1285 ,
        "title": "美丽花环" ,
        "description": "" ,
        "smallImage": "http://imgvip.angogotech.net/upfiles/image/20210319/20210319093457_9181.jpg" ,
        "thumbImage": "http://imgvip.angogotech.net/upfiles/image/20210319/20210319093505_8946.jpg" ,
        "foregroundImage": "http://imgvip.angogotech.net/upfiles/image/20210319/20210319093508_6446.jpg" ,
        "backgroundImage": "http://imgvip.angogotech.net/upfiles/image/20210319/20210319093511_6525.jpg" ,
        "templateFile": "http://imgvip.angogotech.net/upfiles/ThemeRAR/20210319/20210319093514_3712.zip" ,
        "highLevel": 0 ,
        "recommend": "0" ,
        "useVersionS": "0" ,
        "useVersionE": "99999999" ,
        "remark": "" ,
        "isEnable": True ,
        "fileVersion": 1 ,
        "bgType": 0 ,
        "currentCategoryId": 140 ,
        "currentCategoryName": "问候" ,
        "locationInCurrentCategory": 6 ,
        "rownum": 7 ,
        "downloadCount": 31464 ,
        "templateFileName": "20210319093514_3712.zip" ,
        "templateFileSize": "844440" ,
        "collect": False
    }]
}
data = dict["data"]
print(data)
list = []
for i in range(0 , len(data)):
    title = data[i]["title"]
    smallImage_url = data[i]["smallImage"]
    thumbImage_url = data[i]["thumbImage"]
    templateFile_url = data[i]["templateFile"]
    Category_name = data[i]["currentCategoryName"]
    dict = {title: [smallImage_url, thumbImage_url, templateFile_url, Category_name]}
    list.append(dict)
print(list)