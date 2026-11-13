cnt = 0
sum = 0

while True:
    n = int(input())
    if 20 <= n <= 29:
        sum += n
        cnt += 1
    else:
        print(f"{sum / cnt :.2f}")
        break