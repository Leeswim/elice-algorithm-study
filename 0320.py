#프로그래머스 Lv.2 전화번호 목록(해시)
#2023-03-20

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)):
        if i == len(phone_book) - 1:
            answer = True
        elif phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
            break
        else:
            answer = False
    return answer
