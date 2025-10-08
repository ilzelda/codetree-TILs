N = int(input())

nums = [-1 for _ in range(N)]
visited = [False for _ in range(N+1)]

# Please write your code here.
def recur(i): # i번째 위치 숫자 선택
    if i >= N:
        for number in nums:
            print(number, end=' ')
        print()
        return

    for n in range(1,N+1)[::-1]:
        if visited[n] : continue

        nums[i] = n
        visited[n] = True
        recur(i+1)
        visited[n] = False


recur(0)