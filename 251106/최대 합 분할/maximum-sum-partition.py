N = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

# [sumA][sumB]
dp = [ [False]*(sum(arr)+1) for _ in range(sum(arr)+1)]
dp[0][0] = True

for n in arr:
    for i in range(len(dp))[::-1]:
        for j in range(len(dp))[::-1]:

            if i-n >=0 and dp[i-n][j] : dp[i][j] = True # n을 A에 넣음
            if j-n >=0 and dp[i][j-n] : dp[i][j] = True # n을 B에 넣음

            # dp[i][i] = True # C에 넣음

ans = -1

for i in range(len(dp)):
    if dp[i][i] : ans = max(ans, i)

print(ans)

        
