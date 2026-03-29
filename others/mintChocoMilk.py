# from collections import deque

# N, T = map(int, input().split())
# F = [[''] *N for _ in range(N)]
# for i in range(N):
#     food = input()
#     for j in range(N):
#         F[i][j] = food[j]

# B = [list(map(int, input().split())) for _ in range(N)]
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
# groupB = []
# visited = [[0] * N for _ in range(N)]

# def morning():
#     for i in range(N):
#         for j in range(N):
#             B[i][j] += 1

# def grouping():
#     g = 0
#     for r in range(N):
#         for c in range(N):
#             if visited[r][c] != 0: continue
#             target = F[r][c]
#             max_B = B[r][c]
#             b_r = r; b_c = c
#             q  = deque([(r,c)])
#             g += 1
#             num = 0

#             while q:
#                 curr_r, curr_c = q.popleft()
#                 for i in range(4):
#                     cr = curr_r + dr[i]
#                     cc = curr_c + dc[i]
#                     if cr<0 or cr >= N or cc < 0 or cc>=N or visited[cr][cc] != 0 or F[cr][cc] != target: continue
#                     else:
#                         visited[cr][cc] = g
#                         q.append((cr, cc))
#                         num += 1
#                         # 신앙심 갱신
#                         if B[cr][cc] > max_B:
#                             max_B = B[cr][cc]
#                             B[b_r][b_c] -= 1
#                             b_r = cr; b_c = cc
#                         elif B[cr][cc] == max_B:
#                             if cr == b_r:
#                                 if cc < b_r:
#                                     B[b_r][b_c] -= 1
#                                     b_r = cr; b_c = cc
#                             elif cr < b_r:
#                                 B[b_r][b_c] -= 1
#                                 b_r = cr; b_c = cc

#             B[b_r][b_c] += (num-1)    # 그룹장 신앙심 처리
#             fg = len(target)
#             groupB.append([fg, B[b_r][b_c], b_r, b_c]) # 그룹장의 좌표와 신앙심을 groupB[g-1]에 저장

# def addFood(x, y):
#     if len(x) == 1 and len(y) == 1:
#         if x == 'T': return x+y
#         elif y == 'T': return y+x
#         elif x == 'C': return x+y
#         else: return y+x
#     else: return "TCM"

# def spread():
#     groupB.sort(key=lambda x:(x[0], -x[1], x[2], x[3]))
#     for g in groupB:
#         d = g[1] % 4
#         x = g[1] - 1
#         r = g[2]
#         curr_r = g[2]
#         c= g[3]
#         curr_c = g[3]
#         B[r][c] = 1

#         while x:
#             if curr_r+ dr[d] < 0 or curr_r+ dr[d] >= N or curr_c+dc[d] < 0 or curr_c+dc[d] >= N:
#                 break
#             target = F[curr_r+ dr[d]][curr_c+dc[d]]
#             belif = B[curr_r+ dr[d]][curr_c+dc[d]]
#             bf = F[r][c]

#             if target == bf:
#                 curr_r += dr[d]
#                 curr_c += dc[d]
#                 continue
#             elif x > belif: # 강한 전파
#                 x -= (belif + 1)
#                 B[curr_r+ dr[d]][curr_c+dc[d]] += 1
#                 F[curr_r+ dr[d]][curr_c+dc[d]] = bf
#             elif x <= belif: # 약한 전파
#                 x = 0
#                 B[curr_r+ dr[d]][curr_c+dc[d]] += x
#                 addFood(bf, target)

# def addB(x):
#     ans = 0
#     for r in range(N):
#         for c in range(N):
#             if F[r][c] == x: ans += B[r][c]
    
#     return ans


# for _ in range(T):
#     morning()
#     grouping()
#     spread()
#     for f in ["TCM", "TC", "TM", "CM", "M", "C", "T"]:
#         sumB = addB(f)
#         print(sumB, end=' ')



from collections import deque

N, T = map(int, input().split())
F = [[''] * N for _ in range(N)]
for i in range(N):
    food = input()
    for j in range(N):
        F[i][j] = food[j]

B = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def morning():
    for i in range(N):
        for j in range(N):
            B[i][j] += 1

def grouping():
    groupB = []
    visited = [[False] * N for _ in range(N)]  # 매일 초기화

    for r in range(N):
        for c in range(N):
            if visited[r][c]:
                continue
            target = F[r][c]
            visited[r][c] = True  # 시작 셀 즉시 방문 처리
            q = deque([(r, c)])
            members = [(r, c)]

            while q:
                curr_r, curr_c = q.popleft()
                for i in range(4):
                    cr = curr_r + dr[i]
                    cc = curr_c + dc[i]
                    if 0 <= cr < N and 0 <= cc < N and not visited[cr][cc] and F[cr][cc] == target:
                        visited[cr][cc] = True
                        q.append((cr, cc))
                        members.append((cr, cc))

            # 대표자 선정: B 높은 순 → r 작은 순 → c 작은 순
            leader = members[0]
            for mr, mc in members[1:]:
                lr, lc = leader
                if (B[mr][mc], -mr, -mc) > (B[lr][lc], -lr, -lc):
                    leader = (mr, mc)

            # 신앙심 이전
            lr, lc = leader
            for mr, mc in members:
                if (mr, mc) != (lr, lc):
                    B[mr][mc] -= 1
            B[lr][lc] += len(members) - 1  # num-1 아닌 len-1

            groupB.append([len(target), B[lr][lc], lr, lc])
    return groupB

def addFood(x, y):
    # TCM 순서 보장, 다양한 길이 처리
    combined = set(x) | set(y)
    result = ''
    for ch in ['T', 'C', 'M']:
        if ch in combined:
            result += ch
    return result

def spread(groupB):
    defended = [[False] * N for _ in range(N)]  # 방어 상태 추가
    groupB.sort(key=lambda g: (g[0], -g[1], g[2], g[3]))

    for g in groupB:
        r, c = g[2], g[3]
        if defended[r][c]:  # 방어 상태면 전파 안 함
            continue

        bf = F[r][c]
        curr_b = B[r][c]  # 현재 B 기준으로 방향/간절함 계산
        d = curr_b % 4
        x = curr_b - 1
        B[r][c] = 1
        curr_r, curr_c = r, c

        while x > 0:
            nr = curr_r + dr[d]
            nc = curr_c + dc[d]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                break

            t_food = F[nr][nc]
            t_b = B[nr][nc]

            if t_food == bf:
                curr_r, curr_c = nr, nc
                continue

            if x > t_b:  # 강한 전파
                x -= (t_b + 1)
                B[nr][nc] += 1
                F[nr][nc] = bf
                defended[nr][nc] = True
                curr_r, curr_c = nr, nc
            else:  # 약한 전파
                B[nr][nc] += x  # x=0 전에 먼저 더하기
                F[nr][nc] = addFood(bf, t_food)  # 반환값 대입
                defended[nr][nc] = True
                x = 0

def addB(food):
    ans = 0
    for r in range(N):
        for c in range(N):
            if F[r][c] == food:
                ans += B[r][c]
    return ans  # 들여쓰기 수정: 루프 밖으로

for _ in range(T):
    morning()
    groupB = grouping()
    spread(groupB)
    results = []
    for f in ["TCM", "TC", "TM", "CM", "M", "C", "T"]:
        results.append(str(addB(f)))
    print(' '.join(results))


            

