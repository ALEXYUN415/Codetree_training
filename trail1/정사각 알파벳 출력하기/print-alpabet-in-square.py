n = int(input())
# A => 65
cnt = "A"
for _ in range(n):
    for _ in range(n):
        print(cnt, end = "")
        cnt = chr(ord(cnt) + 1)
        
    print()