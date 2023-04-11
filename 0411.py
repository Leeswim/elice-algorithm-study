#프로그래머스 Lv.0 로그인 성공?
#2023-04-11

def solution(id_pw, db):
    answer = ''
    for i in range(len(db)):
        if db[i][0] == id_pw[0]:
            if db[i][1] == id_pw[1]:
                answer = "login"
                return answer
            else:
                answer = "wrong pw"
                break
        else:
            answer = "fail"
    return answer
