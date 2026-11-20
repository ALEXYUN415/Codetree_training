n = int(input())
arr = list(map(int, input().split()))
rev = arr[::-1]

for i in range(n):
    if rev[i] % 2 == 0:
        print(rev[i], end = " ")
