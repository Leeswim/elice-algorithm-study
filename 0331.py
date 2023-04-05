#챌린지 문제
#프로그래머스 Lv.1 신고 결과 받기 (2022 KAKAO BLIND RECRUITMENT)
#2023-03-31

def solution(id_list, report, k):
    answer = [0]*len(id_list)
    temp = []
    report_list = []
    check = []
    for i in range(len(report)):
        a, b = report[i].split()
        temp.append(b)
        check.append([a, b])
    check_temp = []
    for i in range(len(check)):
        if check[i] not in check_temp:
            check_temp.append(check[i])
        else: pass
    check = check_temp
    for i in range(len(id_list)):
        if temp.count(id_list[i]) >= k:
            report_list.append(id_list[i])
    for i in range(len(report_list)):
        for j in range(len(check)):
            if check[j][1] == report_list[i] and len(check) != 1:
                answer[id_list.index(check[j][0])] = answer[id_list.index(check[j][0])] + 1
                
    return answer
