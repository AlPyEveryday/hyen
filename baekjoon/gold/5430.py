from collections import deque

N = int(input())

for _ in range(N):
    flag = 0
    string = input()
    m = int(input())
    temp_arr = input()

    # 숫자 개수 따라 스플라이싱 달라짐
    if m > 1:
        arr = temp_arr[1:-1].split(",")
        arr = [int(x) for x in arr]
    elif m == 1:
        arr = [int(temp_arr[1:-1])]
    elif m == 0:
        arr = []
    queue = deque(arr)

    for s in string:
        if s == "R":
            if flag == 1: flag = 0
            elif flag == 0: flag = 1
        elif s == "D":
            if len(queue) < 1:
                print("error")
                flag = -1
                break
            if flag == 0:
                queue.popleft()
            elif flag == 1:
                queue.pop()
    
    if flag == 0:
        print("[" + ",".join(map(str, list(queue))) + "]") #list로 변환해야함
    elif flag == 1:
        print("[" + ",".join(map(str, list(queue)[::-1])) + "]") #리스트 거꾸로 출력하기

    # 위에서 str = input() 으로 썼었더니 타입 오류남
    # 출력이 공백없이 나와야 해서 요소 사이에 "," 추가하는 ",".join(리스트)를 사용하는것