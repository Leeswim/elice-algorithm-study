#챌린지 문제
#프로그래머스 Lv.1 크레인 인형뽑기 게임 (2019 카카오 개발자 겨울 인턴십)
#2023-04-15

def solution(board, moves):
    stack = []
    boom = 0
    for i in range(len(moves)):
        target = moves[i] - 1
        for j in range(len(board)):
            if board[j][target] != 0:
                if len(stack) >= 1 and stack[-1] == board[j][target]:
                    board[j][target] = 0
                    stack.pop()
                    boom += 2
                    break
                else:     
                    stack.append(board[j][target])
                    board[j][target] = 0
                    break
            else: continue
    answer = boom
    return answer
