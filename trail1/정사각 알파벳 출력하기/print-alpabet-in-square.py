n = int(input())
# A => 65
x = 65
for _ in range(n):
    for _ in range(n):
        print(chr(x), end ="")
        x += 1
    print()