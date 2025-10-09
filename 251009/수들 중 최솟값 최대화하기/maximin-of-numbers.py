N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
is_choosed_col = [False for _ in range(N)]
choosed = []
ans = -1

def recur(row): # row행에서 칠하기
    global ans

    if row == N:
        min_num = 10000
        for i in range(N):
            j = choosed[i]
            min_num = grid[i][j] if grid[i][j] < min_num else min_num
        
        ans = min_num if min_num > ans else ans
        return

    for col in range(N):
        if is_choosed_col[col] : continue

        is_choosed_col[col] = True
        choosed.append(col)
        recur(row+1)
        choosed.pop()
        is_choosed_col[col] = False

recur(0)
print(ans)