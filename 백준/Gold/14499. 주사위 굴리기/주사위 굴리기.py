from collections import deque
n,m,x,y,k = map(int,input().split())
box = []
for _ in range(n):
    box.append(list(map(int,input().split())))

api = list(map(int,input().split()))

dice = [[0] * 3 for _ in range(4)]

def switch(num):
    global dice
    if num == 0:
        tmp = dice[1][1]
        dice[1][1] = dice[1][2]
        dice[1][2] = dice[3][1]
        dice[3][1] = dice[1][0]
        dice[1][0] = tmp
    elif num == 1:
        tmp = dice[1][1]
        dice[1][1] = dice[1][0]
        dice[1][0] = dice[3][1]
        dice[3][1] = dice[1][2]
        dice[1][2] = tmp
    elif num == 2:
        tmp = dice[3][1]
        dice[3][1] = dice[2][1]
        dice[2][1] = dice[1][1]
        dice[1][1] = dice[0][1]
        dice[0][1] = tmp
    else:
        tmp = dice[0][1]
        dice[0][1] = dice[1][1]
        dice[1][1] = dice[2][1]
        dice[2][1] = dice[3][1]
        dice[3][1] = tmp

    return dice[1][1]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

dQ = deque()
for i in api:
    dQ.append(i)

cD = 0
cX = x
cY = y
while dQ:
    now = dQ.popleft() - 1
    if 0<=cX + dx[now]<n and 0<=cY + dy[now]<m:
        cX += dx[now]
        cY += dy[now]

        cur = switch(now)
        print(dice[3][1])
        if box[cX][cY] == 0:
            box[cX][cY] = cur
        else:
            dice[1][1] = box[cX][cY]
            box[cX][cY] = 0