N = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
total = sum(arr)

dp = [False for _ in range(total+1)] # sumA=i를 만들 수 있는가
dp[0]= True

for n in arr:
    for i in range(len(dp))[::-1]:
        if i-n >=0: dp[i] = True if dp[i-n] else False

if total % 2 != 0 : ans = "No"
else:
    if dp[int(total/2)] : ans = "Yes" 
    else : ans = "No"

print(ans)



