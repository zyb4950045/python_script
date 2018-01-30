#coding=utf-8

import mysql.connector

user = 'root'
passwd = None
database = 'test'

connection = mysql.connector.connect(user=user, password=passwd, database=database)
cursor = connection.cursor()
query = 'SELECT * FROM test'
cursor.execute(query)
for id, name in cursor:
    print('id : %s, name : %s' %(id, name))