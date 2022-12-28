def fibonacci():
    cur,prev = 1,0
    while True:
        yield cur
        cur, prev = cur+prev, cur


f = fibonacci()


for i in range(10):
    print(next(f))