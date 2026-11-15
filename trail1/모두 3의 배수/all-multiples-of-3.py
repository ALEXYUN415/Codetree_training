ck = False

for i in range(5):
    n = int(input())
    if n % 3 !=0:
        ck = True
        break

if ck is True:
    print(0)
else:
    print(1)