import sys
import heapq
input = sys.stdin.readline

N, M, X = map(int, input().split())

INF = 1e8
graph = [[] for _ in range(N+1)]

result = []

for i in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))



def dijkstra(start):
    q = []
    distance = [INF] * (N+1)

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
    
        if distance[now] < dist:
            continue
        
        for next_node, weight in graph[now]:
            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))
    return distance

go_to_x = [0] * (N+1)
for i in range(1, N+1):
    temp = dijkstra(i)
    go_to_x[i] = temp[X]

back_from_x = dijkstra(X)
max = 0

for i in range(1, N+1):
    if go_to_x[i] + back_from_x[i] > max:
        max = go_to_x[i] + back_from_x[i]

print(max)