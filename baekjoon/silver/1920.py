N = int(input())
A = set(map(int, input().split()))
# A.sort()
M = int(input())
B = list(map(int, input().split()))

for b in B:
    if b in A: print(1)
    else: print(0)

# for b in B:
#     start = 0
#     end = N-1
#     found = False

#     while start <= end:
#         mid = (start+end)//2

#         if b == A[mid]: 
#             found = True
#             break
#         elif b < A[mid]: end = mid -1
#         elif b > A[mid]: start = mid +1
    
#     if found: print(1)
#     else: print(0)
