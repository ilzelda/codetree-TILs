N = int(input())
L = [0 for _ in range(N+1)]
M = [0 for _ in range(N+1)]
R = [0 for _ in range(N+1)]

for i in range(1,N+1):
    L[i], M[i], R[i] = map(int, input().split())

dp = [[-1] * 3 for _ in range(N+1)] # i층 j번째 방에서 최대 보물 수

for j in range(3):
    dp[0][j] = 0

# 0:L 1:M 2:R
for i in range(1,N+1):
    dp[i][0] = max(dp[i-1][1] + L[i],
                    dp[i-1][2] + L[i])

    dp[i][1] = max(dp[i-1][0] + M[i],
                    dp[i-1][2] + M[i])
                    
    dp[i][2] = max(dp[i-1][0] + R[i],
                    dp[i-1][1] + R[i])

print(max(dp[-1]))