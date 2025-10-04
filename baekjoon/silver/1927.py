n = int(input())
A = []
for i in range(n):
    x = int(input())
    if x == 0:
        if len(A) > 0: 
            print(A[0])
            del A[0]
        else: print(0)
    elif x > 0:
        A.append(x)
        A.sort()