#챌린지 문제
#프로그래머스 Lv.1 신규 아이디 추천 (2021 KAKAO BLIND RECRUITMENT)
#2023-03-24

def solution(new_id):
    new_id = new_id.lower()
    banned = ['~', "'", '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '=', '+', '[', '{', ']', '}', ':', '?', ',', '<', '>', '/']
    i = 0
    while i < len(new_id):
        if new_id[i] in banned:
            new_id = new_id.replace(new_id[i], '')
        else: i = i + 1
    
    i = 0
    if len(new_id) >= 2:
        while i < len(new_id) - 1:
            if new_id[i] == '.' and new_id[i+1] == '.':
                new_id = new_id[:i] + new_id[i+1:]
            else: i = i + 1
    elif new_id == '..':
        new_id = 'a'
    else: pass
    
    if len(new_id) >= 2:
        if new_id[0] == '.':
            new_id = new_id[1:]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    elif new_id == '.':
        new_id = ''
    else:
        pass
    
    if len(new_id) == 0:
        new_id = 'a'
        
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    elif len(new_id) <= 2:
        while len(new_id) < 3:
            new_id = new_id + new_id[-1]
    else: pass
    
    answer = new_id
    return answer
