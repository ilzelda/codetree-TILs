N = int(input())
red = [0]
blue = [0]

for _ in range(2 * N):
    r, b = map(int, input().split())
    red.append(r)
    blue.append(b)

# Please write your code here.
INT_MIN = (1<<30) * -1
dp = [ [INT_MIN] * (N+1) for _ in range(2*N +1) ] # i번째까지ㅏ j개의 빨간색을 선택했을 때 최대 합 
dp[0][0] = 0


for i in range(1, 2*N + 1):
    for j in range(1, N+1):
        dp[i][j] = max(dp[i-1][j-1] + red[i], dp[i-1][j] + blue[i], dp[i][j])

for row in dp:
    for n in row:
        print(f"{n:2d}" if n >=0 else ' X' , end= ' ')
    print()

print(dp[-1][-1])
