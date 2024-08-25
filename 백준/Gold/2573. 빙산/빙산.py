from collections import deque
n,m = map(int,input().split())

box = []

for _ in range(n):
    spot = list(map(int,input().split()))
    box.append(spot)

def checking():
    cnt = 0
    ch = [[0]*m for _ in range(n)]
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    for i in range(n):
        for j in range(m):
            if box[i][j] != 0 and ch[i][j] == 0:
                dQ = []
                dQ = deque(dQ)
                dQ.append((i,j))
                ch[i][j] = 1
                cnt+= 1

                while(dQ):
                    x,y = dQ.popleft()
                    
                    for k in range(4):
                        xx = x + dx[k]
                        yy = y + dy[k]
                        if 0<=xx<n and 0<=yy<m:
                            if box[xx][yy] != 0 and ch[xx][yy] == 0:
                                ch[xx][yy] = 1
                                dQ.append((xx,yy))
    return cnt

dx = [1,0,-1,0]
dy = [0,1,0,-1]


tot = 0
while True:
    tmp = True

    bh = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if box[i][j] > 0:
                tmp = False
                cnt = 0
                for k in range(4):
                    ii = i + dx[k]
                    jj = j + dy[k]
                    if 0<=ii<n and 0<=jj<m and box[ii][jj] == 0 and bh[ii][jj] == 0:
                        cnt += 1
                if box[i][j]-cnt <= 0:
                    box[i][j] = 0
                    bh[i][j] = 1
                else:
                    box[i][j] -= cnt
    
    tot += 1

    if tmp == True:
        print(0)
        break
    
    if checking() >= 2:
        print(tot)
        break