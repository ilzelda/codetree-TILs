N = int(input())

# Please write your code here.
# i번째 날에서, T를 총 j번 받았고, B를 최근 연속으로 k번받았을 때 가능한 경우의 수
dp = [ [[0]*3 for _ in range(3) ]for _ in range(1000+1) ] 
dp[0][0][0] = 1

dp[1][0][0] = 1 # G
dp[1][0][1] = 1 # B
dp[1][1][0] = 1 # T

for i in range(2, N+1):
    for j in range(3):
        for k in range(3):
            # G 추가 
            dp[i][j][0] += dp[i-1][j][k]

            # T 추가
            if j >= 1 : dp[i][j][0] += dp[i-1][j-1][k]

            # B 추가
            if k >= 1 : dp[i][j][k] += dp[i-1][j][k-1]
            


# for i, row in enumerate(dp[:N+1]):
#     print(f'{i} :', row)

ans = 0
for j in range(3):
    for k in range(3):
        ans += dp[N][j][k]

print(ans % (10**9 + 7))

# ans = 0
# cur = []

# def recur(nT):
#     global cur, ans

#     if len(cur) >= 3:
#         BBB = True
#         for i in range(1,4):
#             if cur[-i] != 'B': 
#                 BBB = False
#                 break
#         if BBB : return

#     if nT >= 3 : return

#     if len(cur) == N:
#         ans+=1
#         return

#     for res in ['G','B','T']:
#         cur.append(res)
        
#         if res != 'T' : recur(nT)
#         else : recur(nT+1)

#         cur.pop()

# recur(0)
