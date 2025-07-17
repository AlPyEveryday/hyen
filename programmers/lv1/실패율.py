def solution(N, stages):
    stage_list = [0 for _ in range(N)]
    clear = 0
    for s in stages:
        if s <= N : stage_list[s-1] +=1
        if s > N: clear += 1 # 사실 이미 clear한 사람들은 따로 뭐 처리해줄필요 없긴함
    print(stage_list)

    fail_dict = {stage : 0 for stage in range(1,N+1)}
    for i in range(len(stage_list)):
        tryPeople = len(stages)
        for j in range(i):
            tryPeople -= stage_list[j] # 해당 스테이지 이전에 있는 사람들은 시도한 사람에포함 안되니까 빼줌
        
        if tryPeople == 0: # 분모가 0이되면 runtime eroor가 난다
            fail_dict[i+1] = 0 # i+1로 한 이유는 스테이지는 1부터니까
        else:
            fail_dict[i+1] = stage_list[i]/tryPeople
    
    fail = []
    for f in fail_dict:
        fail.append((fail_dict[f], f))  # (실패율, 스테이지 번호)

    # 실패율 내림차순, 같으면 스테이지 번호 오름차순
    fail.sort(key=lambda x: (-x[0], x[1]))

        

    print(fail)

    answer = []
    for f in fail:
        answer.append(f[1])


    print(answer)
    
    return answer

solution(5,[2, 1, 2, 6, 2, 4, 3, 3])