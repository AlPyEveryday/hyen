def solution(video_len, pos, op_start, op_end, commands):
    # 모든 시간을 전부 초 단위로 바꿈
    min, sec = video_len.split(":")
    total_sec = int(min)*60 + int(sec)

    p_min, p_sec = pos.split(":")
    p_minToSec = int(p_min)*60 + int(p_sec)

    op_m, op_s = op_start.split(":")
    opStart = int(op_m)*60 + int(op_s)

    op_em, op_es = op_end.split(":")
    opEnd = int(op_em)*60 + int(op_es)

    # 시작 지점이 오프닝 사이라면 스킵
    if (p_minToSec >= opStart) and (p_minToSec <= opEnd): p_minToSec = opEnd

    # 명령어 따라서 초 옮김
    for c in commands:
        if c == "next" and (p_minToSec + 10) <= total_sec: p_minToSec += 10
        elif c == "next" and (p_minToSec + 10) > total_sec: p_minToSec = total_sec
        elif c == "prev" and (p_minToSec - 10) >= 0 : p_minToSec -= 10
        elif c == "prev" and (p_minToSec - 10) < 0 : p_minToSec = 0
        # 시간 이동후 오프닝 사이라면 스킵
        if (p_minToSec >= opStart) and (p_minToSec <= opEnd): p_minToSec = opEnd

    # 다시 분, 초로 바꾸고 문자열로 변경
    f_min = str(p_minToSec//60)
    f_sec = str(p_minToSec%60)
    # 
    if len(f_min) == 1: f_min = "0" + f_min
    if len(f_sec) == 1: f_sec = "0" + f_sec
    return("%s:%s" %(f_min,f_sec))

    

print(solution("07:22", "04:05", "00:15", "04:07", ["next"]))