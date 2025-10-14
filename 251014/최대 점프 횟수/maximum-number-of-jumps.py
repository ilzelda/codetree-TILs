N = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
dp = [0 for _ in range(N)] # i번째 까지 왔을 때 최대 점프 횟수
dp[0]=1

for i in range(0,N):
    if dp[i] == 0 : continue

    for d in range(1, arr[i]+1):
        if i+d >= N : break

        dp[i+d] = max(dp[i+d], dp[i]+1)


# print(dp)
print(max(dp)-1)