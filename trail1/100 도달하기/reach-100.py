n = int(input())
arr = [1,n]

for i in range(100):
    arr.append(arr[i] + arr[i+1])

    if arr[i] + arr[i+1] > 100:
        break

print(*arr)

