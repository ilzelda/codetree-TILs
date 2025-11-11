N, K = map(int, input().split())
numbers = list(map(int, input().split()))

# Please write your code here.
INT_MIN = (1<<30) * -1

dp = [ [INT_MIN]*(K+1) for _ in range(N+1)] # i번째까지 선택했을 때, j개의 음수 선택상태에서의, 최대합

dp[0][0] = 0

for i in range(1,N+1):
    if numbers[i-1] >= 0:
        for j in range(K+1):
            dp[i][j] = max(dp[i-1][j] + numbers[i-1], numbers[i-1])
    else:
        for j in range(1,K+1):
            dp[i][j] = dp[i-1][j-1] + numbers[i-1]

ans = INT_MIN
for row in dp:
    ans = max(ans, max(row))

# for row in dp : 
#     for n in row:
#         if n == INT_MIN:
#             n = 'X'
#         print(n, end=' ')
#     print()

print(ans)


