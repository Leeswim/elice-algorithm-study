#프로그래머스 Lv.1 모의고사 (완전탐색)
#2023-03-27

import math
def solution(answers):
    num1 = [1, 2, 3, 4, 5] * int((10000/5))
    num2 = [2, 1, 2, 3, 2, 4, 2, 5] * int((10000/8))
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * int((10000/10))
    length = len(answers)
    num1 = num1[:length]
    num2 = num2[:length]
    num3 = num3[:length]
    num1_cnt = 0
    num2_cnt = 0
    num3_cnt = 0
    for i in range(length):
        if answers[i] == num1[i]:
            num1_cnt = num1_cnt + 1
        if answers[i] == num2[i]:
            num2_cnt = num2_cnt + 1
        if answers[i] == num3[i]:
            num3_cnt = num3_cnt + 1
    level = []
    level.append(num1_cnt)
    level.append(num2_cnt)
    level.append(num3_cnt)
    maxnum = max(level)
    answer = []
    for i in range(len(level)):
        if level[i] == maxnum:
            answer.append(i+1)
    return answer
