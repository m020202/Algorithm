import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(n)]

def BFS():
    ch = [[0]*m for _ in range(n)]
    cnt = 0
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    dQ = []
    dQ = deque(dQ)
    for i in range(n):
        for j in range(m):
            if box[i][j] == 2 and ch[i][j] == 0:
                ch[i][j] = 1
                dQ.append((i,j))
                while dQ:
                    now = dQ.popleft()
                    for k in range(4):
                        xx = now[0] + dx[k]
                        yy = now[1] + dy[k]
                        if 0<=xx<n and 0<=yy<m:
                            if box[xx][yy] == 0 or box[xx][yy] == 2:
                                if ch[xx][yy] == 0:
                                    ch[xx][yy] = 1
                                    dQ.append((xx,yy))
    for i in range(n):
        for j in range(m):
            if box[i][j] == 0 and ch[i][j] == 0:
                cnt += 1
    return cnt
ans = 0
def DFS(x,lt,rt):
    global ans
    if x == 3:
        ans = max(ans,BFS())
        return
    for i in range(lt,n):
        for j in range(m):
            if i == lt and j <= rt:
                continue
            if box[i][j] == 0:
                box[i][j] = 1
                DFS(x+1,i,j)
                box[i][j] = 0

DFS(0,0,-1)
print(ans)