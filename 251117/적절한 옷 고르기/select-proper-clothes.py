N, M = map(int, input().split())
clothes = [tuple(map(int, input().split())) for _ in range(N)]
s = [x[0] for x in clothes]
e = [x[1] for x in clothes]
v = [x[2] for x in clothes]

# Please write your code here.
INT_MIN = -(200 * 1000 + 1)
dp = [ [INT_MIN] * N for _ in range(M+1)] #i번째 날 j번째 옷을 골랐을 경우 최대 만족도 
for j in range(N):
    if s[j] == 1 : dp[1][j] = 0

for i in range(2,M+1):
    for j in range(N):
        if not s[j] <= i <= e[j]: continue
        
        for k in range(N):
            dp[i][j] = max(dp[i][j],
                            dp[i-1][k] + abs(v[k]-v[j]))


# for i, row in enumerate(dp):
#     print(f"{i} : ",end='')
#     for n in row:
#         if n<0 : print('  x',end='')
#         else : print(f"{n:3d}", end='')
#     print()

print(max(dp[-1]))

