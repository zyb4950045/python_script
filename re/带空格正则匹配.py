#coding=utf-8
import re

Regex = re.compile(r'abc(\d{3})(\s{3})')
'''
空格ascii码32，看着转义吧，不行就直接上 
r"adhajkdhaabc123   fabcdaf"
'''
res = Regex.search("adhajkdhaabc123\x20\x20\x20fabcdaf")
print res.group(2)

