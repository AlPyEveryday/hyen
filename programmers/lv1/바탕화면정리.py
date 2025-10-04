def solution(wallpaper):
    answer= []
    fileIn = {'top' : 100, 'left' : 100, 'right' : -1, 'bottom' : -1}
    for w in wallpaper:
        n = len(w)
        h = wallpaper.index(w)
        for i in range(n):
            if w[i] == "#":
                if i < fileIn['left'] : fileIn['left'] = i
                if i+1 > fileIn['right'] :fileIn['right'] = i+1
                if h < fileIn['top'] : fileIn['top'] = h
                if h+1 > fileIn['bottom'] : fileIn['bottom'] = h+1
    
    print(fileIn)
    answer= [fileIn['top'], fileIn['left'],fileIn['bottom'],fileIn['right']]
            
    return answer

solution([".#...", "..#..", "...#."])