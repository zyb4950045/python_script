import re
def strip(source, char=None):
    if None == char:
        reg = re.compile(r'^ *| *$')
    else:
        #这是匹配的char
        #reg = re.compile(r'^[char]*|[char]*$')
        #需要专门拼接字符串
        reg = re.compile(r'^[' + char + ']*|[' + char + ']*$')
    print(r'^[char]*|[char]*$')
    print(reg.findall(source))
    return reg.sub('', source)

if __name__ == '__main__':
    input = "*****aadad*******adada********"
    print(strip(input, '*'))