#!/usr/bin/python
# -*- coding: UTF-8 -*-
from PIL import Image
import os
import sys
"""
  * @author hupc
 * @since 2021/03/25
"""

def photo_size(file_path):
    img = Image.open(file_path)
    imgSize = img.size  # 大小/尺寸
    w = img.width  # 图片的宽
    h = img.height  # 图片的高
    f = img.format  # 图像格式
    return w,h,f

if __name__ == '__main__':
    print("当前路径",os.path.dirname(os.path.realpath(sys.argv[0])))

    path_name=os.path.dirname(os.path.realpath(sys.argv[0]))+os.sep+'photo'#path_name :表示你需要批量改的文件夹
    # print(path_name)
    # path_name1 = "photo"
    # get_path = os.path.dirname(os.path.realpath(sys.argv[0])
    for item in os.listdir(path_name):#进入到文件夹内，对每个文件进行循环遍历
        photo_info = photo_size(path_name+os.sep+item)
        w = photo_info[0]
        h = photo_info[1]
        f = photo_info[2]
        # print(os.path.join(path_name1,item))
        os.rename(os.path.join(path_name,item),os.path.join(path_name,("size_{}_{}_{}".format(w,h,item))))#os.path.join(path_name,item)表示找到每个文件的绝对路径并进行拼接操作
    print("重命名完成......")


