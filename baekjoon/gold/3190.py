from collections import deque

N = int(input())
K = int(input())

# 기본이 되는 N x N 배열
arr = [[0 for col in range(N)] for row in range(N)]

# 사과 있는 곳 1로 표시
for _ in range(K):
    x,y = map(int, input().split())
    arr[x-1][y-1] = 1

# 방향 (동서남북 방향)
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# 방향 변화 저장
L = int(input())
sec = [0 for _ in range(L)]
change = [0 for _ in range(L)]

for i in range(L):
    second, direc = input().split()
    if direc == 'D': d = 1
    elif direc == 'L': d = -1

    sec[i] = int(second)
    change[i] = d

# 변수명 정리를 안해서 ㅎㅎ..
c = 0
di = 0
i= 0
head_x = 0
head_y = 0
queue = deque([[0,0]])

# 방향 바꾸기 함수
def directions(di, i):
    di = di + change[i]
    if di == 4: di = 0
    elif di == -1 : di = 3

    return di

# 반복하며 확인
while True:
    c += 1
    head_x += dir[di][0]
    head_y += dir[di][1]

    tail_x = queue[0][0]
    tail_y = queue[0][1]

    if head_x < 0 or head_x >= N or head_y <0 or head_y >= N:
        print(c)
        break
    elif arr[head_x][head_y] == -1:
        print(c)
        break
    
    if i<L and sec[i] == c:
        di = directions(di, i)
        i += 1
    
    if arr[head_x][head_y] == 1:
        arr[tail_x][tail_y] = -1
    else:
        arr[tail_x][tail_y] = 0
        queue.popleft()
    
    arr[head_x][head_y] = -1
    queue.append([head_x, head_y])

