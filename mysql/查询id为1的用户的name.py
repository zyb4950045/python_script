import mysql.connector

config = {
    # "host" : "localhost",
    # "port" : 3306,
    "user" : "root",
    "password" : "root",
    "database" : "test"
}

conn = mysql.connector.connect(**config)
cursor = conn.cursor()
query = "SELECT name FROM user WHERE id = 1"
cursor.execute(query)
for name in cursor.fetchone():
    print(name.decode())
