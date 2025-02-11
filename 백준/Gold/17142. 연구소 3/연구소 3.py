import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(n)]

# 비활성 바이러스 위치 체크
deactivate = []
for i in range(n):
    for j in range(n):
        if box[i][j] == 2:
            deactivate.append((i,j))

dx = [1,0,-1,0]
dy = [0,1,0,-1]
def cal(bomb):
    dic = {} # 비활성 폭탄의 실질적 시간
    ch = [[-1] * n for _ in range(n)]
    # 벽들은 0으로 세팅
    for i in range(n):
        for j in range(n):
            if box[i][j] == 1:
                ch[i][j] = 0
            elif box[i][j] == 2:
                ch[i][j] = 0
                dic[(i,j)] = 10000

    for i in bomb:
        dic[i] = 0

    dq = deque(bomb)
    while dq:
        x,y = dq.popleft()
        cur = ch[x][y]
        if box[x][y] == 2:
            cur = dic[(x,y)]

        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0<=xx<n and 0<=yy<n:
                if box[xx][yy] == 0:
                    if ch[xx][yy] == -1 or ch[xx][yy] > cur + 1:
                        ch[xx][yy] = cur + 1
                        dq.append((xx,yy))

                # 폭탄이면, 실제 걸린 시간에서 제외시키기 위해 dic에 실제 시간 저장.
                elif box[xx][yy] == 2:
                    if dic[(xx,yy)] > cur + 1:
                        dic[(xx,yy)] = cur + 1
                        dq.append((xx,yy))

    mx = 0
    for i in range(n):
        for j in range(n):
            if ch[i][j] == -1:
                return -1
            mx = max(mx,ch[i][j])
    return mx

ans = -1
def func(cnt, bomb, next):
    global ans, box
    if cnt == m:
        res = cal(bomb)
        if res != -1:
            if ans == -1:
                ans = res
            else:
                ans = min(ans, res)
    else:
        for i in range(next+1, len(deactivate)):
            bomb.append(deactivate[i])
            func(cnt+1, bomb, i)
            bomb.pop()

func(0,[], -1)
print(ans)