N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

nums = [0 for _ in range(N)]
choosed = []
ans = -1
# Please write your code here.
def recur(row): # row번째에서 선택
    global ans

    if row >= N:
        res = sum(nums)
        # print(f'{nums}->{res}')
        ans = res if res > ans else ans
        return
    
    for j in range(N):
        if j in choosed: continue

        choosed.append(j)
        nums[row] = grid[row][j]
        recur(row+1)
        choosed.pop()

recur(0)
print(ans)