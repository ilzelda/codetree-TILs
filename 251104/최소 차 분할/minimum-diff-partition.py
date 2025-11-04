N = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
total = sum(arr)

INT_MAX = 1 << 30
ans = INT_MAX

dp = [False for _ in range(1000 * 100 + 1)] # i를 만들 수 있는지

for n in arr:
    dp[n] = True

for i in range(0, len(dp)):
    if dp[i]:
        ans = min(ans, abs(total - (2*i)))

        for n in arr:
            if i+n < len(dp) : dp[i+n] = True

print(ans)




