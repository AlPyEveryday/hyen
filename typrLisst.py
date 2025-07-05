# List
# 리스트명 = [요소1, 요소2, 요소3, ...]
a = []
b = [1, 2, 3]
c = ['life', 'is', 'too', 'short']

# 인덱싱
d = b[:2]

# 리스트 더하기 
print(b + d)
# 리스트 길이 구하기: len

# 리스트 수정
b[1] = 33
print(b)

# 리스트 삭제 : del 객체
del b[1]
print(b)

print("="*50)

# 리스트에 요소 추가 (append)
a.append([5,6]) # 리스트에 리스트 추가
print(a)
a.append(4)
print(a)

# 순서대로 정렬: sort()
# 위치 반환: index(x)
# 요소 삽입: insert(a, b) -> a번째 위치에 b 삽입
# 요소 제거: remove(x) -> 리스트에서 첫번째로 나오는 x를 삭제
# pop(): 리스트의 맨 마지막 요소 돌려주고 그 요소 삭제
# pop(x): x번째 요소 돌려주고 그 요소 삭제
# count(x): x가 몇개 있는지 조사해 그 개수 돌려줌
# a.extend(x): x에는 리스트만 올수 있고 원래의 a 리스트에 x 리스트를 더함 
