N, M = map(int, input().split())
arr = list(map(int, input().split()))

INT_MIN = -(1<<30)

# i번째, 숫자가 j일 때, 다른 횟수 k일 때의 최대 유사도
dp = [ [[INT_MIN]*(M+1) for _ in range(5)] for _ in range(N) ] 
i0 = dp[0]

for n in range(1,5):
    if n==arr[0]:
        i0[n][0] = 1
    else:
        i0[n][0] = 0

for n in range(1,5):
    if n == arr[0]:
        dp[n][0] = 0

for i in range(1, N):
    for j in range(1,5):
        for k in range(M+1):
            
            for jj in range(1,5):
                # i번째가 i-1번재와 다르고 arr[i]와 같을 때
                if jj!=j and j == arr[i] and k-1>=0:
                    dp[i][j][k] = max(dp[i][j][k],
                                        dp[i-1][jj][k-1] + 1)
            
                # i번째가 i-1번째와 다르고 arr[i]와 다를 때
                if jj != j and j!=arr[i] and k-1>=0:
                    dp[i][j][k] = max(dp[i][j][k],
                                        dp[i-1][jj][k-1])
                        
                # i번째와 i-1번째가 같고  arr[i]와 다를 때
                if jj == j and j!=arr[i]:
                    dp[i][j][k] = max(dp[i][j][k],
                                        dp[i-1][jj][k])
                
                # i번째가 i-1번째와 같고  arr[i]와 같을 때
                if jj == j and j==arr[i]:
                    dp[i][j][k] = max(dp[i][j][k],
                                        dp[i-1][jj][k]+1)    

ans = INT_MIN
for j in range(1,5):
    for k in range(M+1):
        ans = max(ans, dp[-1][j][k])

# for row in dp:
#     print(row)
print(ans)
