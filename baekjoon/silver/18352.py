from collections import deque
import sys

input = sys.stdin.readline
N, M, K, X = map(int, input().split())
graphs = [[] for _ in range(N+1)]
for i in range(M):
    fro, to = map(int, input().split())
    graphs[fro].append(to)

visited = [False for _ in range(N+1)]


def BFS(graphs, X, visited, K):
    start = X
    queue = deque([start])
    dis = [0 for _ in range(N+1)]
    city = []

    while queue:
        v = queue.popleft()
        visited[v] = True
        if dis[v] == K: city.append(v)
        for i in graphs[v]:
            if not visited[i]:
                queue.append(i)
                dis[i] = dis[v] + 1
                visited[i] = True
 
    city.sort()
    if city:
        for c in city:
            print(c)
    else: print(-1)
    

BFS(graphs, X, visited, K)




# from collections import deque
# import sys
# input = sys.stdin.readline

# N, M, K, X = map(int, input().split())

# # 그래프 초기화
# graphs = [[] for _ in range(N+1)]
# for _ in range(M):
#     a, b = map(int, input().split())
#     graphs[a].append(b)

# # 방문 및 거리 배열
# distance = [-1] * (N+1)
# distance[X] = 0

# # BFS
# queue = deque([X])
# while queue:
#     v = queue.popleft()
#     for i in graphs[v]:
#         if distance[i] == -1:  # 방문 안했으면
#             distance[i] = distance[v] + 1
#             queue.append(i)

# # K 거리인 도시 수집
# result = [i for i, d in enumerate(distance) if d == K]
# enumerate() : 인덱스와 값(i,d) 같이 반환함

# if not result:
#     print(-1)
# else:
#     result.sort()
#     for city in result:
#         print(city)
