N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
MAX_R = 100
INT_MAX = 1<<30

def solve(lb):
    dp = [ [ INT_MAX for _ in range(N) ] for _ in range(N)]
    nums = [ [-1 ] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            nums[i][j] = grid[i][j] if grid[i][j] >= lb else INT_MAX
    
    dp[0][0] = nums[0][0]
    for i in range(1,N):
        dp[i][0] = max(nums[i][0], dp[i-1][0])
    for j in range(1,N):
        dp[0][j] = max(nums[0][j], dp[0][j-1])
    
    
    for i in range(1,N):
        for j in range(1,N):
            dp[i][j] = max(min(dp[i-1][j], dp[i][j-1]), nums[i][j])


    # if lb==2:
    #     for i in range(N):
    #         print(nums[i])
    #     for i in range(N):
    #         print(dp[i])

    return dp[N-1][N-1]



ans = 99
for lower_bound in range(1,101):
    max_val = solve(lower_bound)
    if max_val == INT_MAX : continue

    ans = min(ans, max_val - lower_bound)

print(ans)
