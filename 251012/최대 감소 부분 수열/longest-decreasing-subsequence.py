N = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
dp = [-1 for _ in range(N+1)] # i번째까지 최대 수열 길이

dp[0] = 1

for i in range(1,N):
    max_length = 0
    for j in range(i):
        if nums[j] > nums[i] : 
            max_length = dp[j] if max_length < dp[j] else max_length
    
    dp[i] = max_length + 1


print(max(dp))