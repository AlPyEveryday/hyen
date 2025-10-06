import sys

input = sys.stdin.readline
N = int(input())
dic ={}
# lis = [[0] * N for _ in range(N) ]
# lis[0] = [0, 0, 0, 1, 0, 0, 0]
# lis[1] =[0, 0, 0, 0, 0, 0,1]
# lis[2] =[0, 0, 0, 0, 0, 0, 0]
# lis[3] = [0, 0, 0, 0, 1, 1, 0]
# lis[4] = [1, 0, 0, 0, 0, 0, 0]
# lis[5] =[0, 0, 0, 0, 0, 0, 1]
# lis[6] = [0, 0, 1, 0, 0, 0, 0]

for i in range(N):
    l = list(map(int, input().split()))
    n1 = [index for index, value in enumerate(l) if value == 1]
    dic[i] = set(n1)



for i in range(N):
    check = set()
    changed = True
    while changed:
        changed = False
        new_nodes = set()
        for m in dic[i]:
            if m not in check:
                new_nodes |= dic[m]
                check.add(m)
        if not new_nodes.issubset(dic[i]):
            dic[i] |= new_nodes
            changed = True

for i in range(N):
    print(' '.join(['1' if j in dic[i] else '0' for j in range(N)]))


# 처음에 했을때는 리스트로 한줄씩 출렷했는데 그러면 리스트 출력이니 당연히 답이랑 다름
# 이렇게 하면 숫자 출력이 아니라 문자열로 1 0 이 출력되니 틀림ㅁ
# for i in range(N):
#    l = ""
#    for j in range(N):
#        if j in dic[i]: l+="1"
#        else: l+= "0"
#    print(l)