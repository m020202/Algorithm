from collections import deque
n,m = map(int,input().split())
box = []

for _ in range(n):
    box.append(list(map(int,input().split())))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

ch = [[0] * m for _ in range(n)]
mx = 0

def checking(x,y):
    k = [0] * 4
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<n and 0<=yy<m:
            k[i] = box[xx][yy]
        
    result = box[x][y] + sum(k)
    ans = 0
    for i in range(4):
        ans = max(ans,result-k[i])
    return ans

def dfs(x,y,cnt,tot):
    global mx, ch
    if cnt == 4:
        mx = max(mx,tot)
        return
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<n and 0<=yy<m and ch[xx][yy] == 0:
            ch[xx][yy] = 1
            dfs(xx,yy,cnt+1,tot+box[xx][yy])
            ch[xx][yy] = 0

for i in range(n):
    for j in range(m):
        mx = max(checking(i,j), mx)
        ch[i][j] = 1
        dfs(i,j,1,box[i][j])
        ch[i][j] = 0
        

print(mx)
