N = int(input())
s = [0]
b = [0]
for _ in range(N):
    si, bi = map(int, input().split())
    s.append(si)
    b.append(bi)

# Please write your code here.\
INT_MIN = (1<<30) * -1

# 지금까지 앞 i명의 학생을 보며, 축구부에 j명을, 야구부에 k명을 선택했을 때 나올 수 있는 능력의 합의 최대
dp = [ [ [INT_MIN for _ in range(10)] for _ in range(12) ] for _ in range(N+1) ]
dp[0][0][0] = 0

for i in range(1, N+1):
    for j in range(min(i+1,12)):
        for k in range(min(i-j+1,10)):
            dp[i][j][k] = dp[i-1][j][k]

            if j-1 >= 0 : dp[i][j][k] = max(dp[i-1][j-1][k] + s[i], dp[i][j][k])
            if k-1 >= 0 : dp[i][j][k] = max(dp[i-1][j][k-1] + b[i], dp[i][j][k])

print(dp[-1][-1][-1])