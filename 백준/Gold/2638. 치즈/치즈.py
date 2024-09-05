import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
hr = 0
while True:
    ans = []
    dQ = deque()
    dQ.append((0,0))
    # 각 칸의 치즈가 공기와 접촉한 횟수
    contact = [[0] * m for _ in range(n)] 
    ch = [[0] * m for _ in range(n)]
    ch[0][0] = 1
    while dQ:
        x,y = dQ.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<n and 0<=yy<m:
                if box[xx][yy] == 1:
                    if contact[xx][yy] == 1:
                        ans.append((xx,yy))
                    else:
                        contact[xx][yy] = 1
                else:
                    if ch[xx][yy] == 0:
                        ch[xx][yy] = 1
                        dQ.append((xx,yy))
    if len(ans) == 0:
        print(hr)
        break
    for i,j in ans:
        box[i][j] = 0
    hr += 1