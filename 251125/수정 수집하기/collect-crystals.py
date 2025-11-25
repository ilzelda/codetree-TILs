N, K = map(int, input().split())
gems = input()

dp = [ [0] * (K+1) for _ in range(N) ] # j번 이동했을 때 i번째 일때 수집한 수정 개수

# 짝 : L
# 홀 : R

for i in range(N):
    for j in range(K+1):
        if (j % 2 == 0 and gems[i] == 'L') \
            or  (j % 2 == 1 and gems[i] == 'R') :
            grab = 1 
        else :
            grab = 0

        dp[i][j] = max(dp[i][j],
                        dp[i-1][j] + grab)
        
        if j-1 >= 0 :
            dp[i][j] = max(dp[i][j],
                            dp[i-1][j-1] + grab)

print(max(dp[-1]))
        