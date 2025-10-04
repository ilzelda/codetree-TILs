N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
dp = [ [-1] * N for _ in range(N) ]

# init
dp[0][N-1] = grid[0][N-1]

for i in range(1,N):
    dp[i][N-1] = grid[i][N-1] + dp[i-1][N-1]

for j in range(N-1)[::-1]:
    dp[0][j] = grid[0][j] + dp[0][j+1]


# bottom-up
for i in range(1,N):
    for j in range(N-1)[::-1]:
        dp[i][j] = min(grid[i][j] + dp[i-1][j], grid[i][j] + dp[i][j+1])

print(dp[N-1][0])
