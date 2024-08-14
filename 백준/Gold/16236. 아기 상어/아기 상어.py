import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize
n = int(input())
box = [list(map(int,input().split())) for _ in range(n)]
# 상어 크기
size = 2
# 상어 위치
a,b = 0,0
# 총 물고기 수
cnt = 0
for i in range(n):
    for j in range(n):
        if box[i][j] == 9:
            a,b = i,j
        elif box[i][j] != 0:
            cnt += 1

tot = 0
cur = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]
while cnt:
    ansX,ansY = -1, -1
    dist = INF
    ch = [[-1] * n for _ in range(n)]
    ch[a][b] = 0
    dQ = deque()
    dQ.append((a,b))
    while dQ:
        curX, curY = dQ.popleft()
        num = ch[curX][curY]
        if num > dist:
            continue
        for i in range(4):
            xx = curX + dx[i]
            yy = curY + dy[i]
            if 0<=xx<n and 0<=yy<n:
                if ch[xx][yy] == -1:
                    if box[xx][yy] == 0 or box[xx][yy] == size:
                        ch[xx][yy] = num + 1
                        dQ.append((xx,yy))
                    elif box[xx][yy] < size:
                        ch[xx][yy] = num + 1
                        dQ.append((xx,yy))
                        if num + 1 < dist:
                            dist = num + 1
                            ansX = xx
                            ansY = yy
                        elif num + 1 == dist:
                            if xx < ansX:
                                dist = num + 1
                                ansX = xx
                                ansY = yy
                            elif xx == ansX:
                                if yy < ansY:
                                    dist = num + 1
                                    ansX = xx
                                    ansY = yy
    if ansX == -1 and ansY == -1:
        break
    else:
        box[a][b] = 0
        a = ansX
        b = ansY
        box[a][b] = 9
        cur += 1
        if size == cur:
            size += 1
            cur = 0
        tot += dist
        cnt -= 1

print(tot)