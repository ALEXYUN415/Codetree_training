n = int(input())
nums = list(map(int, input().split()))

arr = [x for x in nums if x % 2 == 0]

for x in arr:
    print(x, end=" ")