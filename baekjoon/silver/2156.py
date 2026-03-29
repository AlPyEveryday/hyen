import sys

input = sys.stdin.readline
n = int(input())

wine = []
for _ in range(n):
    x = int(input())
    wine.append(x)

dp = [0] * n

if n >= 1:
    dp[0] = wine[0]

if n >= 2:
    dp[1] = wine[0] + wine[1]

if n >=3:
    dp[2] = max(dp[1], wine[1]+wine[2], dp[0]+wine[2])

for i in range(3,n):
    # 안마시는 경우
    case1 = dp[i-1]

    # i, i-1번째 마시는 경우
    case2 = wine[i]+wine[i-1] + dp[i-3]

    # i, i-2번째 마시는 경우
    case3 = wine[i]+dp[i-2]

    dp[i] = max(case1, case2, case3)

print(dp[n-1])

