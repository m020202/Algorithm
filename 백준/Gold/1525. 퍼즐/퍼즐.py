def to_string(matrix):
    new_string = ""
    for i in range(3):
        for j in range(3):
            new_string += str(matrix[i][j])
    return new_string


import sys
from collections import deque
input = sys.stdin.readline
arr = [list(map(int,input().split())) for _ in range(3)]
ans = "123456780"
dx = [1,0,-1,0]
dy = [0,1,0,-1]
tot = 100000
ch = {}

tmp = to_string(arr)
ch[tmp] = 0
x = y = 0
for i in range(3):
    for j in range(3):
        if arr[i][j] == 0:
            x,y = i,j

dq = deque([(x,y,0,tmp)])
while dq:
    x,y,cnt,t = dq.popleft()
    box = [list(map(int,t[i:i+3])) for i in range(0,9,3)]
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<3 and 0<=yy<3:
            box[x][y], box[xx][yy] = box[xx][yy], box[x][y]
            tmp = to_string(box)
            if (tmp in ch and ch[tmp]>cnt+1) or tmp not in ch:
                ch[tmp] = cnt+1
                dq.append((xx,yy,cnt+1,tmp))
            box[x][y], box[xx][yy] = box[xx][yy], box[x][y]

if ans in ch:
    print(ch[ans])
else:
    print(-1)



