n = int(input())

cnt = 1

for _ in range(n):
    for j in range(n):
        if cnt * 2 >= 10:
            cnt = 1
        print(cnt * 2, end = " ")
        cnt += 1
        
    print()