#프로그래머스 Lv.1 숫자 문자열과 영단어(2021 카카오 채용연계형 인턴십)
#2023-03-22

def solution(s):
    while True:
        if "zero" in s:
            s = s.replace('zero', '0')
        elif "one" in s:
            s = s.replace('one', '1')
        elif "two" in s:
            s = s.replace('two', '2')
        elif "three" in s:
            s = s.replace('three', '3')
        elif "four" in s:
            s = s.replace('four', '4')
        elif "five" in s:
            s = s.replace('five', '5')
        elif "six" in s:
            s = s.replace('six', '6')
        elif "seven" in s:
            s = s.replace('seven', '7')
        elif "eight" in s:
            s = s.replace('eight', '8')
        elif "nine" in s:
            s = s.replace('nine', '9')
        else:
            s = s
        
        try: answer = int(s)
        except: continue
        else: break
        
    return answer
