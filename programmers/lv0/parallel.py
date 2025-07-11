dots= [[1, 4], [9,2], [3,8], [11, 6]]


def solution(dots):
    [x1,y1], [x2, y2], [x3, y3], [x4, y4] = dots
    a = (y2-y1)/(x2-x1) == (y4-y3)/(x4-x3)
    b = (y3-y1)/(x3-x1) == (y4-y2)/(x4-x2)
    c = (y4-y1)/(x4-x1) == (y3-y2)/(x3-x2)
    """
    slope = []
    for i in range(3):
        t = i+1
        while(t<4):
            dx = (dots[t][1]-dots[i][1])/(dots[t][0]-dots[i][0])
            slope.append(dx)
            t += 1
        

    print(slope)
    for s in slope:
        if (slope[0] == slope[5]) | (slope[1] == slope[4]) | (slope[2] == slope[3]): return 1
    return 0
    """
    if a | b | c: return 1
    else: return 0

print(solution(dots))

# 처음에 잘못한 점:
# 기울기 배열을 만들어 동일한 값이 2개 이상 존재하면 1을 리턴하게 했는데, 이러면 동일한 점을 두번 연결하는 경우가 포함됨
# 문제에서는 서로 다른 네점을 각각 2개씩 짝지어서 이은 직선이 평행하는 경우를 찾는것인데, 
# 내가 한 경우에는 1,2번 이어서 만든 직선과 1,3번 이어서 만든 직선의 기울기가 동일해도 1을 리턴하게끔 설정됨

# 이후 수정
# 기울기 배열에서 (0,5), (1,4), (2,3)이 동일한 경우 1을 리턴하게 함

# 개선가능한 점
# dots를 중첩언패킹 [x1,y1], [x2, y2], [x3, y3], [x4, y4] = dots  >> 통해서 더 깔끔하게 만들수 있음
# a,b,c에는 각 직선이 평행한지 여부 (True, False)가 저장됨




