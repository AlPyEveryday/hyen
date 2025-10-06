import heapq
import sys

input = sys.stdin.readline
n = int(input())
heap = []
for i in range(n):
    x = int(input())
    if x == 0:
        if heap: 
            print(heapq.heappop(heap))
        else: print(0)
    elif x > 0:
        heapq.heappush(heap, x)