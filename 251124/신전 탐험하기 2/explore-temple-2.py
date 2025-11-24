N = int(input())

Treasure = [ [0]*3 for _ in range(N+1) ]

for i in range(1, N+1):
    Treasure[i][0], Treasure[i][1], Treasure[i][2] = map(int, input().split())

INT_MIN = -(1<<30)

dp = [ [ [INT_MIN]*3 for _ in range(N+1) ] for _ in range(3) ] # 1층에서 i번째 방을 선택했을 때, j층 에서 k번째 방을 선택했을 때 최대 보물

for i in range(3):
    for k in range(3):
        if i==k : 
            dp[i][1][k] = Treasure[1][k]
        
for i in range(3):
    for j in range(2,N):
        dp[i][j][0] = max( Treasure[j][0] + dp[i][j-1][1], 
                            Treasure[j][0] + dp[i][j-1][2])
        
        dp[i][j][1] = max( Treasure[j][1] + dp[i][j-1][0], 
                            Treasure[j][1] + dp[i][j-1][2])

        dp[i][j][2] = max( Treasure[j][2] + dp[i][j-1][1], 
                            Treasure[j][2] + dp[i][j-1][0])

dp[0][N][1] = max( Treasure[N][1] + dp[0][N-1][0], 
                    Treasure[N][1] + dp[0][N-1][2])
dp[0][N][2] = max( Treasure[N][2] + dp[0][N-1][0], 
                    Treasure[N][2] + dp[0][N-1][2])

dp[1][N][0] = max( Treasure[N][0] + dp[1][N-1][1], 
                    Treasure[N][0] + dp[1][N-1][2])
dp[1][N][2] = max( Treasure[N][2] + dp[1][N-1][1], 
                    Treasure[N][2] + dp[1][N-1][0])

dp[2][N][0] = max( Treasure[N][0] + dp[2][N-1][1], 
                   Treasure[N][0] + dp[2][N-1][0])
dp[2][N][1] = max( Treasure[N][1] + dp[2][N-1][2], 
                    Treasure[N][1] + dp[2][N-1][0])

            

print(
    max(
        max(dp[0][-1]),
        max(dp[1][-1]),
        max(dp[2][-1]),
    )
)