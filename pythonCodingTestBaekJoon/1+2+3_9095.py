# 9095 1, 2, 3 더하기

import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    dp = [0] * (N + 1) # dp 초기화

    for i in range(1, N+1):
        if i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = 2
        elif i == 3:
            dp[i] = 4
        else:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[N])

# n=1 -> 1 (1개)
# n=2 -> 1+1 / 2 (2개)
# n=3 -> 1+1+1 / 2+1 / 1+2 / 3 (4개)
# n=4 -> 1+1+1+1 / 1+1+2 / 1+2+1 / 2+1+1 / 2+2 / 3+1 / 1+3 (7개)
# n=5 -> 1+1+1+1+1 / 1+1+1+2 [4개] / 1+1+3 [3개] / 2+2+1 [3개] / 2+3 [2개] (13개)
# n=6 -> 1+1+1+1+1+1 / 1+1+1+1+2 [5개] / 1+1+2+2 [6개] / 2+2+2 / 1+1+1+3 [4개] / 1+2+3 [6개] / 3+3 (24개)
