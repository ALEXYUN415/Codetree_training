arr = list(map(int, input().split()))

even = arr[1::2]   
three = arr[2::3]  

print(f"{sum(even)} {sum(three) / len(three):.1f}")