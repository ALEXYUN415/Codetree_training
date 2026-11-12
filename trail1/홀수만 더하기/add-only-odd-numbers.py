n = int(input())

cnt = 0
for i in range(1,n+1):
    i = int(input())
    if i % 2 == 1 and i % 3 ==0:
        cnt += i
print(cnt)
