N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

# Please write your code here.
dp = [-1 for _ in range(M+1)] # 무게가 j일때 최대 가치
dp[0] = 0

for i in range(N):
    # i번째 물건을 고려한다
    for j in range(0, M+1)[::-1]:
        
        # i번째 선택
        if j-w[i] >= 0 and dp[j-w[i]] != -1:
            
            dp[j] = max(dp[j], dp[j-w[i]] + v[i])
            
print(dp[M])