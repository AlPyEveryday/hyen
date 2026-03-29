from collections import deque

R, C, K = map(int, input().split())
arr = [[0] * C for _ in range(R)]
golem = [list(map(int, input().split())) for _ in range(K)]
is_exit = [[0] * C for _ in range(R)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def dir_c(d):
    d += 1
    if d == 4:
        d=0
    return d

def dir_cc(d):
    d -= 1
    if d == -1:
        d=3
    return d

def can_move_south(r, c):
    # 남쪽으로 한 칸 내려가기 위해 체크 (r+2, c), (r+1, c-1), (r+1, c+1)
    for nr, nc in [(r+2, c), (r+1, c-1), (r+1, c+1)]:
        if not (nr < R and 0 <= nc < C): return False # 밑바닥 체크
        if nr >= 0 and arr[nr][nc] != 0: return False # 골렘 존재 여부
    return True

def can_move_west(r, c):
    # 서쪽 회전 이동을 위해 체크
    # (r-1, c-1), (r, c-2), (r+1, c-1), (r+1, c-2), (r+2, c-1)
    for nr, nc in [(r-1, c-1), (r, c-2), (r+1, c-1), (r+1, c-2), (r+2, c-1)]:
        if not (nr < R and 0 <= nc < C): return False
        if nr >= 0 and arr[nr][nc] != 0: return False
    return True

def can_move_east(r, c):
    # 동쪽 회전 이동을 위해 체크
    # (r-1, c+1), (r, c+2), (r+1, c+1), (r+1, c+2), (r+2, c+1)
    for nr, nc in [(r-1, c+1), (r, c+2), (r+1, c+1), (r+1, c+2), (r+2, c+1)]:
        if not (nr < R and 0 <= nc < C): return False
        if nr >= 0 and arr[nr][nc] != 0: return False
    return True

def bfs(start_r, start_c):
    q = deque([(start_r, start_c)])
    visited = [[False] * C for _ in range(R)]
    visited[start_r][start_c] = True
    max_r = start_r

    while q:
        curr_r, curr_c = q.popleft()
        max_r = max(max_r, curr_r)

        for i in range(4):
            nr, nc = curr_r + dr[i], curr_c + dc[i]
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and arr[nr][nc] != 0:
                # 같은 골렘 내부거나, 현재 칸이 출구여서 인접한 다른 골렘으로 넘어가는 경우
                if arr[nr][nc] == arr[curr_r][curr_c] or is_exit[curr_r][curr_c]:
                    visited[nr][nc] = True
                    q.append((nr, nc))
    return max_r + 1

ans = 0
for i in range(K):
    # 초기 위치
    ci, di = golem[i]
    r, c, d = -2, ci - 1, di

    while True:
        # 1. 남쪽 이동 가능 여부 체크 (r+2, c) 및 양옆 (r+1, c-1/c+1)
        if can_move_south(r, c): 
            r += 1
        # 2. 서쪽 이동: 왼쪽 한 칸(r, c-1) + 왼쪽 아래(r+1, c-1) + 그 아래(r+2, c-1) 등 체크
        elif can_move_west(r, c):
            r += 1
            c -= 1
            d = dir_cc(d)
        # 3. 동쪽 이동
        elif can_move_east(r, c):
            r += 1
            c += 1
            d = dir_c(d)
        else:
            break

    # 숲 범위를 벗어난 경우 (몸통이 0행보다 위)
    if r < 1:
        arr = [[0] * C for _ in range(R)]
        is_exit = [[False] * C for _ in range(R)]
    else:
        # 골렘 고정 (십자 모양 5칸 기록)
        arr[r][c] = i + 1
        for k in range(4):
            arr[r + dr[k]][c + dc[k]] = i + 1
        # 출구 표시
        is_exit[r + dr[d]][c + dc[d]] = True
        
        # 정령 이동 후 점수 합산
        ans += bfs(r, c)

print(ans)