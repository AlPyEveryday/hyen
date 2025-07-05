# 문자열
# 방법 1: 큰 따옴표로 양쪽 둘러싸기
print("hi")
# 방법 2: 작은 따옴표로 양쪽 둘러싸기
print('hello')
# 그외 방법: 큰따옴표 or 작은 따옴표 3개를 연속으로 써서 양쪽에 둘러싸기

# 문자열에 " 혹은 '을 포함하고 싶으면 \ 사용
print("he said \"hi\"")
print("I want \'pizza\'")


# 이스케이프 코드
# \n : 줄바꿈
# \t : 문자열 사이 탭 간격
# \\ : 문자 \를 그대로 사용할때
# \000 : 널 문자

# 문자열 곱하기
a = "I am hungry"
print(a*2)
print("=" * 50)

# 문자열 길이 : len 함수
print(len(a))

# 문자열 인덱싱
print(a[3])
print(a[-1]) # 제일 오른쪽
print(a[0:3]) # [a:b] -> a번째 에서 b개 만큼 슬라이싱
# 생략시 a는 맨처음, b는 맨끝을 의미

print("="*50)

# 문자열 포매팅
# %s : String
# %c : character
# %d : Integer
# %f : floating-point
# %o : 8진수
# %x: 16진수
# %% : 문자 %자체
print("I have %d apples" %3)
rate = 3.22
print("rate is %f" %rate)
print("rate is %0.2f" %rate) # 소수점 뒷자리 설정

# 두개 이상의 값 넣을때
name = "hyen"
id = "20221362"
print("my name is %s and my ID id %s" %(name, id))
print("my name is {name} and my ID id {id}".format(name = "hyen", id =20221362))

# f 문자열 포매팅
print(f"hi {name}")

#  문자 개수 세기
print(a.count('h'))
# 위치 알려주기
print(a.find('m')) # 존재하지 않는다면 -1 반환
