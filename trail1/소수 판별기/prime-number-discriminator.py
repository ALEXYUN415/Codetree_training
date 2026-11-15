n = int(input())

ck = False

for i in range(2,n):
    if n % i == 0:
        ck = True
        break

if ck is True:
    print("C")
else:
    print("P")