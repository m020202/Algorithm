def solution(s):
    answer = True
    box = list(map(str,s))
    lt = 0

    for i in box:
        if (i == '('):
            lt += 1
        else:
            if (lt > 0):
                lt -= 1
            else:
                return False

    if lt > 0:
        return False
    return True