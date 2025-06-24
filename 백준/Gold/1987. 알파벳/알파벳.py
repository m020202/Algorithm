import sys
input = sys.stdin.readline
n,m = map(int,input().split())
box = [list(map(str,input())) for _ in range(n)]
for i in box:
    i.pop()
ans = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]

ch = [True] * 27
ch[ord(box[0][0]) -64] = False
def DFS(x,y,cnt):
    global ans
    tmp = True
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<n and 0<=yy<m:
            if ch[ord(box[xx][yy])-64] == True:
                ch[ord(box[xx][yy])-64] = False
                DFS(xx,yy,cnt+1)
                ch[ord(box[xx][yy])-64] = True
                tmp = False
    if tmp == True:
        ans = max(ans,cnt)

DFS(0,0,1)
print(ans)
