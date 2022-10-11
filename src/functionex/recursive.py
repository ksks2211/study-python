from math import nan


def factorial(x):
    if x < 0:
        return nan
    elif x <= 1:
        return 1
    return x * factorial(x - 1)


result = factorial(10)

print(result)
