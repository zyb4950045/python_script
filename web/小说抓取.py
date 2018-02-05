import requests
import bs4
import re

url = "http://www.136book.com/linjiajiejieshibasui/"
html = requests.get(url)
# file = open("out.txt", "w+")
soup = bs4.BeautifulSoup(html.text)
element = soup.select("#book_detail")[1].select("a")
# print(content)
# Regex = re.compile("<a href=|</a>")
# for line in element:
#     temp = Regex.sub("", str(line)).split(r'">')
    # file.write(temp[1])




