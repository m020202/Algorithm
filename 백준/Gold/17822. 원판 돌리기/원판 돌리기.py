import sys
from collections import deque
input = sys.stdin.readline
N,M,T = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(N)]
xdk = [list(map(int,input().split())) for _ in range(T)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def shifting(arr,dir,k): # 시계 또는 반시계 회전
    if dir: # 반시계
        for _ in range(k):
            tmp = arr[0]
            for i in range(1,M):
                arr[i-1] = arr[i]
            arr[-1] = tmp
    else: # 시계
        for _ in range(k):
            tmp = arr[-1]
            for i in range(M-1,-1,-1):
                arr[i] = arr[i-1]
            arr[0] = tmp

    return arr

def removing(): # 인접한 수 제거
    ch = [[0]*M for _ in range(N)]
    res = False
    for i in range(N):
        for j in range(M):
            if ch[i][j] == 0 and box[i][j] != 0:
                cur = box[i][j]
                dq = deque([(i,j)])
                ch[i][j] = 1
                tmp = False
                while dq:
                    x,y = dq.popleft()
                    for k in range(4):
                        if k <= 1:
                            xx = x + dx[k]
                            yy = y + dy[k]
                        else:
                            xx = (x + dx[k] + N) % N
                            yy = (y + dy[k] + M) % M
                        if 0<=xx<N and 0<=yy<M and box[xx][yy] != 0:
                            if ch[xx][yy] == 0 and box[xx][yy] == cur:
                                tmp = True
                                ch[xx][yy] = 1
                                dq.append((xx,yy))
                if not tmp:
                    ch[i][j] = 0

    for i in range(N):
        for j in range(M):
            if ch[i][j] == 1:
                res = True
                box[i][j] = 0
    return res

def updating(): # 평균 기반 값 업데이트
    # 평균 구하기
    tot = 0
    cnt = 0
    for i in range(N):
        for j in range(M):
            if box[i][j] != 0:
                tot += box[i][j]
                cnt += 1
    if cnt == 0:
        return 
    avg = tot / cnt

    # 값 업데이트
    for i in range(N):
        for j in range(M):
            if box[i][j] != 0:
                if box[i][j] > avg:
                    box[i][j] -= 1
                elif box[i][j] < avg:
                    box[i][j] += 1


for x,d,k in xdk:
    for i in range(x,N+1,x): # x의 배수 shifting
        box[i-1] = shifting(box[i-1],d,k)
    result = removing() # 인접한 수 탐색
    if result:
        continue
    else:
        updating()

ans = 0
for i in box:
    ans += sum(i)
print(ans)