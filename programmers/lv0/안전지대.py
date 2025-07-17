def solution(board):
    n = len(board)
    landmine = [[0 for _ in range(n)] for _ in range(n)]
    print(landmine)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1: 
                landmine[i][j] = 1
                if ((j+1) < n) & ((j-1) >= 0):
                    landmine[i][j+1] = 1
                    landmine[i][j-1] = 1
                if ((i+1) < n) & ((i-1) >= 0):
                    landmine[i+1][j] = 1
                    landmine[i-1][j] = 1
                    if ((j+1) < n) & ((j-1) >= 0):
                        landmine[i+1][j+1] = 1
                        landmine[i+1][j-1] = 1
                        landmine[i-1][j-1] = 1
                        landmine[i-1][j+1] = 1
    
    cnt = 0
    for i in range(n):
        for j in range(n):
            if landmine[i][j] == 0 : cnt+= 1



    
    print(landmine)
    print(cnt)
    return cnt

solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1]])