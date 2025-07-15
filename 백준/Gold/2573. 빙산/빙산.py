import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def checking(ch): # 두 덩어리 이상 체크
    tmp = [[0]*m for _ in range(n)]
    cnt = 1
    for i in range(n):
        for j in range(m):
            if ch[i][j] > 0 and tmp[i][j] == 0:
                if cnt > 1:
                    return True
                tmp[i][j] = cnt
                dq = deque([(i,j)])
                while dq:
                    x,y = dq.popleft()
                    for k in range(4):
                        xx = x + dx[k]
                        yy = y + dy[k]
                        if 0<=xx<n and 0<=yy<m:
                            if ch[xx][yy] > 0 and tmp[xx][yy] == 0:
                                tmp[xx][yy] = cnt
                                dq.append((xx,yy))
                cnt += 1
    return False

island = {}
for i in range(n):
    for j in range(m):
        if box[i][j] > 0:
            island[(i,j)] = True

year = 0
res = True
while True:
    if res and checking(box):
        print(year)
        sys.exit()
    if not island:
        print(0)
        sys.exit()

    tmp = []
    for i,j in island:
        cnt = 0
        for k in range(4):
            ii = i + dx[k]
            jj = j + dy[k]
            if n > ii >= 0 == box[ii][jj] and 0<=jj<m:
                cnt += 1

        new = box[i][j] - cnt if box[i][j] > cnt else 0
        tmp.append((i,j,new))

    res = False
    for i,j,new in tmp:
        box[i][j] = new
        if new == 0:
            res = True
            island.pop((i,j))

    year += 1



