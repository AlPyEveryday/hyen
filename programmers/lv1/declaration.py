def solution(id_list, report, k):
    """
    dec = [[] for _ in range(len(id_list))] # 초기화
    cnt = [0 for _ in range(len(id_list))] 
    answer = [0 for _ in range(len(id_list))]

    for r in report:
        x = r.split()
        i = id_list.index(x[0])
        if (x[1] in dec[i]) == False : dec[i].append(x[1])
    
    print(dec)

    
    for i  in range(len(id_list)):
        for d in dec:
            if id_list[i] in d: cnt[i] += 1

    t = 0
    for c in cnt:
        if c >= k:
            for d in range(len(dec)):
                if id_list[t] in dec[d]: answer[d] += 1
        t += 1
        
    """

    report_dict = {user: set() for user in id_list}
    for r in report:
        x1, x2 = r.split()
        report_dict[x2].add(x1)
    
    reported = set([user for user in report_dict if len(report_dict[user]) >= k])
    answer_dict = {user: 0 for user in id_list}

    for r in reported:
        for report_user in report_dict[r]:
            answer_dict[report_user] += 1

    answer = [answer_dict[user] for user in id_list]    
    
    
    return answer

id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3

print(solution(id_list, report, k))