import sys
input = sys.stdin.readline

def combi(arr,n):
    result = []
    if n == 0:
        return [[]]
    
    for i in range(0, len(arr)):
        elem = arr[i]
        rest_arr = arr[i+1:]
        for C in combi(rest_arr, n-1):
            result.append([elem]+C)

    return result
    
res_list = []

while True:
    set_line = input().split()
    if int(set_line[0]) == 0: 
        break
    else:
        arr = list(map(int,set_line[1:]))
        arr.sort()
        res = combi(arr, 6)
        res_list.append(res)

for idx, res in enumerate(res_list):
    if idx > 0:
        print()
    for r in res:
        print(' '.join(map(str, r)))
        