#프로그래머스 Lv.1 폰켓몬 (해시)
#2023-03-29

def solution(nums):
    n = len(nums) / 2
    test = []
    for i in range(len(nums)):
        if nums[i] not in test:
            test.append(nums[i])
    if n < len(test):
        answer = n
    else:
        answer = len(test)
    return answer
