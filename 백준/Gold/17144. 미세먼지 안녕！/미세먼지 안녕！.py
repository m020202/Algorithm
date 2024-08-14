import sys
input = sys.stdin.readline
r,c,t = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(r)]
air = []
# 공기 청정기 위치 탐색
for i in range(r):
    if box[i][0] == -1:
        air.append(i)

# 인접한 네 방향으로 미세먼지 확산시키기
def spread(x,y,num):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    cur = num // 5
    cnt = 0
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<r and 0<=yy<c:
            if box[xx][yy] != -1:
                cnt += 1
                ch[xx][yy] += cur
    return cnt

while t:
    # 미세먼지 확산
    ch = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if box[i][j] > 0:
                cnt = spread(i,j,box[i][j])
                ch[i][j] -= (box[i][j]//5*cnt)
    
    for i in range(r):
        for j in range(c):
            box[i][j] += ch[i][j]
    
    # 미세먼지 순환
    # 위쪽 버전
    # 가장 윗 칸
    tmp = box[0][0]
    for i in range(1,c):
        box[0][i-1] = box[0][i]
    
    # 왼 칸 -> 위 쪽 공기청정기 위치 기준 : (air[0],0)
    for i in range(air[0]-1,1,-1):
        box[i][0] = box[i-1][0]
    box[1][0] = tmp

    # 아랫 칸
    a = air[0]
    tmp = box[a][-1]
    for i in range(c-1,0,-1):
        box[a][i] = box[a][i-1]
    box[a][1] = 0

    # 오른쪽 칸
    for i in range(a-1):
        box[i][-1] = box[i+1][-1]
    box[a-1][-1] = tmp
    
    # 아래쪽 버전
    # 위쪽 칸
    a = air[1]
    tmp = box[a][-1]
    for i in range(c-1,1,-1):
        box[a][i] = box[a][i-1]
    box[a][1] = 0

    # 오른 칸
    tmp2 = box[-1][-1]
    for i in range(r-1,a+1,-1):
        box[i][-1] = box[i-1][-1]
    box[a+1][-1] = tmp

    # 가장 아랫 칸
    tmp = box[-1][0]
    for i in range(c-2):
        box[-1][i] = box[-1][i+1]
    box[-1][c-2] = tmp2
    
    # 왼쪽 칸
    for i in range(a+1,r-2):
        box[i][0] = box[i+1][0]
    box[r-2][0] = tmp
    
    t -= 1

tot = 0
for i in range(r):
    for j in range(c):
        if box[i][j] > 0:
            tot += box[i][j]

print(tot)