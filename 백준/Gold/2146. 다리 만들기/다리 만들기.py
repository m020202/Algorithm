import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
box = [list(map(int,input().split())) for _ in range(n)]
spot = [[0]*n for _ in range(n)]

# 영역 구분
cur = 1
dx = [1,0,-1,0]
dy = [0,1,0,-1]
land = []
for i in range(n):
    for j in range(n):
        if spot[i][j] == 0 and box[i][j] == 1:
            dq = deque([(i,j)])
            land.append((i,j,cur))
            while dq:
                x,y = dq.popleft()
                for k in range(4):
                    xx = x + dx[k]
                    yy = y + dy[k]
                    if 0<=xx<n and 0<=yy<n:
                        if spot[xx][yy] == 0 and box[xx][yy] == 1:
                            spot[xx][yy] = cur
                            dq.append((xx,yy))
                            land.append((xx,yy,cur))
            cur += 1

# 한 영역 다른 영역 min 구하기
mn = sys.maxsize
for i in range(len(land)):
    for j in range(i+1, len(land)):
        if land[i][2] != land[j][2]:
            val = abs(land[i][0]-land[j][0]) + abs(land[i][1]-land[j][1]) - 1
            if val < mn:
                mn = val

print(mn)
