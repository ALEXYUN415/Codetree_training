a , b = 0 , 0

for _ in range(10):
    n = int(input())
    if n % 3 ==0 and n % 5 == 0:
        a += 1
        b += 1
    elif n % 5 == 0:
        b += 1
    elif n % 3 ==0:
        a += 1

print(a, b)
