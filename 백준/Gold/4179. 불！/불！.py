import sys
from collections import deque
input = sys.stdin.readline
r,c = map(int,input().split())
box = [list(map(str,input().rstrip())) for _ in range(r)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

x = y = 0 # 지호 초기 위치
fireTime = [[-1]*c for _ in range(r)]
dq = deque()
for i in range(r):
    for j in range(c):
        if box[i][j] == 'J':
            x,y = i,j
        if box[i][j] == 'F':
            fireTime[i][j] = 0
            dq.append((i,j))

# 위치별 불 확산 시간 파악
while dq:
    curX, curY = dq.popleft()
    val = fireTime[curX][curY] + 1
    for i in range(4):
        nxtX = curX + dx[i]
        nxtY = curY + dy[i]
        if 0<=nxtX<r and 0<=nxtY<c:
            if box[nxtX][nxtY] !='#':
                if fireTime[nxtX][nxtY] == -1 or fireTime[nxtX][nxtY] > val:
                    fireTime[nxtX][nxtY] = val
                    dq.append((nxtX,nxtY))

# 지호 위치 최단거리 파악
ch = [[-1]*c for _ in range(r)]
ch[x][y] = 0
dq = deque([(x,y)])
while dq:
    curX,curY = dq.popleft()
    val = ch[curX][curY] + 1
    for i in range(4):
        nxtX = curX + dx[i]
        nxtY = curY + dy[i]
        if 0<=nxtX<r and 0<=nxtY<c:
            if box[nxtX][nxtY] != '#':
                if ch[nxtX][nxtY] == -1 or ch[nxtX][nxtY] > val:
                    if fireTime[nxtX][nxtY] > val or fireTime[nxtX][nxtY] == -1:
                        ch[nxtX][nxtY] = val
                        dq.append((nxtX,nxtY))

mn = sys.maxsize
for i in range(r):
    for j in range(c):
        if i == 0 or i == r-1 or j == 0 or j == c-1:
            if ch[i][j] != -1:
                mn = min(mn, ch[i][j])

print(mn+1 if mn != sys.maxsize else 'IMPOSSIBLE')


