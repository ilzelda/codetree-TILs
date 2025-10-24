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

# ans = INT_MAX
# def recur(cur_total, cur_len, start_i):
#     global ans

#     if cur_total == M:
#         ans = min(ans, cur_len)
#         return
#     elif cur_total > M : return

#     for i in range(start_i, N):
#         recur(cur_total+arr[i], cur_len+1, i+1)

# recur(0,0,0)
# if ans == INT_MAX: ans = -1
# print(ans)

dp = [INT_MAX for _ in range(M+1)] # 합이 i일 때 최소길이
dp[0]=0

for i in range(N):
    for j in range(M,-1,-1):
        if arr[i] <= j:
            dp[j] = min(dp[j], dp[j-arr[i]]+1)

ans = dp[M] if dp[M] != INT_MAX else -1
print(ans)



# MAX_ANS = 101

# # 변수 선언 및 입력:
# n, m = tuple(map(int, input().split()))
# arr = list(map(int, input().split()))

# # dp[i] : 지금까지 선택한 수들의 합이 i일 때, 
# #         가능한 최소 수열의 길이
# dp = [0] * (m + 1)


# def initialize():
#     # 최소를 구하는 문제이므로, 
#     # 초기에는 전부 MAX_ANS을 넣어줍니다.
#     for i in range(m + 1):
#         dp[i] = MAX_ANS
    
#     # 초기 조건으로
#     # 아직 아무런 수도 고르지 않은 상태를 정의합니다.
#     # 따라서 지금까지 선택한 수들의 합이 0이며
#     # 지금까지 수열의 길이는 0이므로,
#     # dp[0] = 0을 초기 조건으로 설정합니다.
#     dp[0] = 0

   
# initialize()

# # 각 수들을 선택해봅니다.
# for i in range(n):
#     # 합 j를 만들기 위해
#     # i번 원소를 사용한 경우에 대해 갱신을 진행합니다.
#     # 이때 각 원소를 최대 한번씩만 선택하기 위해서는
#     # 포문을 0 -> m이 아닌, m -> 0 방향으로 진행해야만 함에 유의합니다.
#     for j in range(m, -1, -1):
#         if j >= arr[i]:
#             dp[j] = min(dp[j], dp[j - arr[i]] + 1)

# # 합을 정확히 m을 만들었을 때
# # 가능한 최소 수열의 길이 구해야 하므로
# # dp[m]이 답이 됩니다.
# min_len = dp[m]

# # 합 m을 만드는 것이 불가능 할 시, -1을 출력합니다.
# if min_len == MAX_ANS:
#     min_len = -1

# print(min_len)
