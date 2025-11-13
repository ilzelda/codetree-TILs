N, M = map(int, input().split())
nums = [0] + list(map(int, input().split()))

# Please write your code here.
INT_MIN = (1<<30) * -1
dp = [ [0]*41 for _ in range(N+1)] # i번째숫자까지 계산했을 때 결과가 j일때 가지수
dp[0][0+20] = 1

for i in range(1, N+1):
    for j in range(-20, 21):
        
        # 이전에서, nums[i]를 더해서 될 수 있음
        if -20 <= j-nums[i] <= 20: 
            if dp[i-1][j-nums[i]+20] >= 1:

                dp[i][j+20] += dp[i-1][j-nums[i]+20] 

        # 이전에서, nums[i]를 빼서 될 수 있음
        if -20 <= j+nums[i] <= 20: 
            if dp[i-1][j+nums[i]+20] >= 1:

                dp[i][j+20] += dp[i-1][j+nums[i]+20] 

# for j in range(-20, 21):
#     print(f"{j:3d}", end='')
# print()

# for row in dp:
#     for n in row:
#         if n<0: 
#             n = '  x'
#             print(f"{n}", end='')
#         else:
#             print(f"{n:3d}", end='')
#     print()

print(dp[-1][M+20])
