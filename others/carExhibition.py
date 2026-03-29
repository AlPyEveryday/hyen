from collections import deque

n, m, k = map(int, input().split())

edges = []

for _ in range(m):
    x, y = map(int, input().split())
    edges.append((x - 1, y - 1))

start_points = list(map(lambda x: int(x) - 1, input().split()))


# Please write your code here.
# 간선을 딕셔너리로 표현

dic = {key: [] for key in range(n)}

for ex, ey in  edges:
    dic[ex].append(ey)

ans = [[-1] * k for _ in range(n)]
i = 0

# k번만 반복
for sp in start_points:
    visited = [False for _ in range(n)]
    visited[sp] = True
    q = deque([(sp, 0)])
    ans[sp][i] = 0

    while q:
        s, d = q.popleft()
        if dic[s]:
            for neighbor in dic[s]:
                if visited[neighbor] == False:
                    q.append((neighbor, d+1))
                    visited[neighbor] = True
                    ans[neighbor][i] = d+1
    
    i +=1

max_time = float('inf')
for j in range(n):
    if min(ans[j]) == -1: continue

    if max(ans[j]) < max_time:
        max_time = max(ans[j])

if max_time == float('inf'): print(-1)
else: print(max_time)