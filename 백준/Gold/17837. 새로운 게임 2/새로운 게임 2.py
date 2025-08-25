import sys
input = sys.stdin.readline
N,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
ch = [[[] for _ in range(N)] for _ in range(N)]
box = []
for idx in range(K):
    i,j,d = map(int,input().split())
    ch[i-1][j-1].append(idx)
    box.append((idx,i-1,j-1,d-1))
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def checking():
    for i in range(N):
        for j in range(N):
            if len(ch[i][j]) >= 4:
                return True
    return False

cnt = 1
while True:
    if cnt > 1000:
        print(-1)
        break
    for k in range(K):
        if checking():
            print(cnt)
            sys.exit()
        idx,i,j,d = box[k]
        x = i + dx[d]
        y = j + dy[d]
        if (x<0 or x>=N) or (y<0 or y>=N) or (arr[x][y] == 2):
            d = d + 1 if (d == 0 or d == 2) else d - 1
            x = i + dx[d]
            y = j + dy[d]
            box[k] = (idx,i,j,d)
            if (x<0 or x>=N) or (y<0 or y>=N) or (arr[x][y] == 2):
                continue
            else:
                cur = ch[i][j].index(idx)
                tmp = ch[i][j][cur:]
                ch[i][j] = ch[i][j][:cur]
                if arr[x][y] == 0:
                    ch[x][y] += tmp
                if arr[x][y] == 1:
                    ch[x][y] += tmp[::-1]
        else:
            cur = ch[i][j].index(idx)
            tmp = ch[i][j][cur:]
            ch[i][j] = ch[i][j][:cur]
            if arr[x][y] == 0:
                ch[x][y] += tmp
            if arr[x][y] == 1:
                ch[x][y] += tmp[::-1]

        # 동기화 시키기
        for num in tmp:
            idx,i,j,d = box[num]
            box[num] = (idx,x,y,d)

    if checking():
        print(cnt)
        sys.exit()
    cnt += 1
