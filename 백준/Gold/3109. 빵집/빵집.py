import sys
from collections import deque
input = sys.stdin.readline
r,c = map(int,input().split())
box = [list(map(str,input().rstrip())) for _ in range(r)]
dx = [-1,0,1]
ans = 0
def dfs(x,y):
    global ans
    if y == c-1:
        ans += 1
        return True
    for i in range(3):
        xx = x + dx[i]
        yy = y + 1
        if 0<=xx<r and 0<=yy<c:
            if box[xx][yy] == '.':
                box[xx][yy] = 'x'
                if dfs(xx,yy):
                    return True
    return False

for i in range(r):
    dfs(i,0)

print(ans)