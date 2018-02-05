import os
path = os.getcwd()
file = open(path + '/' + 'test.py')
list = file.readlines()
for content in list:
    print(content, end='')
file.close()