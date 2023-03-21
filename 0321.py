#프로그래머스 Lv.1 완주하지 못한 선수(해시)
#2023-03-21

def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion.append("")
    i = 0
    while participant[i] == completion[i]:
        i+=1
    answer = participant[i]
    return answer
