import sys
from collections import deque
input = sys.stdin.readline
n,m, limit = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(n)]
x,y = map(int,input().split()) # 출발지점
x-=1
y-=1
psg = {}
for _ in range(m):
    a,b,c,d = map(int,input().split())
    psg[(a-1,b-1,c-1,d-1)] = True

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def search_passenger(x,y,psg):
    dq = deque([(x,y)])
    ch = [[-1] * n for _ in range(n)]
    ch[x][y] = 0
    while dq:
        curX, curY = dq.popleft()
        val = ch[curX][curY] + 1
        for i in range(4):
            newX = curX + dx[i]
            newY = curY + dy[i]
            if 0<=newX<n and 0<=newY<n and box[newX][newY] == 0:
                if ch[newX][newY] == -1 or ch[newX][newY] > val:
                    ch[newX][newY] = val
                    dq.append((newX,newY))

    mn = sys.maxsize
    ans = (100,100)
    if all(ch[i][j] == -1 for i,j,k,l in psg):
        print(-1)
        sys.exit()

    for i in psg:
        if (ch[i[0]][i[1]],i[0],i[1]) < (mn,ans[0],ans[1]):
            mn = ch[i[0]][i[1]]
            ans = i

    return mn,ans

def BFS(x,y,xx,yy):
    dq = deque([(x, y)])
    ch = [[-1] * n for _ in range(n)]
    ch[x][y] = 0
    while dq:
        curX, curY = dq.popleft()
        val = ch[curX][curY] + 1
        for i in range(4):
            newX = curX + dx[i]
            newY = curY + dy[i]
            if 0 <= newX < n and 0 <= newY < n and box[newX][newY] == 0:
                if ch[newX][newY] == -1 or ch[newX][newY] > val:
                    ch[newX][newY] = val
                    dq.append((newX, newY))
    return ch[xx][yy]

while True:
    if not psg:
        print(limit)
        break

    w,cur = search_passenger(x,y,psg)
    if w > limit:
        print(-1)
        break

    limit -= w
    x,y = cur[0], cur[1]
    psg.pop(cur)
    result = BFS(x,y,cur[2],cur[3])
    if result == -1 or result > limit:
        print(-1)
        break
    else:
        limit += result
        x,y = cur[2],cur[3]




