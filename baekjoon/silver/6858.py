import heapq
# 같은 상황이라면 값이 더 작은 걸 택하기 위해서 heapq를 사용 -> 넣을 때마다 가장 작은 수가 제일 앞에 오게 넣기 때문
# deque는 append로 넣는 경우 그냥 뒤에 넣음

N = 7
e = 5

graph =[[] for i in range(N+1)]
indegree =  [0 for i in range(N+1)]
# 문제에서 주어진대로 먼저 넣어두기
graph[1].append(7)
graph[1].append(4)
graph[2].append(1)
graph[3].append(4)
graph[3].append(5)

indegree[7] += 1
indegree[4] += 1
indegree[1] += 1
indegree[4] += 1
indegree[5] += 1

for i in range(10):
    a = int(input()) # input()으로 받으면 문자열임 -> 정수로 변환해줘야함
    b = int(input())
    if a == 0 and b == 0:
        break
    graph[a].append(b) # a-> b 연결 (b전에 a가 와야 함)
    indegree[b] += 1 # b를 향한 화살표 개수 증가 (= b전에 실행 되어야 하는 일의 개수)
    e += 1

for j in range(1, N+1):
    graph[j].sort() # 추후 연결된 노드들 중에서 작은 것부터 큐에 넣기위해 정렬

result = []
q = []

for i in range(1, N+1):
    if indegree[i] == 0: # 선행 노드가 없는 것 먼저 큐에 넣어줌
        heapq.heappush(q, i) # 자동으로 작은 수들이 맨 앞에 오게 정렬하면서 넣음

while q:
    now = heapq.heappop(q) 
    result.append(now) # 큐에 있는 값중 가장 작은 값 (= 더이상 선행되어야 하는 일이 없는 노드) 꺼내서 result(일의 순서)에 넣음
    for x in graph[now]:
        indegree[x] -= 1 # 선행되는 일을 했으니(now) 그와 연결된 노드들의 indegree 값도 줄여줌
        if indegree[x] == 0: 
            heapq.heappush(q, x) # 더이상 선행되어야 하는 일이 없어진 경우 큐에 넣어줌


if len(result) != N:
    print("Cannot complete these tasks. Going to bed.")
else:
    print(' '.join(map(str, result)))
