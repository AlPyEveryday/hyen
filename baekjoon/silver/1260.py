#N, M, V = map(int, input().split())
N = 4 
M = 5 
V = 1

graph = [[] for _ in range(N)]

print(graph)

graph[0].append(1)
graph[1].append(0)
graph[0].append(2)
graph[2].append(0)
graph[0].append(3)
graph[3].append(0)
graph[1].append(3)
graph[3].append(1)
graph[2].append(3)
graph[3].append(2)

# for _ in range(M):
#     x, y = map(int, input().split())
#     graph[x-1].append(y-1)
#     graph[y-1].append(x-1)

for i in range(N):
    graph[i].sort()

visit = [False] * N
stack = []

def DFS(V, graph, visit):
    visit[V] = True
    print(V+1, end=' ')

    for i in graph[V]:
        if not visit[i]:
            DFS(i,graph, visit)

DFS(V-1, graph, visit)

def BFS(V, graph, visit):
    if visit[V] == False:
        visit[V] = True
        print(V+1, end=' ')

    for i in graph[V]:
        if not visit[i]:
            visit[i] = True
            print(i+1, end=' ')
    
    for i in graph[V]:
        BFS(i, graph, visit)

BFS(V-1, graph, visit)

