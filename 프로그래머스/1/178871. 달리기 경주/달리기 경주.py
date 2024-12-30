def solution(players, callings):
    answer = []

    dic = {}
    for i in range(len(players)):
        dic[players[i]] = i

    for i in callings:
        idx = dic[i]
        tmp = players[idx-1]
        players[idx-1] = players[idx]
        players[idx] = tmp
        dic[i] -= 1
        dic[tmp] += 1

    answer = players
    return answer