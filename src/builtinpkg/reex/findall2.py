import re


title = "<title>Hello</title>"

print(re.findall(r'<title>\w+</title>',title))
print(re.findall(r'<title>(\w+)</title>',title))

