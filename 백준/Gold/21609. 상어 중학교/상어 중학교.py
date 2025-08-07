import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

# 블록 영역 찾기
def searching():
    res = []
    compare = (2,-1,-1,-1)
    ch = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0 and ch[i][j] == 0:
                ch[i][j] = 1
                cur = arr[i][j]
                tmp = []
                dq = deque([(i,j)])
                tot = 0
                rainbow_cnt = 0
                ch_rainbow = [[0]*N for _ in range(N)]
                if arr[i][j] == 0:
                    idx = idy = N+1
                    ch_rainbow[i][j] = 1
                else:
                    idx,idy = i,j
                while dq:
                    x,y = dq.popleft()
                    if arr[x][y] == 0:
                        rainbow_cnt += 1
                    else:
                        if (x, y) < (idx, idy):
                            idx, idy = x, y
                    tmp.append((x, y))
                    tot += 1
                    for k in range(4):
                        xx = x + dx[k]
                        yy = y + dy[k]
                        if 0<=xx<N and 0<=yy<N:
                            if arr[xx][yy] == 0 and ch_rainbow[xx][yy] == 0:
                                ch_rainbow[xx][yy] = 1
                                dq.append((xx,yy))
                            elif arr[xx][yy] == cur and ch[xx][yy] == 0:
                                ch[xx][yy] = 1
                                dq.append((xx,yy))

                if (tot, rainbow_cnt,idx,idy) > compare:
                    compare = (tot, rainbow_cnt,idx,idy)
                    res = tmp
    return (res,compare[0])

def removing(a):
    while a:
        i,j = a.pop()
        arr[i][j] = -2 # -2: 빈칸으로 취급


def shifting():
    for i in range(N-1,-1,-1):
        for j in range(N):
            if arr[i][j] < 0:
                continue
            for k in range(i+1,N):
                if arr[k][j] == -2:
                    arr[k-1][j],arr[k][j] = arr[k][j],arr[k-1][j]
                else:
                    break

def rotating():
    global arr
    new_box = []
    for j in range(N-1,-1,-1):
        tmp = []
        for i in range(N):
            tmp.append(arr[i][j])
        new_box.append(tmp)
    arr = new_box

ans = 0
while True:
    a,b = searching()
    if not a:
        break
    ans += (b * b)
    removing(a)
    shifting()
    rotating()
    shifting()

print(ans)