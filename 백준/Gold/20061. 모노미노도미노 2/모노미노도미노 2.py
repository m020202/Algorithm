import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
box = [[0]*10 for _ in range(10)]
ans = 0

def positioning(t,x,y):
    if t == 1:
        # 파란 영역으로 이동
        idx = 9
        for i in range(y+1,10):
            if box[x][i] == 1:
                idx = i-1
                break
        box[x][idx] = 1

        # 초록 영역으로 이동
        idx = 9
        for i in range(x+1,10):
            if box[i][y] == 1:
                idx = i-1
                break
        box[idx][y] = 1

    elif t == 2:
        # 파란 영역으로 이동
        idx = 9
        for i in range(y+2,10):
            if box[x][i] == 1:
                idx = i-1
                break
        box[x][idx] = 1
        box[x][idx-1] = 1

        # 초록 영역으로 이동
        idx1,idx2 = 9,9
        for i in range(x+1,10):
            if idx1 == 9 and box[i][y] == 1:
                idx1 = i-1
            if idx2 == 9 and box[i][y+1] == 1:
                idx2 = i-1
        num = min(idx1,idx2)
        box[num][y],box[num][y+1] = 1,1


    else:
        # 파란 영역으로 이동
        idx1,idx2 = 9,9
        for i in range(y+1,10):
            if idx1 == 9 and box[x][i] == 1:
                idx1 = i-1
            if idx2 == 9 and box[x+1][i] == 1:
                idx2 = i-1
        num = min(idx1, idx2)
        box[x][num],box[x+1][num] = 1,1

        # 초록 영역으로 이동
        idx = 9
        for i in range(x+2,10):
            if box[i][y] == 1:
                idx = i-1
                break
        box[idx][y] = 1
        box[idx-1][y] = 1

def condition1():
    global ans
    # 파란 영역 체크
    tmp = False
    while not tmp:
        tmp = True
        for i in range(6,10):
            if all(box[j][i] == 1 for j in range(4)):
                tmp = False
                ans += 1
                for k in range(i,3,-1):
                    for j in range(4):
                        box[j][k] = box[j][k-1]
                for j in range(4):
                    box[j][4] = 0

    # 초록 영역 체크
    tmp = False
    while not tmp:
        tmp = True
        for i in range(6,10):
            if all(box[i][j] == 1 for j in range(4)):
                tmp = False
                ans += 1
                for k in range(i,3,-1):
                    for j in range(4):
                        box[k][j] = box[k-1][j]
                for j in range(4):
                    box[4][j] = 0

def condition2():
    # 파란 영역 체크
    for _ in range(2):
        if any(box[i][5] == 1 for i in range(4)):
            for i in range(4):
                for j in range(9,3,-1):
                    box[i][j] = box[i][j-1]
            for i in range(4):
                box[i][4] = 0

    # 초록 영역 체크
    for _ in range(2):
        if any(box[5][i] == 1 for i in range(4)):
            for i in range(4):
                for j in range(9,3,-1):
                    box[j][i] = box[j-1][i]
            for i in range(4):
                box[4][i] = 0

def calc():
    tot = 0
    # 파란 영역 블록 개수
    for i in range(6,10):
        for j in range(4):
            if box[j][i] == 1:
                tot += 1

    # 초록 영역 블록 개수
    for i in range(6,10):
        for j in range(4):
            if box[i][j] == 1:
                tot += 1

    print(tot)

for t,x,y in arr:
    positioning(t,x,y)
    condition1()
    condition2()

print(ans)
calc()
