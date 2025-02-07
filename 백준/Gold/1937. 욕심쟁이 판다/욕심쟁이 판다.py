import sys
sys.setrecursionlimit(300000)
input = sys.stdin.readline
n = int(input())
box = [list(map(int,input().split())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]
ch = [[0] * n for _ in range(n)]

def dfs(x,y):
    global ch
    if ch[x][y] != 0:
        return ch[x][y]
    cur = 0
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<n and 0<=yy<n:
            if box[xx][yy] < box[x][y]:
                cur = max(cur, dfs(xx,yy))
    ch[x][y] = cur + 1
    return cur + 1

for i in range(n):
    for j in range(n):
        if ch[i][j] == 0:
            dfs(i,j)

print(max(map(max,ch)))

