n = int(input())
ans = 1
for i in range(n):
    a, b = map(int, input().split())
    for j in range(a,b+1):
        ans *= j
    print(ans)
    ans = 1