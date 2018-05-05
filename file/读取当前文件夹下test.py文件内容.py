import os
path = os.getcwd()
file = open(path + '/' + '查询id为1的用户的name.py')
list = file.readlines()
for content in list:
    print(content, end='')
file.close()