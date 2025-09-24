import sys,copy
input = sys.stdin.readline
N,M = map(int,input().split())
arr = [list(map(str,input().rstrip())) for _ in range(N)]
rx,ry = 0,0 # 빨간 구슬 위치
bx,by = 0,0 # 파란 구슬 위치
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            rx,ry = i,j
        if arr[i][j] == 'B':
            bx,by = i,j

def moving(d,r_x,r_y,b_x,b_y):
    new_rx,new_ry,new_bx,new_by = 0,0,0,0 # 새로운 구슬 위치
    if d == 0: # 왼쪽
        if r_y < b_y: # 빨간공이 더 왼쪽에 위치
            tmp = False
            for i in range(r_y-1,-1,-1):
                if arr[r_x][i] == '#':
                    new_rx = r_x
                    new_ry = i+1
                    break
                elif arr[r_x][i] == 'O':
                    tmp = True
                    break
            for i in range(b_y-1,-1,-1):
                if arr[b_x][i] == '#' or (b_x == new_rx and i == new_ry):
                    new_bx = b_x
                    new_by = i+1
                    break
                elif arr[b_x][i] == 'O':
                    return 1,()
            if tmp:
                return 0,()
        else:
            for i in range(b_y-1,-1,-1):
                if arr[b_x][i] == '#':
                    new_bx = b_x
                    new_by = i+1
                    break
                elif arr[b_x][i] == 'O':
                    return 1,()
            for i in range(r_y-1,-1,-1):
                if arr[r_x][i] == '#' or (r_x == new_bx and i == new_by):
                    new_rx = r_x
                    new_ry = i+1
                    break
                elif arr[r_x][i] == 'O':
                    return 0,()
    elif d == 1: # 오른쪽
        if r_y > b_y: # 빨간공이 더 오른쪽에 위치
            tmp = False
            for i in range(r_y+1,M):
                if arr[r_x][i] == '#':
                    new_rx = r_x
                    new_ry = i-1
                    break
                elif arr[r_x][i] == 'O':
                    tmp = True
                    break
            for i in range(b_y+1,M):
                if arr[b_x][i] == '#' or (b_x == new_rx and i == new_ry):
                    new_bx = b_x
                    new_by = i-1
                    break
                elif arr[b_x][i] == 'O':
                    return 1,()
            if tmp:
                return 0,()
        else:
            for i in range(b_y+1,M):
                if arr[b_x][i] == '#':
                    new_bx = b_x
                    new_by = i-1
                    break
                elif arr[b_x][i] == 'O':
                    return 1,()
            for i in range(r_y+1,M):
                if arr[r_x][i] == '#' or (r_x == new_bx and i == new_by):
                    new_rx = r_x
                    new_ry = i-1
                    break
                elif arr[r_x][i] == 'O':
                    return 0,()
    elif d == 2: # 위
        if r_x < b_x: # 빨간공이 더 위에 위치
            tmp = False
            for i in range(r_x-1,-1,-1):
                if arr[i][r_y] == '#':
                    new_rx = i+1
                    new_ry = r_y
                    break
                elif arr[i][r_y] == 'O':
                    tmp = True
                    break
            for i in range(b_x-1,-1,-1):
                if arr[i][b_y] == '#' or (i == new_rx and b_y == new_ry):
                    new_bx = i+1
                    new_by = b_y
                    break
                elif arr[i][b_y] == 'O':
                    return 1,()
            if tmp:
                return 0,()
        else:
            for i in range(b_x-1,-1,-1):
                if arr[i][b_y] == '#':
                    new_bx = i+1
                    new_by = b_y
                    break
                elif arr[i][b_y] == 'O':
                    return 1,()
            for i in range(r_x-1,-1,-1):
                if arr[i][r_y] == '#' or (i == new_bx and r_y == new_by):
                    new_rx = i+1
                    new_ry = r_y
                    break
                elif arr[i][r_y] == 'O':
                    return 0,()
    else: # 아래
        if r_x > b_x: # 빨간공이 더 아래에 위치
            tmp = False
            for i in range(r_x+1,N):
                if arr[i][r_y] == '#':
                    new_rx = i-1
                    new_ry = r_y
                    break
                elif arr[i][r_y] == 'O':
                    tmp = True
                    break
            for i in range(b_x+1,N):
                if arr[i][b_y] == '#' or (i == new_rx and b_y == new_ry):
                    new_bx = i-1
                    new_by = b_y
                    break
                elif arr[i][b_y] == 'O':
                    return 1,()
            if tmp:
                return 0,()
        else:
            for i in range(b_x+1,N):
                if arr[i][b_y] == '#':
                    new_bx = i-1
                    new_by = b_y
                    break
                elif arr[i][b_y] == 'O':
                    return 1,()
            for i in range(r_x+1,N):
                if arr[i][r_y] == '#' or (i == new_bx and r_y == new_by):
                    new_rx = i-1
                    new_ry = r_y
                    break
                elif arr[i][r_y] == 'O':
                    return 0,()
    return 2,(new_rx,new_ry,new_bx,new_by)

ans = -1
ch = {}
ch[(rx,ry,bx,by)] = True
def func(cnt,r_x,r_y,b_x,b_y):
    global ans
    if cnt > 10:
        return
    for i in range(4):
        res,tmp = moving(i,r_x,r_y,b_x,b_y)
        if res == 0:
            ans = min(ans,cnt) if ans != -1 else cnt
        elif res == 2:
            new_rx,new_ry,new_bx,new_by = tmp
            if (new_rx,new_ry,new_bx,new_by) not in ch:
                ch[(new_rx, new_ry, new_bx, new_by)] = True
                arr[r_x][r_y] = '.'
                arr[b_x][b_y] = '.'
                arr[new_rx][new_ry] = 'R'
                arr[new_bx][new_by] = 'B'
                func(cnt+1,new_rx,new_ry,new_bx,new_by)
                arr[new_rx][new_ry] = '.'
                arr[new_bx][new_by] = '.'
                arr[r_x][r_y] = 'R'
                arr[b_x][b_y] = 'B'
                ch.pop((new_rx, new_ry, new_bx, new_by))

func(1,rx,ry,bx,by)
print(ans)
