from functools import reduce


nums = range(1,11)




net = reduce(lambda acc,cur : acc+cur, nums)

print(net)

