N = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.
inc_dp = [0 for _ in range(N)]

inc_dp[0]=1

for i in range(1, N):
    num = sequence[i]
    max_dp = 0

    for j in range(i):
        if sequence[j] < num:
            max_dp = max(inc_dp[j], max_dp)        

    inc_dp[i] = max_dp + 1

ans1 = max(inc_dp)

dec_dp = [ 0 for _ in range(N)]

dec_dp[0]=1

for i in range(1, N):
    num = sequence[i]
    max_dp = 0

    for j in range(i):
        if sequence[j] > num:
            max_dp = max(dec_dp[j], max_dp)

    dec_dp[i] = max_dp + 1

ans2 = max(dec_dp)

def find(subseq):
    dec_dp = [ 0 for _ in range(len(subseq))]

    dec_dp[0]=1

    for i in range(1, len(subseq)):
        num = subseq[i]
        max_dp = 0

        for j in range(i):
            if subseq[j] > num:
                max_dp = max(dec_dp[j], max_dp)

        dec_dp[i] = max_dp + 1

    return max(dec_dp)


dp = [0 for _ in range(N)]
dp[0] = 1

for pivot in range(N-1):
    base = inc_dp[pivot]

    # pivot 이후부터 감소 찾기
    dp[pivot]=find(sequence[pivot+1:])
    # print(f"{sequence[pivot+1:]} : {dp[i]} + {base}")
    dp[pivot] += base

ans3 = max(dp)

# print("inc : ", inc_dp)
# print("dec : ", dec_dp)
# print("dp : ", dp)

print(max(ans1, ans2, ans3))

