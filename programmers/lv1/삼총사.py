def solution(number):
    n = len(number)
    cnt =  0
    
    for i in range(0,n):
        for j in range(1, n-1):
            for k in range(2, n-2):
                if number[i]+number[j] + number[k] == 0: cnt+=1
        
        
    print(cnt)
    return cnt

solution([-2, 3, 0, 2, -5])