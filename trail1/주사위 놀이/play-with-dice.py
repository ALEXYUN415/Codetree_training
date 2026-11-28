count = [0] * 7

arr = list(map(int, input().split()))

for i in arr:
    count[i] += 1

count_arr = [0] * 7


for i in range(1, 7):
    cnt = count[i]
    print(f"{i} - {cnt}")
