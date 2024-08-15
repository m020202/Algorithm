import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
box = [list(map(int,input().split())) for _ in range(n)]
dQ = deque(box)
dir = []
ans = [[0] * 101 for _ in range(101)]

while dQ:
    y,x,d,g = dQ.popleft()
    dir = [d]
    for i in range(g):
        for j in range(len(dir)-1,-1,-1):
            cur = dir[j]
            dir.append((cur+1)%4)
    ans[x][y] = 1
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]
    for i in dir:
        x += dx[i]
        y += dy[i]
        if 0<=x<=100 and 0<=y<=100:
            ans[x][y] = 1

tot = 0
for i in range(100):
    for j in range(100):
        if ans[i][j] == 1 and ans[i+1][j] == 1 and ans[i+1][j+1] == 1 and ans[i][j+1] == 1:
            tot += 1

print(tot)
            