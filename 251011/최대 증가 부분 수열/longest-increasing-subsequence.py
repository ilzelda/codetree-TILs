# n = int(input())
# arr = list(map(int, input().split()))
# dp = [-1 for _ in range(n)]

# def recur(idx):
#     if dp[idx] != -1 : return dp[idx]

#     cnt = 1

#     for i in range(idx+1,n):
#         if  arr[idx] < arr[i] :
#             cnt = max(cnt, recur(i)+1)
    
#     dp[idx] = cnt
#     return dp[idx]

# ans = 1
# for i in range(n):
#     ans = max(recur(i), ans)

# print(ans)

N = int(input())

nums = list(map(int,input().split()))

dp = [-1 for _ in range(N)]

dp[0] = 1

for i in range(1,N):
    max_dp = -1
    for j in range(i):
        if nums[j] < nums[i] : 
            max_dp = dp[j] if max_dp < dp[j] else max_dp
    
    dp[i] = max_dp + 1 if max_dp > 0 else 1

print(max(dp))