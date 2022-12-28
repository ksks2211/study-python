import re
target = "<html> <h1>hello</h1> </html>"


# greedy '<html> <h1>hello</h1> </html>'
print(re.findall('<.*>',target))

# lazy '<html>'
print(re.findall('<.*?>',target))


