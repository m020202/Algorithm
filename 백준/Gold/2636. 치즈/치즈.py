import sys
from collections import deque
input = sys.stdin.readline
r,c = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(r)]
cnt = 0
for i in range(r):
    for j in range(c):
        if box[i][j] == 1:
            cnt += 1

dx = [1,0,-1,0]
dy = [0,1,0,-1]
hr = 0
def func():
    dQ = deque()
    dQ.append((0,0))
    melt = deque()
    while dQ:
        x,y = dQ.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<r and 0<=yy<c and ch[xx][yy] == 0:
                ch[xx][yy] = 1
                if box[xx][yy] == 0:
                    dQ.append((xx,yy))
                else:
                    melt.append((xx,yy))

    for i,j in melt:
        box[i][j] = 0
    return len(melt)

while True:
    ch = [[0] * c for _ in range(r)]
    tot = func()
    cnt -= tot
    hr += 1
    if cnt == 0:
        print(hr)
        print(tot)
        break

