import sys,math
from collections import deque
input = sys.stdin.readline
n = int(input())
box = [list(map(int,input().split())) for _ in range(n)]
dragon = [[0] * 101 for _ in range(101)]

# k: 포함된 좌표들, d: 방향, g: 최종 세대, cur: 현재 세대, s: 시작점
def shift(k,g,cur,s,origin):
    if cur > g:
        return
    x,y = s
    newK = []
    mx = 0
    c1,c2 = -1, -1
    for i in k:
        curX,curY = i[0],i[1]
        newX,newY = -1,-1
        if curX > x and curY < y:
            newX = x-(y-curY)
            newY = y-(curX-x)
        elif curX == x and curY < y:
            newX = x-(y-curY)
            newY = y
        elif curX < x and curY < y:
            newX = x-(y-curY)
            newY = y+(x-curX)
        elif curX < x and curY == y:
            newX = x
            newY = y + (x-curX)
        elif curX < x and curY > y:
            newX = x+(curY-y)
            newY = y+(x-curX)
        elif curX == x and curY > y:
            newX = x+(curY-y)
            newY = y
        elif curX > x and curY > y:
            newX = x+(curY-y)
            newY = y-(curX-x)
        elif curX > x and curY == y:
            newX = x
            newY = y-(curX-x)
        else:
            newX = x
            newY = y
        if 0<=newX<=100 and 0<=newY<=100:
            dragon[newX][newY] = 1
            newK.append((newX,newY))
        if curX == origin[0] and curY == origin[1]:
            c1,c2 = newX,newY
    return shift(k+newK,g,cur+1,(c1,c2),origin)

def cuv(x,y,d,g):
    k = [(x,y)]
    if d == 0:
        if y + 1 <=  100:
            k.append((x,y+1))
    elif d == 1:
        if x -1 >= 0:
            k.append((x-1,y))
    elif d == 2:
        if y - 1 >= 0:
            k.append((x,y-1))
    else:
        if x + 1 <= 100:
            k.append((x+1,y))
    dragon[x][y] = 1
    dragon[k[-1][0]][k[-1][1]] = 1
    if g == 0:
        return
    return shift(k,g,1,k[-1],(x,y))

dQ = deque(box)
while dQ:
    x,y,d,g = dQ.popleft()
    cuv(y,x,d,g)

ans = 0
for i in range(100):
    for j in range(100):
        if dragon[i][j] == 1 and dragon[i+1][j] == 1 and dragon[i][j+1] == 1 and dragon[i+1][j+1] == 1:
            ans += 1

print(ans)

