#프로그래머스 Lv.0 다음에 올 숫자
#2023-03-23

def solution(common):
    pm = []
    md = []
    for i in range(len(common)-1):
        if 0 in common:
            pm.append(common[i+1] - common[i])
        else:
            pm.append(common[i+1] - common[i])
            md.append(common[i+1] / common[i])
        
    if len(list(set(pm))) == 1:
        if common[0] == common[1]:
            answer = common[-1]
        else:
            answer = common[-1] + pm[0]
    elif len(list(set(md))) == 1:
        if common[0] == common[1]:
            answer = common[-1]
        else:
            answer = common[-1] * md[0]
    else:
        pass

    return answer
