# N = int(input())
# num = list(map(int, input().split()))
# operator = list(map(int, input().split()))

N =6
num = [1,2,3,4,5,6]
operator = [2,1,1,1]
dictOper = {'+': operator[0], '-': operator[1], '*': operator[2], '/': operator[3]}

def permutation(num, dict, n):
    min = 1000000000
    max = - 1000000000

    def backtrack(path):
        nonlocal max, min
        if len(path) == n:
            res = solve(num, path, n)
            if res > max : max = res
            if res < min : min = res
            return
        
        for d in dict:
            if dict[d] > 0:
                dict[d] -= 1
                path.append(d)
            
                backtrack(path)

                path.pop()
                dict[d] += 1
    
    backtrack([])
    return [max, min]

def solve(num, perm, n):
    res = num[0]
    for i in range(n):
        j = i + 1
        if perm[i] == '+':
            res += num[j]
        elif perm[i] == '-':
            res -= num[j]
        elif perm[i] == '*':
            res *= num[j]
        elif perm[i] == '/':
            if res < 0:
                res = -((-res)//num[j])
            else:
                res = res // num[j]
    return res

result = permutation(num, dictOper, N-1)
print(result[0])
print(result[1])



