N = int(input())
coins = [1,2,5]
# Please write your code here.
dp = [-1 for _ in range(N+1)] # i를 만드는 가짓수

dp[0] = 1
dp[1] = 1
dp[2] = 2 # 0+2, 1+1

for i in range(3,N+1):
    res = 0
    for c in coins:
        before_i = i-c
        if before_i < 0 : continue

        res += dp[before_i]
    dp[i] = res

# print(dp)

print(dp[N])