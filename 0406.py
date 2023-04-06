#프로그래머스 Lv.0 등수 매기기
#2023-04-06

def solution(score):
    arr = []
    for i in range(len(score)):
        arr.append((score[i][0] + score[i][1])/2)
    answer = []
    sort = sorted(arr, reverse = True)
    for i in arr:
        answer.append(sort.index(i)+1)
    return answer
