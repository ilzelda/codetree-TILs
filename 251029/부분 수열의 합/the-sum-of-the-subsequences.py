N, M = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
memo = [ [-1]*(M+1) for _ in range(N) ] # -1 : none 0 : false 1: true

def recur(i, val):
    global memo
    
    if val < 0 : 
        return 0
    
    if i >= N:
        if val == 0 : 
            return 1
        if val > 0 :
            return 0

    if memo[i][val] < 0:
        # 포함
        res1 = recur(i+1, val-A[i])

        # 미포함
        res2 = recur(i+1, val)
    
        memo[i][val] = 1 if res1 == 1 or res2 == 1 else 0

    return memo[i][val]

ans = recur(0, M)
res = "Yes" if ans == 1 else "No"
print(res)