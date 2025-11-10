N = int(input())
first_cards = [0] + list(map(int, input().split()))
second_cards = [0] + list(map(int, input().split()))

# Please write your code here.
INT_MIN = (1<<30) * -1
dp = [[INT_MIN]*(N+1) for _ in range(N+1)] # first가 i이고 second가 j일 때 최대 합
dp[0][0] = 0

for i in range(1, N+1):
    for j in range(1, N+1):
        cur = second_cards[j] if first_cards[i] > second_cards[j] else 0

        # 둘다 버려서 오기
        from_diag = dp[i-1][j-1]+cur 

        # first를 버려서 오기
        from_up = dp[i-1][j] + cur if first_cards[i-1] > second_cards[j] else INT_MIN 

        # second를 버려서 오기
        from_left = dp[i][j-1] + cur if first_cards[i] > second_cards[j-1] else INT_MIN 

        dp[i][j] = max(from_diag, from_up, from_left)


ans = INT_MIN
for row in dp:
    ans = max(ans, max(row))

# print("    ",end='')
# for n in second_cards:
#     print(f"{n:3}", end='')
# print()
# for i, row in enumerate(dp):
#     print(f"{first_cards[i]:3}", end=' ')
#     for j in row:
#         if j<0 : j="  x"
#         print(f"{j:3}",end='')
#     print()

print(ans)