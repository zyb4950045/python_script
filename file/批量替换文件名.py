import os

path = r"D:\download\fireworkmv\music"

list = os.listdir(path)
for temp in list:
    array = temp.split(" - ")
    src = path + "\\" + str(temp)
    dst = path + "\\" + array[1]
    os.rename(src, dst)