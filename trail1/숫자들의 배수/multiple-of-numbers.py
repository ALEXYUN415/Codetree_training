n = int(input())

cnt = 0
i = 1
while cnt < 2:
    a = n * i
    i += 1
    print(a, end = " ")
    if a % 5 == 0:
        cnt += 1