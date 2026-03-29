from collections import deque

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
S, T = map(int, input().split())

adj = [[] for _ in range(n+1)]
res_adj = [[] for _ in range(n+1)]

for ex, ey in edges:
    adj[ex].append(ey)
    res_adj[ey].append(ex)

fromS = [False] * (n+1) # S에서 가는것
toT = [False] * (n+1) # T로 들어올 수 있는 것 (역그래프)
fromT = [False] * (n+1)
toS = [False] * (n+1)

def BFS(start, target, graph, visited):
    q = deque([start])
    visited[start] = True

    while(q) :
        x = q.popleft()
        if x == target:
            continue
        
        for gx in graph[x]:
            if visited[gx] == False:
                visited[gx] = True
                q.append(gx)

BFS(S, T, adj, fromS)
BFS(T, -1, res_adj, toT)
BFS(T, S, adj, fromT)
BFS(S, -1, res_adj, toS)

ans = 0

for i in range(1,n+1):
    if i == S or i == T: continue
    if fromS[i] and toT[i] and fromT[i] and toS[i]:
        ans += 1

print(ans)

