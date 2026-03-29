import sys
input = sys.stdin.readline
C, N = map(int, input().split())

cities = []
for i in range(N):
    cost, customer = map(int, input().split())
    cities.append((cost, customer))

dp = [float('inf')] * (C + 101)  # 고객 1명당 최대 비용이 100이므로
dp[0] = 0

for i in range(C+101):
    if dp[i] == float('inf'):
        continue
    
    for cost, customer in cities:
        next_customer = i + customer
        if next_customer < len(dp):
            dp[next_customer] = min(dp[next_customer], dp[i]+ cost)

# C명 이상 중에서 최소 비용 찾기
answer = min(dp[C:])
print(answer)




