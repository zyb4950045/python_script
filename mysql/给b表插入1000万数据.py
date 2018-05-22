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
sql = 'INSERT INTO b(uid, company, salary) VALUES(%s, %s, %s)'
LEN = int(1E7)
param = []
companyArray = ["百度", "阿里", "腾讯", "美团", "滴滴", "头条", "网易", "京东",
                "新浪", "携程", "搜狐", "搜狗", "小米"]
sz = len(companyArray) - 1
for i in range(0, LEN):
    param.append((random.randint(1, 10), companyArray[random.randint(0, sz)], random.randint(100, 1000)))
cursor.executemany(sql, param)
conn.commit()

cursor.close()
conn.close()
