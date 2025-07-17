def solution(lottos, win_nums):
    unknown = lottos.count(0)
    cnt = 0
    
    for l in lottos:
        if l in win_nums: 
            cnt += 1


    answer = [cnt, cnt+unknown]
    return answer

solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])