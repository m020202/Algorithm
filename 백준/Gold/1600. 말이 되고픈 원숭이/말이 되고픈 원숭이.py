import sys
from collections import deque
input = sys.stdin.readline
k = int(input())
m,n = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(n)]

# 말처럼 갈 수 있는 경로
kx = [2,1,2,1,-2,-1,-2,-1]
ky = [1,2,-1,-2,1,2,-1,-2]

# 그냥 갈 수 있는 경로
dx = [1,0,-1,0]
dy = [0,1,0,-1]

ch = [[[-1 for _ in range(m)] for _ in range(n)] for _ in range(k+1)]
for i in range(k+1):
    ch[i][0][0] = 0

dq = deque()
dq.append((k,0,0))
while dq:
    cnt,x,y = dq.popleft()

    if cnt > 0:
        for i in range(8):
            xx = x + kx[i]
            yy = y + ky[i]
            if 0<=xx<n and 0<=yy<m:
                if box[xx][yy] == 0:
                    if ch[cnt-1][xx][yy] == -1:
                        ch[cnt-1][xx][yy] = ch[cnt][x][y] + 1
                        dq.append((cnt-1, xx, yy))
                    elif ch[cnt-1][xx][yy] > ch[cnt][x][y] + 1:
                        ch[cnt-1][xx][yy] = ch[cnt][x][y] + 1
                        dq.append((cnt-1, xx, yy))

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<n and 0<=yy<m:
            if box[xx][yy] == 0:
                if ch[cnt][xx][yy] == -1:
                    ch[cnt][xx][yy] = ch[cnt][x][y] + 1
                    dq.append((cnt, xx, yy))
                elif ch[cnt][xx][yy] > ch[cnt][x][y] + 1:
                    ch[cnt][xx][yy] = ch[cnt][x][y] + 1
                    dq.append((cnt, xx, yy))

ans = sys.maxsize
tmp = False
for i in range(k+1):
    if ch[i][n-1][m-1] != -1:
        tmp = True
        ans = min(ans, ch[i][n-1][m-1])
if not tmp:
    print(-1)
else:
    print(ans)

