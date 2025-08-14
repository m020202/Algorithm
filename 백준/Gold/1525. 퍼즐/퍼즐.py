def to_tuple(matrix):
    new_tuple = ()
    for i in range(3):
        for j in range(3):
            new_tuple += (matrix[i][j],)
    return new_tuple


import sys
from collections import deque
input = sys.stdin.readline
arr = [list(map(int,input().split())) for _ in range(3)]
ans = (1,2,3,4,5,6,7,8,0)
dx = [1,0,-1,0]
dy = [0,1,0,-1]
tot = 100000
ch = {}

tmp = to_tuple(arr)
ch[tmp] = 0
x = y = 0
for i in range(3):
    for j in range(3):
        if arr[i][j] == 0:
            x,y = i,j

dq = deque([(x,y,0,tmp)])
while dq:
    x,y,cnt,t = dq.popleft()
    box = [list(t[i:i+3]) for i in range(0,9,3)]
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<3 and 0<=yy<3:
            box[x][y], box[xx][yy] = box[xx][yy], box[x][y]
            tmp = to_tuple(box)
            if (tmp in ch and ch[tmp]>cnt+1) or tmp not in ch:
                ch[tmp] = cnt+1
                dq.append((xx,yy,cnt+1,tmp))
            box[x][y], box[xx][yy] = box[xx][yy], box[x][y]

if ans in ch:
    print(ch[ans])
else:
    print(-1)


