N = int(input())
lines = [tuple(map(int, input().split())) for _ in range(N)]
lines = sorted(lines)

def is_overlap(a, b):
    return a[0] <= b[0] <= a[1] or a[0] <= b[1] <= a[1]

dp = [-1 for _ in range(1001)] # i좌표까지에서 선택할 수 있는 최대 선분 개수

dp[lines[0][1]] = 1

last_line = lines[0]

for cur_line in lines[1:]:
    x1 = cur_line[0]

    max_val = max(dp[:x1])
    val = max(max_val+1 ,1)

    dp[cur_line[1]] = val
    # print(f"{cur_line} - maxval:{max_val}, val:{val}")

# print('dp : ', dp[:lines[-1][1]+1])
print(max(dp))