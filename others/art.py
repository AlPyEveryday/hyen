# from  collections import deque
# from collections import defaultdict

# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]

# dx = [-1, 0, 1, 0] # 북 동 남 서
# dy = [0, 1, 0, -1]

# def grouping():
#     visited = [[False] * n for _ in range(n)]
#     group = defaultdict(list)
#     g_arr = [[0] * n for _ in range(n)]
#     g = 0
#     for i in range(n):
#         for j in range(n):
#             if visited[i][j] == False:
#                 q = deque([(i, j)])
#                 visited[i][j] = True
#                 value = arr[i][j]
#                 g += 1
#                 group[g].append(value)

#                 while q:
#                     x,y = q.popleft()
#                     for d in range(4):
#                         if x+dx[d] < 0 or x+dx[d] >= n or y+dy[d]<0 or y+dy[d] >=n:
#                             continue
#                         if visited[x+dx[d]][y+dy[d]] == False and arr[x+dx[d]][y+dy[d]] == value:
#                             q.append((x+dx[d],y+dy[d]))
#                             visited[x+dx[d]][y+dy[d]] = True
#                             group[g].append((x+dx[d],y+dy[d]))
#                             g_arr[x+dx[d]][y+dy[d]] = g
    
#     return g, group, g_arr

# def harmony(g, group, g_arr):
#     h = 0
#     for i in range(1, g-1):
#         for j in range(i+1, g):
#             num = (len(group[i])-1) + (len(group[j]) -1)
#             side = 0
#             value = group[i][0]
#             value2 = group[j][0]
#             for d in range(1, len(group[i])):
#                 x = group[i][d][0]
#                 y = group[i][d][1]
#                 for direction in range(4):
#                     if x+dx[direction] < 0 or x+dx[direction] >= n or y+dy[direction]<0 or y+dy[direction] >=n:
#                             continue
#                     if g_arr[x+dx[direction]][y+dy[direction]] == j:
#                         side += 1
            
#             tmp = num * value * value2 * side
#             h += tmp
    
#     return h

# def lotation():
#     N = n//2
#     C = n - N
#     ret = [[0] * n for _ in range(n)]

#     for r in range(n):
#         for c in range(n):
#             ret[r][c] = arr[c][n-1-r]

#     arr1 = [[0] * N for _ in range(N)]    
#     arr2 = [[0] * N for _ in range(N)]    
#     arr3 = [[0] * N for _ in range(N)]    
#     arr4 = [[0] * N for _ in range(N)]

#     for i in range(N):
#         for j in range(N):
#             arr1[i][j] = arr[i][j]
#             arr2[i][j] = arr[i][j+C]
#             arr3[i][j] = arr[i+C][j]
#             arr4[i][j] = arr[i+C][j+C]
    
#     ret1 = [[0] * N for _ in range(N)]
#     ret2 = [[0] * N for _ in range(N)]
#     ret3 = [[0] * N for _ in range(N)]
#     ret4 = [[0] * N for _ in range(N)]

#     for r in range(N):
#         for c in range(N):
#             ret1[c][N-1-r] = arr1[r][c]
#             ret2[c][N-1-r] = arr2[r][c]
#             ret3[c][N-1-r] = arr3[r][c]
#             ret4[c][N-1-r] = arr4[r][c]
    
#     for i in range(N):
#         for j in range(N):
#             ret[i][j] = ret1[i][j]
#             ret[i][j+C] = ret2[i][j]
#             ret[i+C][j] = ret3[i][j]
#             ret[i+C][j+C] = ret4[i][j]
    
#     return ret

# g, group, g_arr = grouping()
# h = harmony(g, group, g_arr)

# for _ in range(3):
#     lotation()
#     G, GROUP, G_ARR = grouping()
#     h += harmony(G, GROUP, G_ARR)

# print(h)


from collections import deque, defaultdict

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def grouping():
    visited = [[False] * n for _ in range(n)]
    group_coords = defaultdict(list) # 좌표 저장
    group_value = {} # 그룹의 숫자 값 저장
    g_arr = [[0] * n for _ in range(n)]
    g = 0
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                g += 1
                q = deque([(i, j)])
                visited[i][j] = True
                val = arr[i][j]
                group_value[g] = val # 그룹 번호에 따른 숫자 값
                
                while q:
                    x, y = q.popleft()
                    group_coords[g].append((x, y)) # 좌표들 저장
                    g_arr[x][y] = g
                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]
                        if 0 <= nx < n and 0 <= ny < n:
                            if not visited[nx][ny] and arr[nx][ny] == val:
                                visited[nx][ny] = True
                                q.append((nx, ny))
    return g, group_coords, group_value, g_arr

def get_harmony(g_cnt, group_coords, group_value, g_arr):
    h_sum = 0
    # 모든 그룹 쌍에 대해 (i < j)
    for i in range(1, g_cnt + 1):
        for j in range(i + 1, g_cnt + 1):
            side = 0
            # 그룹 i의 각 좌표에서 인접한 칸이 그룹 j인지 확인
            for x, y in group_coords[i]:
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n:
                        if g_arr[nx][ny] == j:
                            side += 1
            
            if side > 0:
                score = (len(group_coords[i]) + len(group_coords[j])) * \
                        group_value[i] * group_value[j] * side
                h_sum += score
    return h_sum

def rotate():
    global arr
    new_arr = [[0] * n for _ in range(n)]
    m = n // 2
    
    # 1. 십자 모양 회전 (반시계)
    for i in range(n):
        new_arr[m][i] = arr[i][m] # 세로줄 -> 가로줄
        new_arr[i][m] = arr[m][n-1-i] # 가로줄 -> 세로줄
        
    # 2. 4개 구역 회전 (시계)
    def rotate_90(sy, sx, size):
        for r in range(size):
            for c in range(size):
                new_arr[sy + c][sx + size - 1 - r] = arr[sy + r][sx + c]

    rotate_90(0, 0, m) # 좌상
    rotate_90(0, m + 1, m) # 우상
    rotate_90(m + 1, 0, m) # 좌하
    rotate_90(m + 1, m + 1, m) # 우하
    
    arr = [row[:] for row in new_arr]

# 메인 실행부
total_h = 0
for _ in range(4): # 초기 상태 + 3회 회전
    g_cnt, coords, values, g_matrix = grouping()
    total_h += get_harmony(g_cnt, coords, values, g_matrix)
    if _ < 3:
        rotate()

print(total_h)




