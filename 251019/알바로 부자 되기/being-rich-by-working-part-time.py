# Please write your code here.
N = int(input())

class Job:
    def __init__(self, _start, _end, _pay):
        self.start = _start
        self.end = _end
        self.pay = _pay

jobs = []

for _ in range(N):
    s, e, p = map(int, input().split())
    jobs.append(Job(s,e,p))

dp = [ 0 for _ in range(len(jobs))] # i번째 알바까지 고려했을 때 최대 돈
dp[0] = jobs[0].pay

def is_overlapped(j1, j2):
    return j1.start <= j2.start <= j1.end

for i in range(1,len(jobs)):
    d = 1
    while i-d >= 0 and is_overlapped(jobs[i-d], jobs[i]) :
        d+=1
    dp[i] = max(dp[i-1], dp[i-d] + jobs[i].pay)

# print('dp : ', dp)

print(max(dp))
