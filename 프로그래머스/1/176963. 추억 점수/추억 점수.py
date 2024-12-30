def solution(name, yearning, photo):
    answer = []

    dic = {}

    for i in range(len(name)):
        dic[name[i]] = yearning[i]

    s = set(name)
    for i in photo:
        tot = 0
        for j in i:
            if j in s:
                tot += dic[j]
        answer.append(tot)
    return answer

print(solution(["may", "kein", "kain", "radi"],[5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))