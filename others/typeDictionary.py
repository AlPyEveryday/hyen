# Dictionary
# 기본 딕셔너리 모습: {Key1:Value1, Key2:Value2, Key3:Value3, ...}
dic = {'name': 'hyen','phone': '01012345678', 'birth': '0507'}
# Key에는 변하지 않는 값, value에는 변하는 값, 변하지 않는 값 모두 사용 가능

# 딕셔너리 쌍 추가 삭제
# 추가
dic['year'] = 2003
print(dic)

# 삭제
del dic['year'] # key로 삭제
print(dic)

# Key가 중복되면 나머지는 무시됨
# key 리스트 만들기 a.keys()
# value 리스트 만들기 a.values()