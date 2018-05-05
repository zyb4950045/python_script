import pymysql
import random

config = {
    # "host" : "localhost",
    # "port" : 3306,
    "user" : "root",
    "password" : "root",
    "database" : "test"
}

conn = pymysql.connect(**config)
cursor = conn.cursor()
sql = 'INSERT INTO Salary(salary) VALUES(%s)'
param = []
for i in range(0, 100):
    param.append(random.randint(1, 100))
cursor.executemany(sql, param)
conn.commit()

cursor.close()
conn.close()
