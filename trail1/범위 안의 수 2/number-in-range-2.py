sum = 0
cnt = 0

for i in range(10):
    i = int(input())

    if i >= 0 and i <= 200:
        sum += i
        cnt += 1

print(sum, f"{sum/cnt :.1f}")