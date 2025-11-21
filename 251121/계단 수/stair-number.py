N = int(input())

# Please write your code here.
dp = [ [0] * 10 for _ in range(N+1)]  # 길이가 i일 때, 끝 수가 j인 경우 개수

for j in range(10):
    dp[1][j]=1
dp[1][0] = 0

for i in range(2,N+1):
    for j in range(10):
        if j-1 >= 0 : dp[i][j] += dp[i-1][j-1]
        if j+1 < 10 : dp[i][j] += dp[i-1][j+1]

# for row in dp:
#     print(row)

print(sum(dp[-1]) % (10**9 + 7))
