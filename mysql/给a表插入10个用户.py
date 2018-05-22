import pymysql
import random

config = {
    # "host" : "localhost",
    # "port" : 3306,
    "user" : "root",
    "password" : "root",
    "database" : "test",
    "charset" : "utf8"
}

conn = pymysql.connect(**config)
cursor = conn.cursor()
sql = 'INSERT INTO a(name) VALUES(%s)'
param = []
for i in range(0, 10):
    param.append(chr(97 + i))
cursor.executemany(sql, param)
conn.commit()

cursor.close()
conn.close()
