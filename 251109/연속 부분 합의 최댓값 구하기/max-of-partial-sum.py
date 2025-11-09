N = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
INT_MIN = (1<<20) * -1

dp = [INT_MIN for _ in range(len(arr))] # i가 마지막일 때 최대 
dp[0] = arr[0]

for i in range(1, len(dp)):
    dp[i] = max(dp[i-1] + arr[i], arr[i])

print(max(dp))
