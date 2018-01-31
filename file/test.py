#coding=utf-8
import os

path = os.getcwd()
# r'\' 是一个大坑，r避免以\结尾
sep = '\\'
print sep
print path.split(sep)
print os.path.realpath(path)
path = "D:\资料\技术资源\编程语言\python".decode("utf-8");
list = os.listdir(path)
for file in list:
    # 获取文件字节
    print os.path.getsize(path + '/' + file) / 1024
    print file
