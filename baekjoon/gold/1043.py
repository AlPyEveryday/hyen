import sys
input = sys.stdin.readline 

N, M = map(int, input().split())
truth_line = input().split()

truth_num = int(truth_line[0])


if truth_num == 0:
    print(M)
    exit() # 진실을 아는 사람이 없으면 바로 M 출력 후 종료

# 진실을 아는 사람 번호만 저장
truth = set(int(x) for x in truth_line[1:])

# 2. 모든 파티 정보를 미리 저장
all_parties = []
for _ in range(M):
    party_info = input().split()
    members = set(int(x) for x in party_info[1:]) # 파티 멤버도 set으로 저장하면 효율적
    all_parties.append(members)


# 3. 진실 전파 (while 루프)
while True:
    pre_truth_size = len(truth) # 전파 전 크기
    
    # 저장된 모든 파티를 순회하며 진실 전파가 있는지 확인
    for party_members in all_parties:
        # party_members와 truth 사이에 겹치는 원소가 있는지 확인 (진실 전파가 발생했는지)
        if not truth.isdisjoint(party_members): 
            # 겹치는 사람이 한 명이라도 있다면, 이 파티의 모든 사람에게 진실이 전파됨
            truth.update(party_members)
            
    # 이번 루프에서 truth 집합 크기가 변하지 않았다면, 더 이상 전파될 진실이 없음
    if pre_truth_size == len(truth):
        break

# 4. 마지막 결과 계산
lie_count = 0
for party_members in all_parties:
    # 최종 truth 집합과 겹치는 사람이 없다면 거짓말 가능
    if truth.isdisjoint(party_members):
        lie_count += 1

print(lie_count)