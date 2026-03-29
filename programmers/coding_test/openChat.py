def solution(record):
    answer = []
    nickName = {}
    for r in record:
        command = r.split()[0]
        if command == "Enter" or command == "Change":
            uid = r.split()[1]
            nickN = r.split()[2]
            nickName[uid] = nickN
    
    for order in record:
        command = order.split()[0]
        if command == "Enter" or command == "Change":
            uid = order.split()[1]
            nickN = order.split()[2]
        else:
            uid = order.split()[1]
        
        ans = ""
        if command == "Enter":
            ans = nickName[uid] + "님이 들어왔습니다."
        elif command == "Leave":
            ans = nickName[uid] + "님이 나갔습니다."
        
        answer.append(ans)
        
    
    return answer

a = solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])
print(a)