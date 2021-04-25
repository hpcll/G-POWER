import requests
import os
import json
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



def	get_file_name(file_path):
	(filepath, tempfilename) = os.path.split(file_path)
	(filename, extension) = os.path.splitext(tempfilename)
	file_name = filename + extension
	return file_name,extension


def mkdir(name,file_url,path):
	folder = os.path.exists(path)
	if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
		print("{}不存在".format(Category_name))
		os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
		download_img(name,file_url,path)
	else:
		download_img(name,file_url,path)


def download_img(name,file_url,path):
	r = requests.get(file_url, stream=True)
	file_name = name+get_file_name(file_url)[1]
	print(r.status_code) # 返回状态码
	file_Route = "{}/{}".format(path,file_name)
	if r.status_code == 200:
		open(file_Route, 'wb').write(r.content) # 将内容写入图片
		print("下载完成.....")
		del r


if __name__ == '__main__':
	response = requests.request("GET", url1, headers=headers , data=payload).text
	dict = json.loads(response)
	data1 = dict["data"]
	for i in range(3 , len(data1)):
		id = data1[i]["id"]
		print(type(id))
		url = "http://apiv2.angogotech.net/CutoutTemplate/config/cutoutTemplateList?pageSize=100&pageAnchor=0&categoryId={}&requestAll=true&todayFirst=true".format(id)
		Response = requests.request("GET", url, headers=headers , data=payload).text
		dict = json.loads(Response)
		data = dict["data"]
		for i in range(0 , len(data)):
			try:
				Category_name = data[i]["currentCategoryName"]
				title = data[i]["title"]
				smallImage_url = data[i]["smallImage"]
				thumbImage_url = data[i]["thumbImage"]
				foregroundImage_url = data[i]["foregroundImage"]
				backgroundImage_url = data[i]["backgroundImage"]
				templateFile_url = data[i]["templateFile"]
				# dict = {title: [smallImage_url, thumbImage_url, templateFile_url, Category_name]}
				# list.append(dict)
				path = "{}/{}".format(Category_name,title)
				mkdir("smallImage", smallImage_url, path)
				mkdir("thumbImage", thumbImage_url, path)
				mkdir("foregroundImage", foregroundImage_url, path)
				mkdir("backgroundImage", backgroundImage_url, path)
				mkdir("templateFile", templateFile_url, path)
				print(i)
			except:
				continue





