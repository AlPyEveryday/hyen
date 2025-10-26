from collections import deque
import sys

input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
        return parent[x]
    else:
        return x

def union(x,y):
    a = find(x)
    b = find(y)

    if a != b: # 대표 노드가 다를 때만 합침
        # size가 작은 트리를 큰 트리 밑으로 붙임
        if size[a] < size[b]:
            parent[a] = b
            size[b] += size[a] # 합쳐진 트리의 크기 갱신
        else:
            parent[b] = a
            size[a] += size[b]
        return True # 합치기 성공
    return False

V, E = map(int, input().split())
edges = []
parent = [0 for _ in range(V+1)]
size = [1] * (V + 1)

for j in range(1, V+1):
    parent[j] = j

for i in range(E):
    a, b, w = map(int, input().split())
    edges.append((w, a, b))

edges.sort()

score = 0
num = 0

for w, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        score += w
        num += 1

        if num == V-1: break

print(score)

