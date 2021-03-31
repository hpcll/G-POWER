#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import re
import datetime

APP_ID = 'ftypf1u62io0'    #"f42v8gzqgsg0"      #APP的应用识别码
Device_ID = '64FD50D7-D803-41F2-BB61-7B5ACDD1FC76' #"A8888356-ADF6-4EEA-AA7C-D036D932A5ED"


# 所有事件获取数据url
url = "https://api.adjust.com/dashboard/api/apps/" + str(APP_ID) + "/event_types?include_archived=false"      #APP对应的所有adjust事件页面URL
cookieString = 'amplitude_id_223be679c0cb3083b6d33145fe356802adjust.com=eyJkZXZpY2VJZCI6ImUzNmUzODcxLTJlYmYtNDQyYS1iNjkyLWRkYjY1N2IwZDQ2MFIiLCJ1c2VySWQiOiI3MTgwMCIsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU2NzU3NzA5MDEzMSwibGFzdEV2ZW50VGltZSI6MTU2NzU3NzY3NTY1NCwiZXZlbnRJZCI6NDgsImlkZW50aWZ5SWQiOjQzLCJzZXF1ZW5jZU51bWJlciI6OTF9; _production_adjust_session=Y1pVYjVrQ2lnL2ZrUTNvN3ZvWmt5bGc4NDltR3IvSjM4QklMOWJDMG9vZ1E2bHYrNlJWVTF1WWF2U0gvQTQyK1VSSHU2U2hMckRKY0JjeXhCSzlZWllDMnZZeUJ0ampRaURaQ2hMLy9IOUViNWpTL3hwd3liREpuZGpCeWZCSEp3QjB0b1RDWFVaWUlZSjFhSW5IZjYvUktUOS9OVGhvYmR2WGg1S1Jtd1FLenp0VGU1NmpLV09hUXhTeWR3RVRBKzJlTlNoRlM2dEJJclpUbTUrVTNkS1AxZVh4cExkeWVMakJYYVNHSk1JWDVWZThiVXF2ZkxrSU43ZVpkb1F5b1E2a1c3UzZvM2tPZ1dUd1UydUN2Y1Zid2FOUlZTdGJ2dzBiM2dUdGp1WW5wdjlpYzFOTlEwdkI1bXNsUTJ1K0YtLUFvU1dzMEtuN1pIN29ta0xhSTFuREE9PQ%3D%3D--ca0733a6f50cfa5f9210101e33ad04bd25c7b2d3'     #识别url必须的headers，不一定都是cookie，当前adjust页面使用cookie
# 测试控制台获取数据url
url_console = "https://api.adjust.com/device_service/api/v1/inspect_device?advertising_id=" + str(Device_ID) + "&app_token=" + str(APP_ID) + "&format=json"      #APP对应的所有adjust事件页面URL
cookieString_console = '_ga=GA1.2.592541789.1567578479; _gid=GA1.2.1665774288.1567578479; _mkto_trk=id:108-GAZ-487&token:_mch-adjust.com-1567578479108-67673; amplitude_id_223be679c0cb3083b6d33145fe356802adjust.com=eyJkZXZpY2VJZCI6ImUzNmUzODcxLTJlYmYtNDQyYS1iNjkyLWRkYjY1N2IwZDQ2MFIiLCJ1c2VySWQiOiI3MTgwMCIsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU2NzU5Mjk5NjQ5MiwibGFzdEV2ZW50VGltZSI6MTU2NzU5NDM1MDEzMSwiZXZlbnRJZCI6NTMsImlkZW50aWZ5SWQiOjQ0LCJzZXF1ZW5jZU51bWJlciI6OTd9; _production_adjust_session=eWR1NnoxOWdUaEhldTludXRSdDN0RWI3VGJMa0hsM3Q4MThqT3BXZXhob0NZeDExa01BdXBNWHdhODZnVEt0WWIwT1o3VHcxdUJBQUZaZTlTcm9OOENVenlITjdUNWEzQjdhTXhZRjVwUm9CLy90TSt3eDNUTGFZSlpSandoeHV3clY5NGxjMnh4ZnBCMm8yM0h6a0JSczdySU1GV3pKbTlLeDJJeTZ5RHNqZUxoZWtuSWN1Y0JlZkowOTc3bHd2NDFmUGNEb3QwcWdiTmtQY3kwMnF3dGpPdU45SFJzWFJwWk1TeXJQZk5PZ3RUSDRKRG1NT3haQzQwVVF0TkRFOGlZK1hGVnQvRkUxVUFMZGxnc0xCS3NRcVlTemZNNGh3dDh5ZzdkTDYvMlNnZmFaWFUzajd1eEV2S0dPN2dLTEotLVNuUkZma1ZHaXZYRHRadjV6NFgrWlE9PQ%3D%3D--4a85c248ac63e305ffb1b592c33df1f2f786b6ec'     #识别url必须的headers，不一定都是cookie，当前adjust页面使用cookie
   
#APP需要记录的所有事件
def get_total_event(APP_ID):
    headers = {"Cookie" : cookieString}
    adjust_response = requests.get(url, headers=headers)
    response =  adjust_response.json()
    return response['events']

# 测试控制台实际查出的测试数据
def get_event_from_console(APP_ID,Device_ID):
    headers_console = {"Cookie" : cookieString_console}
    adjust_response_console = requests.get(url_console, headers=headers_console)
    response_console =  adjust_response_console.json()
    return response_console['LastEventTimes']

# 获取系统时间
def isToday(datestr):
    # 2019-09-02T16:31:52Z
    now = datetime.datetime.now()
    logDate = datetime.datetime.strptime(datestr,'%Y-%m-%dT%H:%M:%SZ') + datetime.timedelta(hours=8)
    diff = now - logDate
    if diff.days < 3 :
        return True
    else:
        return False


events = get_total_event(APP_ID)

logEvents = get_event_from_console(APP_ID,Device_ID)        # 测试控制台的数据
successEvents = []
faildEvents = []
for eventInfo in events:
    token = eventInfo['token']
    name = eventInfo['name']
    if token in logEvents:
        logDate = logEvents[token]        # 获取token对应的时间
        if isToday(logDate) :
            successEvents.append((name,token))
        else:
            faildEvents.append((name,token))
    else :
        faildEvents.append((name,token))

print('成功上报的事件:')
for result in successEvents:
    print(result[0] + ':' + result[1])
print('未成功上报的事件:')
for result in faildEvents:
    print(result[0] + ':' + result[1])
