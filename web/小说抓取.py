import requests
from bs4 import BeautifulSoup
import re
import os
import time

'''
笔趣网爬取小说
'''

#请求头字典
req_header={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cookie':'__cfduid=d577ccecf4016421b5e2375c5b446d74c1499765327; UM_distinctid=15d30fac6beb80-0bdcc291c89c17-9383666-13c680-15d30fac6bfa28; CNZZDATA1261736110=1277741675-1499763139-null%7C1499763139; tanwanhf_9821=1; Hm_lvt_5ee23c2731c7127c7ad800272fdd85ba=1499612614,1499672399,1499761334,1499765328; Hm_lpvt_5ee23c2731c7127c7ad800272fdd85ba=1499765328; tanwanpf_9817=1; bdshare_firstime=1499765328088',
    'Host':'www.qu.la',
    'Proxy-Connection':'keep-alive',
    'Referer':'http://www.qu.la/book/1265/765108.html',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'
}

#小说主地址
req_url_base='http://www.qu.la/book/'
#单独一本小说地址
req_url=req_url_base+"1/"
#某一章页面地址
txt_section='260824.html'

#请求当前章节页面  params为请求参数
r=requests.get(req_url+str(txt_section),params=req_header)
#soup转换
soup=BeautifulSoup(r.text, "html.parser")
#获取章节名称
section_name=soup.select('#wrapper .content_read .box_con .bookname h1')[0]
#获取章节文本
section_text=soup.select('#wrapper .content_read .box_con #content')[0]
#删除无用项
for ss in section_text.select("script"):
    ss.decompose()

#按照指定格式替换章节内容，运用正则表达式
section_text = re.sub( '\s+', '\r\n\t', section_text.text).strip('\r\n')

title = section_name.string
print('章节名:' + title)
print("章节内容：\n" + section_text)
#以二进制读写模式打开小说文件
file = open('out.txt', "ab+")
# 以二进制写入章节题目 需要转换为utf-8编码，否则会出现乱码
file.write(('\r' + title + '\r\n').encode('UTF-8'))
# 以二进制写入章节内容
file.write((section_text).encode('UTF-8'))
#关闭小说文件
file.close()