n = int(input())
count = [0 for _ in range(10)]
arr = list(map(int, input().split()))
for i in arr:
    count[i] += 1

for i in range(1,10):
    print(count[i])



