def solution(numbers, hand):
    answer = ''
    lLoca = [3,0]
    rLoca = [3,2]
    kp0 = [1, 2, 3]
    kp1 = [4, 5, 6]
    kp2 = [7, 8, 9]
    kp3 = ["*", 0, "#"]
    
    def moveRhand():
        rLoca[0] = loca[0]
        rLoca[1] = loca[1]
        
    def moveLhand():
        lLoca[0] = loca[0]
        lLoca[1] = loca[1]
    
    def move(h):
        if h == "R": moveRhand()
        elif h == "L": moveLhand()
    # 한가지 궁금한 점
    # 내장 함수?를 만들때는 변수가 그냥 알아서 사용이 되는 것인가? like lLoca, loca 같은거
    
    if hand == "right": h = "R"
    elif hand == "left": h = "L"
    
    for n in numbers:
        if n in kp0: loca = [0, kp0.index(n)]
        elif n in kp1: loca = [1, kp1.index(n)]
        elif n in kp2: loca = [2, kp2.index(n)]
        elif n in kp3: loca = [3, kp3.index(n)]
        
        if n in [1, 4, 7]:
            answer += "L"
            moveLhand()
        elif n in [3, 6, 9]:
            answer += "R"
            moveRhand()
        elif n in [2, 5, 8, 0]:
            dist1 = abs(lLoca[0]-loca[0])+abs(lLoca[1]-loca[1])
            dist2 = abs(rLoca[0]-loca[0])+abs(rLoca[1]-loca[1])
            if dist1 < dist2:
                answer += "L"
                moveLhand()
            elif dist2 < dist1:
                answer += "R"
                moveRhand()
            elif dist2 == dist1:
                answer += h
                move(h)
            
    return answer