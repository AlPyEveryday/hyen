import sys
input = sys.stdin.readline

N,L = map(int, input().split())
seq = []
# x + (x+1) + .. + (x+L-1)
# N = L*x + {L*(L-1)}/2
# x = {N - L(L-1)/2}/L
# L을 1씩 증가 (100까지) 그러면서 x가 음수가 되거나 L이 0보다 커지면 -1
found = False

while (L <= 100):
    x = N - (L*(L-1)//2)
    if x < 0:
        break
    
    if (N - (L*(L-1)//2)) % L == 0:
        x = (N - (L*(L-1)//2))//L
        if x >= 0:
            result = [x + i for i in range(L)]
            print(' '.join(map(str, result)))
            found = True
            break
    
    L += 1

if not found:
    print(-1)