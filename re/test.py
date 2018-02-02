import re

str = 'Agent Alice told Agent Carol that Agent \
Eve knew Agent Bob was a double agent.'
Regex = re.compile(r'Agent (\w)\w*')
print(Regex.findall(str))
res = Regex.sub(r'\1****', str)
print(res)