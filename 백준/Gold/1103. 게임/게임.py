import sys
input = sys.stdin.readline
n,m = map(int,input().split())
box = [list(map(str,input().rstrip())) for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
ch = [[-1]*m for _ in range(n)]
visit = [[0]*m for _ in range(n)]
def dfs(x,y):
    if ch[x][y] != -1:
        return ch[x][y]
    weight = int(box[x][y])
    num = 0
    visit[x][y] = 1
    for i in range(4):
        xx = x + dx[i]*weight
        yy = y + dy[i]*weight
        if 0<=xx<n and 0<=yy<m and box[xx][yy] != 'H':
            if visit[xx][yy] == 1:
                print(-1)
                sys.exit()
            else:
                num = max(num,dfs(xx,yy))
    ch[x][y] = num + 1
    visit[x][y] = 0
    return num + 1

dfs(0,0)
print(ch[0][0])

