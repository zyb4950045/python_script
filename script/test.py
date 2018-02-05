import mysql.connector
import os

user = 'root'
password = None
host = 'localhost'
port = 3306
database = 'test'
conn = mysql.connector.connect(user=user, password=password, host=host, port=port, database=database)
cursor = conn.cursor()
query = 'select * from fireworkmv_svapp_bgm'
cursor.execute(query)
result = cursor.fetchall()
musicPath = r"D:\download\fireworkmv\music"
coverPath = r"D:\download\fireworkmv\cover\3x"
musicList = os.listdir(musicPath)
coverList = os.listdir(coverPath)
map = {}
try:
    for row in result:
        id = row[0]
        bgm_name = row[1].decode('utf-8')
        bgm_url = row[2].decode('utf-8')
        bgm_author = row[3].decode('utf-8')
        bgm_cover = row[4].decode('utf-8')
        srcMusic = musicPath + "\\" + bgm_name + ".mp3"
        dstMusic = musicPath + "\\" + str(id) + ".mp3"
        srcCover = coverPath + "\\" + bgm_name + ".png"
        dstCover = coverPath + "\\" + str(id) + ".png"
        os.rename(srcMusic, dstMusic)
        os.rename(srcCover, dstCover)
except:
    print(id)






