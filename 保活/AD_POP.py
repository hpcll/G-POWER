#coding:utf-8
import re
import subprocess
import os
import datetime
import time
import uiautomator2 as u2


def time_format_change(timeStamp,hours):
    """时间转换"""
    dateArray = datetime.datetime.utcfromtimestamp(timeStamp)#将手机上的时间戳转为datetime格式
    print(dateArray)
    BJTIME = dateArray + datetime.timedelta(hours=8+hours)#将时间转为北京时间
    print(BJTIME)
    AndroidTime = BJTIME.strftime("%m%d%H%M%Y")#将时间转换为Android支持的格式
    # print(BJTIME)
    return AndroidTime,BJTIME


def Change_Android_time(AndroidTime):
    """更改手机系统时间"""
    cmds = [
        "su",
        "date "+AndroidTime,
        "exit",#这是是非常关键的，退出
    ]
    obj = subprocess.Popen("adb shell", shell= True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    info = obj.communicate(("\n".join(cmds) + "\n").encode('utf-8'))
    for item in info:
        if item:
            print(item.decode('gbk'))

def get_Android_time():
    """获取手机系统时间"""
    date = os.popen("adb shell echo $EPOCHREALTIME").read()  # 拿到手机的当前时间   时间戳
    timeStamp = int(date.split('.', 1)[0])  # 以空格为分隔符，分隔成两个
    print(timeStamp)
    return timeStamp


def Screenshots(name):
    """"截图"""
    # d.press("home")  # 回home页
    # d.press("power")  # 开启屏幕
    # d.swipe_ext("up")
    # time.sleep(1)
    # os.popen('adb shell input text "0122"')
    # time.sleep(4)
    d.screenshot(name+".png")
    print("截图完成")
    time.sleep(2)



if __name__ == '__main__':
    print("请输入正整数")
    first_app = int(input("首次安装多久后进行弹窗？（单位小时）\n"))
    gap_time = int(input("间隔多久进行一次弹窗？（单位小时）\n"))
    num = int(input("每天弹几次？\n"))#连接手机
    d = u2.connect()
    print(d.info)
    # d.app_start("com.photoeditor.creationphoto")#创意P图
    # d.app_start("com.gpowers.imagesizer")#piczoo
    d.app_start("com.images.albummaster")#万能美图
    i = 1
    a = 1
    b = 1
    while i < num:
        timeStamp = get_Android_time()
        tfc = time_format_change(timeStamp, first_app)
        AndroidTime = tfc[0]
        file_name = str(tfc[1]).replace(":", "-", 2)
        print("AndroidTime:" + AndroidTime)
        Change_Android_time(AndroidTime)
        print("第{}次修改时间完成".format(i))
        d.app_start("com.android.settings")
        d.press("home")
        i = i + 1
        if d(text="广告").wait(timeout=10):
            print("第{}次拉倒广告".format(a))
            Screenshots(str(file_name))
            a = a + 1
        else:
            print("第{}次未拉倒广告".format(b))
            b = b + 1
    print("本次共拉取广告从次数{}次".format(i))
    print("其中拉取到广告的次数{}次".format(a))
    print("其中未拉取到广告的次数{}次".format(b))


