import re


pattern = r'\d+th'

m = re.match(pattern,"  13th")

print(m)


m = re.search(pattern,"   14th")
print(m)