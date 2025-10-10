N, M = map(int, input().split())
grid = [tuple(map(int, input().split())) for _ in range(N)]

# Please write your code here.
visited = [[False]*M for _ in range(N)]
ans = 0

di = [0, 1]
dj = [1, 0]

def in_range(i,j):
    return 0<=i<N and 0<=j<M

def go(i,j):
    global ans

    if i == N-1 and j==M-1 :
        print(1)
        exit(0)

    for d in range(2):
        ni, nj = i+di[d], j+dj[d]
        
        if not in_range(ni,nj): continue
        if visited[ni][nj] : continue
        if grid[ni][nj] == 0 : continue

        visited[ni][nj] = True
        go(ni,nj)


go(0,0)
print(ans)