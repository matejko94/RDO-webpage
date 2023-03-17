import re
p = re.compile(r'\d+')

s = "\u5f20\u6d2a\u6d9b"
m = p.search(s)
print(repr(m.group()))