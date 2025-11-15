N, M = map(int, input().split())
numbers = list(map(int, input().split()))

# Please write your code here.
# 구간을 지금까지 i개 선택했을 때, j번째 까지의 최대합
INT_MIN = (1<<30) * -1
dp = [ [INT_MIN]*(N) for _ in range(M+1)]
for j in range(N):
    dp[0][j] = 0

dp[1][0] = numbers[0]
for j in range(1,N):
    for jj in range(j+1):
        #                       선택하지 않음 
        # print(j," : ",dp[1][j], dp[1][j-1], sum(numbers[jj:j+1]))
        dp[1][j] = max(dp[1][j], dp[1][j-1], sum(numbers[jj:j+1]))

sums = [0 for _ in range(N)]
sums[0] = numbers[0]
for i in range(1,N):
    sums[i] = sums[i-1] + numbers[i]

for i in range(2, M+1):
    for j in range(2*(i-1), min(2*(i-1)+3,N)):
        
        for k in range(j-1):
            for l in range(k+2,j+1):
                dp[i][j] = max(dp[i][j], 
                                dp[i-1][k] + sums[j]-sums[l-1] ) #sum(numbers[l:j+1])

# for row in dp:
#     for n in row:
#         if n < -500 * 1000:
#             print('  x',end='')
#         else:
#             print(f"{n:3d}",end='')
#     print()

print(max(dp[-1]))
        
