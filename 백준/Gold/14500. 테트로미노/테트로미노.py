import sys
input = sys.stdin.readline
n,m = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(n)]

ans = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]
ch = [[0] * m for _ in range(n)]
def dfs(cur, tot, x, y):
    global ans
    if cur == 4:
        ans = max(ans, tot)
        return

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<n and 0<=yy<m:
            if ch[xx][yy] == 0:
                ch[xx][yy] = 1
                dfs(cur+1,tot+box[xx][yy],xx,yy)
                ch[xx][yy] = 0

for i in range(n):
    for j in range(m):
        ch[i][j] = 1
        dfs(1,box[i][j],i,j)
        ch[i][j] = 0

def fuck_shape(x,y):
    global ans
    cur = box[x][y]
    # ㅓ 모양
    if 1<=y and 1<=x<n-1:
        ans = max(ans,cur + box[x][y-1] + box[x+1][y] + box[x-1][y])

    # ㅜ 모양
    if 1<=y<m-1 and x<n-1:
        ans = max(ans,cur + box[x][y-1] + box[x+1][y] + box[x][y+1])

    # ㅏ 모양
    if y<m-1 and 1<=x<n-1:
        ans = max(ans,cur + box[x+1][y] + box[x][y+1] + box[x-1][y])

    # ㅗ 모양
    if 1<=y<m-1 and 1<=x:
        ans = max(ans,cur + box[x][y-1] + box[x-1][y] + box[x][y+1])

for i in range(n):
    for j in range(m):
        fuck_shape(i,j)

print(ans)

