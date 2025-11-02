N = int(input())
profit = list(map(int, input().split()))
profit = [0] + profit
# Please write your code here.
dp = [ -1 for _ in range(N+1)] # 길이가 i 일때 최대 수익
dp[0] = 0
for i in range(1,N+1):
    dp[i] = profit[i]

for i in range(2, N+1):
    for j in range(i):
        dp[i] = max(dp[i], dp[i-j] + profit[j])

print(dp[N])
