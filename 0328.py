#프로그래머스 Lv.0 연속된 수의 합
#2023-03-28

def solution(num, total):
    answer = []
    if num == 1:
        answer.append(total)
    elif num % 2 == 1:
        div = total / num
        for i in range(1, int((num+1)/2)):
            answer.append(div - i)
        answer.reverse()
        answer.append(div)
        for i in range(1, int((num+1)/2)):
            answer.append(div + i)
    else:
        div = total // num
        if div < 0:
            div = round(div)
            for i in range(1, int(num/2)):
                answer.append(div - i)
            answer.reverse()
            answer.append(div)
            answer.append(div+1)
            for i in range(1, int(num/2)):
                answer.append(div + 1 + i)
        else:
            for i in range(1, int(num/2)):
                answer.append(div - i)
            answer.reverse()
            answer.append(div)
            answer.append(div+1)
            for i in range(1, int(num/2)):
                answer.append(div + 1 + i)       
    return answer
