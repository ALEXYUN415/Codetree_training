arr = list(map(int, input().split()))

even = arr[::2]
odd = arr[1::2]

if sum(even) >= sum(odd):
    print(sum(even) - sum(odd))
else:
    print(sum(odd) - sum(even))

