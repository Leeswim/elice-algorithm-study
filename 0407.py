#챌린지 문제
#프로그래머스 Lv.2 순위 검색 (2021 KAKAO BLIND RECRUITMENT)
#2023-04-07

def solution(info, query):
    arr = []
    dic = {}
    for i in range(len(info)):
        temp = info[i].split()
        dic['lang'] = temp[0]
        dic['job'] = temp[1]
        dic['career'] = temp[2]
        dic['food'] = temp[3]
        dic['score'] = temp[4]
        arr.append(dic)
        dic = {}
    answer = []
    for n in range(len(query)):
        li = []
        if "cpp" in query[n] or "java" in query[n] or "python" in query[n]:
            if "cpp" in query[n]:
                for i in range(len(arr)):
                    if arr[i]['lang'] == "cpp":
                        li.append(arr[i])
            elif "java" in query[n]:
                for i in range(len(arr)):
                    if arr[i]['lang'] == "java":
                        li.append(arr[i])
            else:
                for i in range(len(arr)):
                    if arr[i]['lang'] == "python":
                        li.append(arr[i])
        else:
            li = arr
        li2 = []
        if "backend" in query[n] or "frontend" in query[n]:
            if "backend" in query[n]:
                for i in range(len(li)):
                    if li[i]['job'] == "backend":
                        li2.append(li[i])
            else:
                for i in range(len(li)):
                    if li[i]['job'] == "frontend":
                        li2.append(li[i])
        else:
            li2 = li
        li3 = []
        if "junior" in query[n] or "senior" in query[n]:
            if "junior" in query[n]:
                for i in range(len(li2)):
                    if li2[i]['career'] == "junior":
                        li3.append(li2[i])
            else:
                for i in range(len(li2)):
                    if li2[i]['career'] == "senior":
                        li3.append(li2[i])
        else:
            li3 = li2
        li4 = []
        if "chicken" in query[n] or "pizza" in query[n]:
            if "chicken" in query[n]:
                for i in range(len(li3)):
                    if li3[i]['food'] == "chicken":
                        li4.append(li3[i])
            else:
                for i in range(len(li3)):
                    if li3[i]['food'] == "pizza":
                        li4.append(li3[i])
        else:
            li4 = li3
        lis = query[n].split()
        li5 = []
        for i in range(len(li4)):
            if int(li4[i]['score']) >= int(lis[-1]):
                li5.append(li4[i])
        answer.append(len(li5))
    return answer
