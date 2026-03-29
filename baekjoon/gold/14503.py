n,m = map(int, input().split())
r,c,d = map(int, input().split())
num = 0

# 배열 설정
# arr = [[0]*m for _ in range(n)]
# for i in range(n):
#     tmp = list(map(int, input().split()))
#     for j in range(m):
#         arr[i][j] = tmp[j]
arr = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
    
# 방향바꾸기 함수
def dir(d):
    d -= 1
    if d == -1:
        d=3
    return d


while 1:
    if arr[r][c] == 0:
        arr[r][c] = -1
        num +=1
    clean_needed = False  # 이것이 플래그 변수입니다! (주변에 청소할 칸이 있는가?)

    # 2. 주변 4칸 검사 (반복문 활용)
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        
        # 범위 내에 있고, 청소되지 않은 빈 칸(0)이 있다면?
        if 0 <= nr < n and 0 <= nc < m:
            if arr[nr][nc] == 0:
                clean_needed = True # 청소할 곳 발견! 스위치 ON
                break

    if not clean_needed:
        t_r = r - dr[d]
        t_c = c - dc[d]
        if(arr[t_r][t_c] != 1) :
            r = t_r
            c = t_c
            continue
        else:
            break
    else:
        d = dir(d)
        t_r = r + dr[d]
        t_c = c + dc[d]
        if (arr[t_r][t_c] == 0):
            arr[t_r][t_c] = -1
            r = t_r
            c = t_c
            num += 1

print(num)


