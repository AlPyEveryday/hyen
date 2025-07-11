def solution(friends, gifts):
    gift_dict = {name: [] for name in friends}
    for g in gifts:
        # 준사람, 받은 사람으로 나눠 준사람 기준 받은 사람을 리스트로 정리
        sender, receiver = g.split()
        gift_dict[sender].append(receiver)

    # 선물 준 횟수 리스트에 저장
    send_cnt = {name : 0 for name in friends}
    for f in friends:
        send_cnt[f] = len(gift_dict[f])
    
    # 선물 받은 횟수
    receive_cnt = {name : 0 for name in friends}
    for f in friends:
        for i in friends: receive_cnt[f] += gift_dict[i].count(f)

    # 선물 지수
    gift_index = {name : 0 for name in friends}
    for f in friends:
        gift_index[f] = send_cnt[f] - receive_cnt[f]
    
    # 다음 달 받아야하는 선물개수
    next_gift = {name : 0 for name in friends}
    for i in range(len(friends)):
        j = i+1
        while j < len(friends) :
            x = gift_dict[friends[i]].count(friends[j])
            y = gift_dict[friends[j]].count(friends[i])
            if(x > y) : next_gift[friends[i]] += 1
            elif (x < y) : next_gift[friends[j]] += 1
            elif (x == y) | (x==y==0) :
                if(gift_index[friends[i]] > gift_index[friends[j]]) : next_gift[friends[i]] += 1
                elif(gift_index[friends[i]] < gift_index[friends[j]]) : next_gift[friends[j]] += 1
            j += 1   

    gift_list = [next_gift[name] for name in friends]
    gift_list.sort()

    return gift_list[-1]

    

friends = ["joy", "brad", "alessandro", "conan", "david"]
gifts = ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]



print(solution(friends, gifts))