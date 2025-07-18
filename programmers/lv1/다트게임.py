def solution(dartResult):
    answer = 0
    tmp = []
    num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    prev= 0
    prev_v = ''
    cnt = 0
    for d in dartResult:
        if (prev_v in num) and (d in num): # 10 인 경우
            prev = 10
            prev_v = d
        elif d in num: # 숫자는 prev에 넣어두기
            prev = int(d)
            prev_v = d 
        else: # 각 조건에 맞게 tmp의 값들 처리
            prev_v = 'notNum'
            if d == "S": 
                tmp.append(prev)
                cnt += 1
            elif d == "D": 
                tmp.append(prev*prev)
                cnt += 1
            elif d == "T": 
                tmp.append(prev*prev*prev)
                cnt += 1
            elif d == "*":
                for i in range(cnt-2,cnt):
                    tmp[i] = tmp[i]*2
            elif d == "#":
                tmp[cnt-1] = -tmp[cnt-1]   
        
    for t in tmp:
        answer += t
    
    print(answer)
    return answer

solution("1D2S3T*")