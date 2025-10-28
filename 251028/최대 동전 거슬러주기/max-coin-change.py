N, M = map(int, input().split())
coins = list(map(int, input().split()))

INT_MIN = (1<<30) * -1
# Please write your code here.
dp = [INT_MIN for _ in range(M+1)] # i금액의 최대 동전개수

dp[0] = 0

# def recur(val):
#     global dp

#     if val < 0 : return -1
#     if dp[val] != -1 : return dp[val]

#     res = 0

#     for c in coins:
#         res = max( res, recur(val-c) + 1)
#     dp[val] = res

#     return res

# print(recur(M))

for i in range(M+1):
    for c in coins:
        j = i-c
        if j < 0 : continue

        dp[i] = max(dp[i], dp[j]+1)
ans = -1 if dp[M] < 0 else dp[M]
print(ans)

# for i in range(M+1):
#     print(f"{i:2d}", end= ' ')
# print()
# for v in dp:
#     print(f"{v:2d}", end = ' ' )
# print()
