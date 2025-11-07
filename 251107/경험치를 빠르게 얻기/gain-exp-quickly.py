N, M = map(int, input().split())
quests = [tuple(map(int, input().split())) for _ in range(N)]

# Please write your code here.
dp = [-1 for _ in range(100*N+1)] # 시간 i일 때 최대 경험치
dp[0] = 0

for q in quests:
    ex, t = q
    for i in range(len(dp))[::-1]:
        if i-t >= 0 : dp[i] = max(dp[i], dp[i-t] + ex)

ans = -1
for t in range(len(dp)):
    if dp[t] >= M : 
        ans = t
        break
# print(dp[:10])
print(ans)
