N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
dp = [[-1]*N for _ in range(N)]
dp[0][0] = grid[0][0]

for i in range(1,N):
    dp[i][0] = max(grid[i][0], dp[i-1][0])

for j in range(1,N):
    dp[0][j] = max(grid[0][j], dp[j-1][0])

for i in range(1,N):
    for j in range(1,N):
        dp[i][j] = max(min(dp[i-1][j], dp[i][j-1]), grid[i][j])

print(dp[N-1][N-1])
