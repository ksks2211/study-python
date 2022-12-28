import re

sample1 = "gray"
sample2 = "grey"


pattern1 = re.compile('gray|grey')


print(pattern1.match(sample1))
print(pattern1.match(sample2))

pattern2 = re.compile('gr(a|e)y')

print(pattern2.match(sample1))
print(pattern2.match(sample2))
