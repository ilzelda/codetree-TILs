N = int(input())
coins = [0] + list(map(int, input().split()))

# Please write your code here.
INT_MIN = (1<<30) * -1
dp = [ [-1]*4 for _ in range(len(coins))] # i번째 계단일 때, 지금까지 1계단을 j번 선택했을 때 최대 값

for j in range(4):
    dp[0][j] = 0
dp[1][1] = coins[1]

for i in range(1, len(dp)):
    if i-2 >= 0 : 
        dp[i][0] = dp[i-2][0] + coins[i]
        dp[i][1] = max(dp[i-1][0] + coins[i], dp[i-2][1] + coins[i])
        dp[i][2] = max(dp[i-1][1] + coins[i], dp[i-2][2] + coins[i])
        dp[i][3] = max(dp[i-1][2] + coins[i], dp[i-2][3] + coins[i])

ans = INT_MIN
for step in dp:
    for v in step:
        ans = max(ans, v)

print(ans)