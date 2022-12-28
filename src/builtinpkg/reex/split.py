import re


fruits = "apple-banana:orange=kiwi"


print(re.split('[-:=]',fruits))


lyrics = """
all i want for christmas is you
babe
"""

print(re.split(r'\s+',lyrics))