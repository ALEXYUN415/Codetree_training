arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] == 0:
        ans = arr[:i]
        break

print(sum(ans[-1:-4:-1]))
