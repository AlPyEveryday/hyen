def solution(babbling):
    answer = 0
    babe =  ["aya", "ye", "woo", "ma"]
    for b in babbling:
        i = 0
        while i < len(b):
            if b[i:i+3] in babe:
                i += 3
            elif  b[i:i+2] in babe:
                i += 2
            else: 
                i =0
                break
            
        if i != 0: answer += 1
                
    return answer