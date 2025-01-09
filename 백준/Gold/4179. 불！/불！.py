import copy
import sys
from collections import deque
import heapq

r,c = map(int,input().split())
box = [list(map(str,input())) for _ in range(r)]

fire = []
for i in range(r):
    for j in range(c):
        if box[i][j] == 'J':
            x,y = i,j
            box[i][j] = '.'
        elif box[i][j] == 'F':
            fire.append((i,j))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

heap = []
heapq.heappush(heap, (0,x,y))

F = 0 # 불 시간
ch = [[-1] * c for _ in range(r)]
ch[x][y] = 0

def update(newFire):
    global box
    res = []
    while newFire:
        x,y = newFire.pop()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<r and 0<=yy<c:
                if box[xx][yy] != 'F' and box[xx][yy] != '#':
                    res.append((xx,yy))
                    box[xx][yy] = 'F'
    return res

while heap:
    num,x,y = heapq.heappop(heap)
    if F <= num:
        F += 1
        fire = update(fire)

    # 지훈이 위치
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<r and 0<=yy<c:
            if box[xx][yy] != 'F' and box[xx][yy] != '#':
                if ch[xx][yy] == -1:
                    ch[xx][yy] = num + 1
                    heapq.heappush(heap, (num + 1, xx, yy))
                elif ch[xx][yy] > num + 1:
                    ch[xx][yy] = num + 1
                    heapq.heappush(heap, (num + 1, xx, yy))

ans = -1
for i in range(r):
    for j in range(c):
        if i == 0 or i == r-1 or j == 0 or j == c-1:
            if ch[i][j] != -1:
                if ans == -1:
                    ans = ch[i][j]
                else:
                    ans = min(ans,ch[i][j])

if ans == -1:
    print("IMPOSSIBLE")
else:
    print(ans+1)





