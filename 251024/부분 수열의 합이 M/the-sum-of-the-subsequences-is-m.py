# N, M = map(int, input().split())
# A = list(map(int, input().split()))

# # total일 경우, i까지 일때 길이
# dp = [[-1 for _ in range(N)] for _ in range(M+1)]

# def recur(cur_total, start_i):
#     if start_i == 0:
#         return 1
    
#     if dp[cur_total][start_i] != -1:
#         return dp[cur_total][start_i]

#     for i in range(start_i)[::-1]:
#         dp[cur_total][i] = recur(cur_total-A[i], i-1)
    
#     return dp[cur_total][start_i]
    
# recur(M, N-1)

# for t in dp:
#     print(*t)

# print(min(dp[M]))

# N, M = map(int, input().split())
# A = list(map(int, input().split()))

# ans = 1000
# def accum(start_i, cur_len, cur_total):
#     global ans 
    
#     if cur_total == M:
#         ans = min(cur_len, ans)
#         return
#     elif cur_total > M:
#         return
    
#     for i in range(start_i, N):
#         accum(i+1, cur_len+1, cur_total+A[i])

# accum(0,0,0)

# if ans == 1000: 
#     print(-1)
# else:
#     print(ans)

import sys

N, M = map(int, input().split())

arr = list(map(int, input().split()))
INT_MAX = sys.maxsize

ans = INT_MAX
def recur(cur_total, cur_len, start_i):
    global ans

    if cur_total == M:
        ans = min(ans, cur_len)
        return

    for i in range(start_i+1, N):
        recur(cur_total+arr[i], cur_len+1, i)

recur(0,0,0)
if ans == INT_MAX: ans = -1
print(ans)




