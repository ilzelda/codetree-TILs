N = int(input())

# Please write your code here.
dp = [ [-1]*3 for _ in range(N) ] # i번째 날에서 T를 j번 받았을 때 가능한 경우의 수
dp[0][0] = 2 # B, G
dp[0][1] = 1 # T

ans = 0
cur = []

def recur(nT):
    global cur, ans

    if len(cur) >= 3:
        BBB = True
        for i in range(1,4):
            if cur[-i] != 'B': 
                BBB = False
                break
        if BBB : return

    if nT >= 3 : return

    if len(cur) == N:
        ans+=1
        return

    for res in ['G','B','T']:
        cur.append(res)
        
        if res != 'T' : recur(nT)
        else : recur(nT+1)

        cur.pop()

recur(0)

print(ans % (10**9 + 7))