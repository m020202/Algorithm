import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
arr = [list(map(str,input().rstrip())) for _ in range(N)]
E = ()
B = ()
for i in range(N*N):
    x = i//N
    y = i%N
    if not B and arr[x][y] == 'B':
        if 0<=y+1<N and arr[x][y+1] == 'B':
            B = ((x,y+1),0)
        elif 0<=x+1<N and arr[x+1][y] == 'B':
            B = ((x+1,y),1)
    if not E and arr[x][y] == 'E':
        if 0<=y+1<N and arr[x][y+1] == 'E':
            E = ((x,y+1),0)
        elif 0<=x+1<N and arr[x+1][y] == 'E':
            E = ((x+1,y),1)

def U(B):
    x,y = B[0]
    if B[1] == 0:
        box = [(x,y-1), (x,y), (x,y+1)]
    else:
        box = [(x-1,y), (x,y), (x+1,y)]
    for i,j in box:
        if i == 0:
            return (False, B)
        if arr[i - 1][j] == '1':
            return (False,B)
    return (True,((x-1,y),B[1]))

def D(B):
    x,y = B[0]
    if B[1] == 0:
        box = [(x,y-1), (x,y), (x,y+1)]
    else:
        box = [(x-1,y), (x,y), (x+1,y)]
    for i,j in box:
        if i == N-1:
            return (False, B)
        if arr[i + 1][j] == '1':
            return (False, B)
    return (True,((x+1,y),B[1]))

def L(B):
    x,y = B[0]
    if B[1] == 0:
        box = [(x,y-1), (x,y), (x,y+1)]
    else:
        box = [(x-1,y), (x,y), (x+1,y)]
    for i,j in box:
        if j == 0:
            return (False, B)
        if arr[i][j - 1] == '1':
            return (False, B)
    return (True,((x,y-1),B[1]))

def R(B):
    x,y = B[0]
    if B[1] == 0:
        box = [(x,y-1), (x,y), (x,y+1)]
    else:
        box = [(x-1,y), (x,y), (x+1,y)]
    for i,j in box:
        if j == N-1:
            return (False, B)
        if arr[i][j + 1] == '1':
            return (False, B)
    return (True,((x,y+1),B[1]))

def T(B):
    x,y = B[0]
    dx = [-1,-1,-1,0,1,1,1,0]
    dy = [-1,0,1,1,1,0,-1,-1]
    for i in range(8):
        xx = x + dx[i]
        yy = y + dy[i]
        if not (0<=xx<N and 0<=yy<N):
            return (False, B)
        if arr[xx][yy] == '1':
            return (False, B)
    return (True, ((x,y),1-B[1]))

ans = sys.maxsize
ch = [[[-1,-1] for _ in range(N)] for _ in range(N)]
ch[B[0][0]][B[0][1]][B[1]] = 0

dq = deque([B])
while dq:
    B = dq.popleft()
    val = ch[B[0][0]][B[0][1]][B[1]]

    res, tmp = U(B)
    cur = ch[tmp[0][0]][tmp[0][1]][tmp[1]]
    if res and cur == -1 or cur > val + 1:
        ch[tmp[0][0]][tmp[0][1]][tmp[1]] = val + 1
        dq.append(tmp)

    res, tmp = D(B)
    cur = ch[tmp[0][0]][tmp[0][1]][tmp[1]]
    if res and cur == -1 or cur > val + 1:
        ch[tmp[0][0]][tmp[0][1]][tmp[1]] = val + 1
        dq.append(tmp)

    res, tmp = L(B)
    cur = ch[tmp[0][0]][tmp[0][1]][tmp[1]]
    if res and cur == -1 or cur > val + 1:
        ch[tmp[0][0]][tmp[0][1]][tmp[1]] = val + 1
        dq.append(tmp)

    res, tmp = R(B)
    cur = ch[tmp[0][0]][tmp[0][1]][tmp[1]]
    if res and cur == -1 or cur > val + 1:
        ch[tmp[0][0]][tmp[0][1]][tmp[1]] = val + 1
        dq.append(tmp)

    res, tmp = T(B)
    cur = ch[tmp[0][0]][tmp[0][1]][tmp[1]]
    if res and cur == -1 or cur > val + 1:
        ch[tmp[0][0]][tmp[0][1]][tmp[1]] = val + 1
        dq.append(tmp)


if ch[E[0][0]][E[0][1]][E[1]] == -1:
    print(0)
else:
    print(ch[E[0][0]][E[0][1]][E[1]])