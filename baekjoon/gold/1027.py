import sys
input = sys.stdin.readline

N = int(input())
buildings = [0 for _ in range(N+1)]
look = [0 for _ in range(N+1)]
buildingList = input().split()

for i in range(N):
    buildings[i+1] = int(buildingList[i])


for j in range(1, N+1):
    max_look = 0
    max_slope = float('-inf')
    for k in range(j+1, N+1):
        slope = (buildings[k]-buildings[j])/(k-j)
        if slope > max_slope:
            max_look += 1
            max_slope = slope
    
    min_slope = float('inf')
    for k in range(j-1,0,-1):
        slope = (buildings[k]-buildings[j])/(k-j)
        if slope < min_slope:
            max_look += 1
            min_slope = slope
    
    look[j] = max_look


print(max(look))

