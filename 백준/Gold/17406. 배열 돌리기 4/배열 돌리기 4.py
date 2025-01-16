import sys, copy
input = sys.stdin.readline
n,m,k = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(n)]
op = []
for _ in range(k):
    r,c,s = map(int,input().split())
    op.append((r-1,c-1,s))

def rotate(r,c,s,box):
    while (s > 0):
        x,y = r-s, c-s
        xx,yy = r+s, c+s

        # 첫번째
        tmp1 = box[x][yy]
        for i in range(yy,y,-1):
            box[x][i] = box[x][i-1]

        # 두번째
        tmp2 = box[xx][yy]
        for i in range(xx, x+1, -1):
            box[i][yy] = box[i-1][yy]
        box[x+1][yy] = tmp1

        # 세번째
        tmp3 = box[xx][y]
        for i in range(y, yy-1):
            box[xx][i] = box[xx][i+1]
        box[xx][yy-1] = tmp2

        # 네번째
        for i in range(x,xx-1):
            box[i][y] = box[i+1][y]
        box[xx-1][y] = tmp3
        s -= 1
    return box

ans = 10000000
def func(cnt,ch,idx,box):
    global ans
    if cnt == k:
        tot = 1000000
        for i in box:
            tot = min(tot,sum(i))
        ans = min(ans,tot)
        return

    for i in range(k):
        if ch[i] == 0:
            ch[i] = 1
            tmp = rotate(op[i][0],op[i][1], op[i][2], copy.deepcopy(box))
            func(cnt+1,ch,i,tmp)
            ch[i] = 0

ch = [0] * k
for i in range(k):
    ch[i] = 1
    tmp = rotate(op[i][0], op[i][1],op[i][2], copy.deepcopy(box))
    func(1,ch,i,tmp)
    ch[i] = 0

print(ans)





