def get_natural_number(max):
    n = 0
    while True:
        n += 1
        if n <= max:
            yield n
        else:
            return


for i in get_natural_number(10):
    print(i)
