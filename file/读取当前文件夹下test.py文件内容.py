#coding=utf-8
import os
path = os.getcwd()
file = open(path + '/' + 'test.py')
content = file.read()
print content
file.close