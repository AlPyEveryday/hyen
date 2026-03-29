from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    people = defaultdict(list)

    # 정보를 딕셔너리에 추가
    for i in info:
        tmp = i.split()
        conditions = tmp[:-1]
        score = int(tmp[-1])

        for n in range(5):
            for combi in combinations(range(4), n):
                case = conditions[:]

                for idx in combi:
                    case[idx] = '-'
                
                people["".join(case)].append(score)

    for key in people:
        people[key].sort()
    
    for q in query:
        q = q.replace("and", "").split()
        q_condition = "".join(q[:-1])
        q_score = int(q[-1])

        if q_condition in people:
            scores = people[q_condition]
            # 전체 개수 - 기준 점수가 처음 나타나는 인덱스
            idx = bisect_left(scores, q_score)
            answer.append(len(scores) - idx)
        else:
            answer.append(0)

    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))