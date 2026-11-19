arr = list(map(int, input().split()))

sum = 0
cnt = 0
for i in range(10):
    if arr[i] == 0:
        break
    elif arr[i] % 2 == 0:
        sum += arr[i]
        cnt += 1
print(cnt, sum)