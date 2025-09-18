import sys
from collections import deque
input = sys.stdin.readline
N, M, K, = map(int,input().split())
arr = [list(map(int,input().rstrip())) for _ in range(N)]
ch = [list([-1]*(K+1) for _ in range(M)) for _ in range(N)]
for i in range(K+1):
    ch[0][0][i] = 1

dx = [1,0,-1,0]
dy = [0,1,0,-1]

dq = deque()
dq.append((0,0,K))
while dq:
    x,y,r = dq.popleft()
    w = ch[x][y][r]
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<N and 0<=yy<M:
            if arr[xx][yy] == 0:
                if ch[xx][yy][r] == -1 or ch[xx][yy][r] > w+1:
                    ch[xx][yy][r] = w+1
                    dq.append((xx,yy,r))

            elif r > 0:
                if ch[xx][yy][r-1] == -1 or ch[xx][yy][r-1] > w+1:
                    ch[xx][yy][r-1] = w+1
                    dq.append((xx,yy,r-1))

if all(i == -1 for i in ch[N-1][M-1]):
    print(-1)
else:
    print(min(i for i in ch[N-1][M-1] if i != -1))