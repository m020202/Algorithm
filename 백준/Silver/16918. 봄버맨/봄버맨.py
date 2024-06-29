r,c,n = map(int,input().split())
box = [list(map(str,input())) for _ in range(r)]


ch = list([0] * c for _ in range(r))
for i in range(r):
    for j in range(c):
        if box[i][j] == 'O':
            ch[i][j] = 3

def transfering(t):
    for i in range(r):
        for j in range(c):
            if box[i][j] == '.':
                box[i][j] = 'O'
                ch[i][j] = t

def printing():
    for i in range(r):
        for j in range(c):
            print(box[i][j], end='')
        print()

def boom(cur):
    tmp = True
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    for i in range(r):
        for j in range(c):
            if ch[i][j] == cur:
                tmp = False
                box[i][j] = '.'
                ch[i][j] = 0
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]
                    if 0<=x<r and 0<=y<c:
                        if ch[x][y] != cur:
                            box[x][y] = '.'
                            ch[x][y] = 0
    return tmp

for i in range(2, n+1):
    if boom(i):
        transfering(i+3)
printing()
