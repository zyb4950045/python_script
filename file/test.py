import os

path = r"D:\download\fireworkmv\cover\3x"

list = os.listdir(path)
for temp in list:
    src = path + "\\" + temp
    dst = path + "\\" + temp.replace("3x", "")
    print(src, dst)
    os.rename(src, dst)