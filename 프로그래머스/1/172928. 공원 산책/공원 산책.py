def solution(park, routes):
    answer = []

    row = len(park)
    col = len(park[0])
    arr = []
    for i in park:
        tmp = []
        for j in i:
            tmp.append(j)
        arr.append(tmp)

    # 시작 지점 찾기
    x = y = 0
    for i in range(row):
        for j in range(col):
            if arr[i][j] == 'S':
                x = i
                y = j

    def DFS(i,j,op,n):
        global x, y
        if op == 'N':
            for k in range(n):
                i -= 1
                if i < 0 or arr[i][j] == 'X':
                    return (-1,-1)
        elif op == 'S':
            for k in range(n):
                i += 1
                if i >= row or arr[i][j] == 'X':
                    return (-1,-1)
        elif op == 'W':
            for k in range(n):
                j -= 1
                if j < 0 or arr[i][j] == 'X':
                    return (-1,-1)
        else:
            for k in range(n):
                j += 1
                if j >= col or arr[i][j] == 'X':
                    return (-1,-1)
        return (i,j)

    for i in routes:
        xx,yy = DFS(x,y,i[0], int(i[-1]))
        if (xx != -1 and yy != -1):
            x,y = xx, yy

    answer.append(x)
    answer.append(y)
    return answer