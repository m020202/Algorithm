import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
arr = [list(map(str,input().rstrip())) for _ in range(N)]
E = []
B = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'B':
            B.append((i,j))
        elif arr[i][j] == 'E':
            E.append((i,j))
E = (*E[1],0 if E[0][0]==E[1][0] else 1)
B = (*B[1],0 if B[0][0]==B[1][0] else 1)

def is_tree(x,y,d):
    w = [-1,0,1]
    if d == 0:
        for i in w:
            if arr[x][y+i] == '1':
                return False
        return True
    else:
        for i in w:
            if arr[x+i][y] == '1':
                return False
        return True

def is_in(x,y,d):
    if d == 0 and 0<y<N-1 and 0<=x<=N-1:
        return True
    elif d == 1 and 0<x<N-1 and 0<=y<=N-1:
        return True
    return False

ch = [[[-1,-1] for _ in range(N)] for _ in range(N)]
ch[B[0]][B[1]][B[2]] = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

dq = deque([B])
while dq:
    x,y,d = dq.popleft()
    val = ch[x][y][d]
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if is_in(xx,yy,d) and is_tree(xx,yy,d):
            if ch[xx][yy][d] == -1 or ch[xx][yy][d] > val + 1:
                ch[xx][yy][d] = val + 1
                dq.append((xx,yy,d))
    if d:
        if is_in(x,y,1-d) and is_tree(x,y,1-d) and is_in(x-1,y,1-d) and is_tree(x-1,y,1-d) and is_in(x+1,y,1-d) and is_tree(x+1,y,1-d):
            if ch[x][y][1 - d] == -1 or ch[x][y][1 - d] > val + 1:
                ch[x][y][1 - d] = val + 1
                dq.append((x, y, 1 - d))
    else:
        if is_in(x,y,1-d) and is_tree(x,y,1-d) and is_in(x,y-1,1-d) and is_tree(x,y-1,1-d) and is_in(x,y+1,1-d) and is_tree(x,y+1,1-d):
            if ch[x][y][1 - d] == -1 or ch[x][y][1 - d] > val + 1:
                ch[x][y][1 - d] = val + 1
                dq.append((x, y, 1 - d))

if ch[E[0]][E[1]][E[2]] == -1:
    print(0)
else:
    print(ch[E[0]][E[1]][E[2]])