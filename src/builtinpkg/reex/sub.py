import re

name = "name:kim"

# 'kim nice to meet you'
hello = re.sub(r'name:(?P<name>[a-z]+)',r'\g<name> nice to meet you',name)
print(hello)


hello = re.sub(r'name:([a-z]+)',r'\1 nice to meet you',name)
print(hello)


king = "He is a king"

print(re.sub("king",lambda m : m.group().upper(), king))

