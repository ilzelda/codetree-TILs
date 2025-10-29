N, M = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
res = False

def recur(i, left, val):
    global res
    
    if i == len(A):
        if val < 0 : 
            return
        if val == 0 : 
            res = True
            return
        return

    # 포함
    left.append(A[i])
    recur(i+1, left, val-A[i])

    # 미포함
    left.pop()
    recur(i+1, left, val)




recur(0, [], M)

ans = "Yes" if res else "No"
print(ans)