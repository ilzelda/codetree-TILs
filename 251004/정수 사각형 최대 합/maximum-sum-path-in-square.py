# n = int(input())
# grid = [list(map(int, input().split())) for _ in range(n)]

# answer = 0

# # bottom up : 지금까지 지나온 것들의 합을 구한 다음 최대값을 구함
# def recur(x,y,total):
#     if x>=n or y>=n : return

#     total += arr[x][y]

#     if x==n-1 and y==n-1:
#         answer = max(answer, total)
#         return
    
#     recur(x+1, y, total)
#     recur(x, y+1, total)

# # 앞으로 갈 수 있는 것들의 최대를 리턴
# def recur1(x,y):
#     if x>=n or y>=n:
#         return -(1<<30)

#     if x==n-1 and y==n-1:
#         return grid[x][y]

#     if dp[x][y] != -1:
#         return dp[x][y]

#     down = recur1(x+1,y) + grid[x][y]
#     right = recur1(x,y+1) + grid[x][y]

#     dp[x][y] =  max(down, right)
#     return dp[x][y]

# dp = [[-1 for _ in range(n)] for _ in range(n)]
# dp[n-1][n-1] = grid[n-1][n-1]

# print(recur1(0,0))


N = int(input())

arr = [ list(map(int, input().split())) for _ in range(N)]
dp = [ [0]*N for _ in range(N) ]

dp[0][0] = arr[0][0]

for i in range(1,N):
    dp[i][0] = dp[i-1][0] + arr[i][0]

for j in range(1,N):
    dp[0][j] = dp[0][j-1] + arr[0][j]


for i in range(1,N):
    for j in range(1,N):
        dp[i][j] = max(arr[i][j] + dp[i-1][j], arr[i][j]+dp[i][j-1])

# for i in range(N):
#     print(dp[i])

print(dp[N-1][N-1])