n = int(input())

for i in range(n):          # i: 행 (0부터 n-1까지)
    for j in range(n):      # j: 열 (0부터 n-1까지)
        # 1) 첫 번째 줄(i == 0)이거나
        # 2) 홀수 열(j % 2 == 1)이면서 행이 열 이하(i <= j)일 때 별 출력
        if i == 0 or (j % 2 == 1 and i <= j):
            print("* ", end="")
        else:
            print("  ", end="")  # 별이 아닌 자리는 공백 2칸으로 줄 맞추기
    print()