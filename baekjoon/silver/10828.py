import sys
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    order = input().split()
    command = order[0]
    
    n = len(arr)
    if command == "push":
        x = order[1]
        arr.append(int(x))
    elif command == "pop":
        if n > 0:
            p = arr.pop()
        else:
            p = -1    
        print(p)
    elif command == "size":
        print(len(arr))
    elif command == "empty":
        if n > 0:
            print(0)
        else:
            print(1)
    elif command == "top":
        if n > 0:
            print(arr[-1])
        else:
            print(-1)
