
T = "abcdefghijklmnopqrstuvwxyz"
P = "ak"
l_T = len(T)
l_P = len(P)
# order = {}
# for i in range(l_T):
#     order[T[i]] = i

# def solution(T, P):
#     num = 0
#     tmp = 1
#     for k in range(1,l_P):
#         num += l_T ** k

#     for j in range(l_P-1):
#         tmp += ((order[P[j]])  * (l_T  ** (l_P - j-1)))
#     tmp += order[P[l_P-1]]
#     num += tmp
#     return num % 900528


def solution(T, P):
    l_T = len(T)
    l_P = len(P)
    MOD = 900528
    
    # 1. order 딕셔너리 생성 (T의 각 요소의 인덱스를 미리 저장)
    order = {char: i for i, char in enumerate(T)}
    
    # 2. 자릿수가 l_P 미만인 모든 경우의 수 합산
    # 등비수열의 합 공식을 쓰거나, 루프 하나로 처리
    num = 0
    current_pow = 1
    for k in range(1, l_P):
        current_pow = (current_pow * l_T) % MOD
        num = (num + current_pow) % MOD

    # 3. 호너의 방법(Horner's Method)으로 P의 인덱스 계산
    tmp = 0
    for char in P:
        # 매 단계에서 MOD 연산을 수행하여 숫자가 커지는 것을 방지
        tmp = (tmp * l_T + order[char]) % MOD
    
    # 문제의 로직상 tmp에 1을 더해야 한다면 (1-based index 등)
    num = (num + tmp + 1) % MOD
    
    return num


print(solution(T,P))