import sys
input = sys.stdin.readline
sys.setrecursionlimit(50000)
n,m = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(n)]

# 4가지 방향
dx = [1,0,-1,0]
dy = [0,1,0,-1]

dp = [[-1] * m for _ in range(n)]
dp[0][0] = 1
def dfs(x,y):
    global dp
    if dp[x][y] != -1:
        return dp[x][y]

    cur = box[x][y]
    tot = 0
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<n and 0<=yy<m:
            if cur < box[xx][yy]:
                tot += dfs(xx,yy)
    dp[x][y] = tot
    return tot

print(dfs(n-1,m-1))
