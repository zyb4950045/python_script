import mysql.connector
user = 'root'
password = None
host = 'localhost'
port = 3306
database = 'test'
conn = mysql.connector.connect(user=user, password=password, host=host, port=port, database=database)
cursor = conn.cursor()
query = 'select * from fireworkmv_svapp_bgm where id = 1'
cursor.execute(query)
result = cursor.fetchall()
map = {}
for row in result:
    id = row[0]
    bgm_name = row[1].decode('utf-8')
    bgm_url = row[2].decode('utf-8')
    bgm_author = row[3].decode('utf-8')
    bgm_cover = row[4].decode('utf-8')
    bgm_time = row[5]
    #bytearray -> string需要utf-8解码
    map[bgm_name] = id
    print(id, bgm_name)
    print(map)



