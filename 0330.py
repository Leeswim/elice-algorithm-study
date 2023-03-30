#프로그래머스 Lv.1 K번째수 (정렬)
#2023-03-30

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        new_array = array[commands[i][0]-1:commands[i][1]]
        new_array.sort()
        answer.append(new_array[commands[i][2]-1])
    return answer
