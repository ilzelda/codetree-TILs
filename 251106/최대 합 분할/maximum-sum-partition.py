N = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

# # [sumA][sumB]
# dp = [ [False]*(sum(arr)+1) for _ in range(sum(arr)+1)]
# dp[0][0] = True

# for n in arr:
#     for i in range(len(dp))[::-1]:
#         for j in range(len(dp))[::-1]:

#             if i-n >=0 and dp[i-n][j] : dp[i][j] = True # n을 A에 넣음
#             if j-n >=0 and dp[i][j-n] : dp[i][j] = True # n을 B에 넣음

#             # dp[i][i] = True # C에 넣음

# ans = -1

# for i in range(len(dp)):
#     if dp[i][i] : ans = max(ans, i)

# print(ans)

        
# A-B : -total<=0<=total
#       0 total total*2

from copy import deepcopy

dp = [ -1 for _ in range(2*sum(arr)+1)] # diff i일때 sumA의 값 

offset = sum(arr)
dp[0+offset] = 0 # sumA:0 sumB:0

for n in arr: # n을 고려함
    new_dp = [ -1 for _ in range(2*sum(arr)+1)]

    for d in range(-sum(arr), sum(arr)+1): 
        if dp[d+offset] < 0 : continue

        #diff가 d일때 

        # n을 A에 넣음
        if 0<= d+n+offset < len(dp):
            new_dp[d+n+offset] = max(new_dp[d+n+offset], dp[d+offset] + n)    
        
        # n을 B에 넣음
        if 0<= d-n+offset < len(dp):
            new_dp[d-n+offset] = max(new_dp[d-n+offset], dp[d+offset])    

        # C에 넣음
        new_dp[d+offset] = max(new_dp[d+offset], dp[d+offset])    

    dp = deepcopy(new_dp)

print(dp[0+offset])
