N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
dp = [ [-1] * M for _ in range(N)] # i,j 까지 왔을 때 최대 점프 횟수를 저장
dp[0][0] = 1

for i in range(1,N):
    for j in range(1, M):
        num = grid[i][j]

        for si in range(i):
            for sj in range(j):
                if grid[si][sj] < num :
                    dp[i][j] = max(dp[i][j], dp[si][sj] + 1)

# for row in dp:
#     print(row)

ans = -1
for row in dp:
    ans = max( ans, max(row) )
print(ans)
