import mysql.connector

user = 'root'
password = None
database = 'test'

conn = mysql.connector.connect(user=user, password=password, database=database)
cursor = conn.cursor()
query = 'select * from test'

cursor.execute(query)
result = cursor.fetchall()
for row in result:
    id = row[0]
    name = row[1].decode('utf-8')
    print("id=%d,name=%s" %(id, name))
