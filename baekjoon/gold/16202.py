import sys
from collections import deque

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
        return parent[x]
    return x

def union(x, y):
    a = find(x)
    b = find(y)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

input = sys.stdin.readline
N, M, K =map(int, input().split())

nodes = [[] for _ in range(M)]
parent = [0 for _ in range(N+1)]
result = []

for k in range(1, N+1):
    parent[k] = k

for i in range(1, M+1):
    x, y = map(int, input().split())
    nodes[i-1].append(x)
    nodes[i-1].append(y)

weight = deque(range(1, M + 1))

for _ in range(K):
    parent = [k for k in range(N + 1)]
    score = 0
    edges_count = 0

    for w in weight:
        x = nodes[w-1][0]
        y = nodes[w-1][1]
        if find(x) != find(y):
            union(x, y)
            score += w
            edges_count += 1

            if edges_count == N - 1:
                break
    
    if edges_count != N-1: score = 0
    result.append(score)
    weight.popleft()

print(' '.join(map(str,result)))

