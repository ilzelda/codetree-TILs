N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)

# Please write your code here.
dp = [-1 for _ in range(M+1)] #무게가 i일때 최대 가치
dp[0] = 0

for i in range(1, M+1):
    for j in range(N):
        before = i-w[j]
        if before < 0 : continue

        dp[i] = max(dp[i], dp[before] + v[j])

print(max(dp))
        