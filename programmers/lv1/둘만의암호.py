def solution(s, skip, index):
    # 유효한 알파벳 리스트 만들기 (skip 제외)
    alphabet = [chr(i) for i in range(97, 123) if chr(i) not in skip]

    answer = ''
    # for문 통해서 문자열에서 문자 하나씩 가져올 수 있음
    for ch in s:
        current_idx = alphabet.index(ch)
        new_idx = (current_idx + index) % len(alphabet) # z 넘는 경우 처리하기 위해 나머지로
        answer += alphabet[new_idx]

    return answer

    # 도저히 안되는 코드
    # # 문자열 -> 리스트
    # s_list= list(s)
    # skip_list = list(skip)
    # print(s_list)
    # sToInt = []
    # skipToInt = []
    # answer =[]
    # # ord: 문자열을 아스키코드로 변환!
    # for s in s_list:
    #     sToInt.append(ord(s))
    
    # for k in skip_list:
    #     skipToInt.append(ord(k))
    
    # for t in sToInt:
    #     x = t
    #     for i in range(index):
    #         x += 1
    #         if (x > ord("z")): 
    #             x = ord("a")
    #         elif (x in skipToInt):
    #             for k in range(1, len(skip_list)+1):
    #                 if (k+x) in skipToInt: continue
    #                 else:
    #                     x += k
    #                     if (x+k > ord("z")): 
    #                         x = ord("a")
    #                     break
    #     answer.append(chr(x))

    # print(answer)
    # result = ''
    # for a in answer:
    #     result += a
    # print(result)


solution("aukks", "wbqd", 5)