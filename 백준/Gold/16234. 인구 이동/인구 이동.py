from collections import deque
n,l,r = map(int,input().split())
box = []
for _ in range(n):
    box.append(list(map(int,input().split())))

dx = [1,0,-1,0]
dy = [0,1,0,-1]


def checking(x,y,ch):
    cur = box[x][y]
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<n and 0<=yy<n and ch[xx][yy] == 0:
            if l <= abs(cur-box[xx][yy]) <= r:
                return True
    return False

cnt = 0
while True:
    ch = [[0] * n for _ in range(n)]
    tmp = False
    for i in range(n):
        for j in range(n):
            if ch[i][j] == 0:
                if checking(i,j,ch) == False:
                    continue

                dQ = deque()
                dQ.append((i,j))
                ch_cnt = 0
                ch_sum = 0
                ky = []
                ky.append((i,j))
                ch[i][j] = 1
                while dQ:
                    x,y = dQ.popleft()
                    cur = box[x][y]
                    ch_cnt += 1
                    ch_sum += cur

                    for k in range(4):
                        xx = x + dx[k]
                        yy = y + dy[k]
                        if 0<=xx<n and 0<=yy<n and ch[xx][yy] == 0:
                            if l <= abs(cur-box[xx][yy]) <= r:
                                ch[xx][yy] = 1
                                dQ.append((xx,yy))
                                ky.append((xx,yy))
                                tmp = True
                
                for m,p in ky:
                    box[m][p] = ch_sum // len(ky)


    if tmp == False:
        break
    cnt += 1                

print(cnt)

