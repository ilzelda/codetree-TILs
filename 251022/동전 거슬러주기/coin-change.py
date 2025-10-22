

# dp = [-1 for _ in range(10001)] # i원을 거슬러줄 때 최소 동전 개수
# # dp[0] = 0
# # for c in coin:
# #     dp[c] = 1

# def recur(money): #  i원을 거슬러줄 때 최소 동전 개수
#     if money == 0: # base
#         return 0
#     elif money < 0 : 
#         return 1<<30

#     if dp[money] != -1 : 
#         return dp[money]

#     res = 1<<30
    
#     for i in range(N):
#         num = recur(money - coin[i]) + 1
#         res=min(res,num)

#     dp[money] = res
    
#     return dp[money]

# print(recur(M))

# dp = [1<<30 for _ in range(10001)] # i원을 거슬러줄 때 최소 동전 개수
# dp[0] = 0
# for c in coin:
#     dp[c] = 1

# for m in range(M+1):
#     for i in range(N):
#         if m-coin[i] < 0 : continue

#         if dp[m-coin[i]] != -1 :
#             dp[m] = min(dp[m], dp[m-coin[i]] + 1)

# # print(*dp[:M])
# if dp[M] != 1<<30:
#     print(dp[M])
# else :
#     print(-1)

N, M = map(int, input().split())
coin = list(map(int, input().split()))

dp = [1<<30 for _ in range(M+1)] # i원을 만들 수 있는 최소 동전개수

dp[0] = 0
for c in coin:
    dp[c] = 1

def recur(_coin):
    if _coin < 0:
        return 1<<30
    if dp[_coin] != 1<<30:
        return dp[_coin]

    res = 1<<30
    for c in coin:
        res = min(res, recur(_coin-c) + 1)

    dp[_coin] = res
    
    return dp[_coin]


ans = recur(M) 
ans = -1 if ans == 1<<30 else ans
print(ans)
