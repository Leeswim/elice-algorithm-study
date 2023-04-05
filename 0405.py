#프로그래머스 Lv.0 다항식 더하기
#2023-04-05

def solution(polynomial):
    arr = polynomial.split(" ")
    for i in range(arr.count("+")):
        arr.remove("+")
    x = 0
    s = 0
    for i in range(len(arr)):
        if arr[i][-1] == "x":
            if arr[i] == "x":
                x += 1
            else:
                x += int(arr[i][:-1])
        else:
            s += int(arr[i])
    if x == 0:
        answer = str(s)
    elif x == 1:
        if s == 0:
            answer = "x"
        else:
            answer = "x + " + str(s)
    else:
        if s > 0:
            answer = str(x) + "x + " + str(s)
        else:
            answer = str(x) + "x"
    return answer
