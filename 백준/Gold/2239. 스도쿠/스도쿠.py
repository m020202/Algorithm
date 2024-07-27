import sys
box = [list(map(int,input())) for _ in range(9)]
zero = []

for i in range(9):
    for j in range(9):
        if box[i][j] == 0:
            zero.append((i,j))

def show():
    for i in range(9):
        for j in range(9):
            print(box[i][j], end='')
        print()

def widthCheck(x,num):
    for i in range(9):
        if box[x][i] == num:
            return False
    return True

def heightCheck(y,num):
    for i in range(9):
        if box[i][y] == num:
            return False
    return True

def boxCheck(x,y,num):
    ir = x % 3
    jr = y % 3

    if ir == 0 and jr == 0:
        # 1층
        if box[x][y+1] == num or box[x][y+2] == num:
            return False
        # 2층
        if box[x+1][y] == num or box[x+1][y+1] == num or box[x+1][y+2] == num:
            return False
        # 3층
        if box[x+2][y] == num or box[x+2][y+1] == num or box[x+2][y+2] == num:
            return False
    elif ir == 1 and jr == 0:
        # 1층
        if box[x-1][y] == num or box[x-1][y+1] == num or box[x-1][y+2] == num:
            return False
        # 2층
        if box[x][y+1] == num or box[x][y+2] == num:
            return False
        # 3층
        if box[x+1][y] == num or box[x+1][y+1] == num or box[x+1][y+2] == num:
            return False
    elif ir == 2 and jr == 0:
        # 1층
        if box[x-2][y] == num or box[x-2][y+1] == num or box[x-2][y+2] == num:
            return False
        # 2층
        if box[x-1][y] == num or box[x-1][y+1] == num or box[x-1][y+2] == num:
            return False
        # 3층
        if box[x][y+1] == num or box[x][y+2] == num:
            return False
    elif ir == 0 and jr == 1:
        # 1층
        if box[x][y-1] == num or box[x][y+1] == num:
            return False
        # 2층
        if box[x+1][y-1] == num or box[x+1][y] == num or box[x+1][y+1] == num:
            return False
        # 3층
        if box[x+2][y-1] == num or box[x+2][y] == num or box[x+2][y+1] == num:
            return False
    elif ir == 1 and jr == 1:
        # 1층
        if box[x-1][y-1] == num or box[x-1][y] == num or box[x-1][y+1] == num:
            return False
        # 2층
        if box[x][y-1] == num or box[x][y+1] == num:
            return False
        # 3층
        if box[x+1][y-1] == num or box[x+1][y] == num or box[x+1][y+1] == num:
            return False
    elif ir == 2 and jr == 1:
        # 1층
        if box[x-2][y-1] == num or box[x-2][y] == num or box[x-2][y+1] == num:
            return False
        # 2층
        if box[x-1][y-1] == num or box[x-1][y] == num or box[x-1][y+1] == num:
            return False
        # 3층
        if box[x][y-1] == num or box[x][y+1] == num:
            return False
    elif ir == 0 and jr == 2:
        # 1층
        if box[x][y-2] == num or box[x][y-1] == num:
            return False
        # 2층
        if box[x+1][y-2] == num or box[x+1][y-1] == num or box[x+1][y] == num:
            return False
        # 3층
        if box[x+2][y-2] == num or box[x+2][y-1] == num or box[x+2][y] == num:
            return False
    elif ir == 1 and jr == 2:
        # 1층
        if box[x-1][y-2] == num or box[x-1][y-1] == num or box[x-1][y] == num:
            return False
        # 2층
        if box[x][y-2] == num or box[x][y-1] == num:
            return False
        # 3층
        if box[x+1][y-2] == num or box[x+1][y-1] == num or box[x+1][y] == num:
            return False
    elif ir == 2 and jr == 2:
        # 1층
        if box[x-2][y-2] == num or box[x-2][y-1] == num or box[x-2][y] == num:
            return False
        # 2층
        if box[x-1][y-2] == num or box[x-1][y-1] == num or box[x-1][y] == num:
            return False
        # 3층
        if box[x][y-2] == num or box[x][y-1] == num:
            return False
    return True

def func(cur, tot):
    global box
    if cur == tot:
        show()
        sys.exit()

    x,y = zero[cur]
    
    for i in range(1,10):
        if widthCheck(x,i) and heightCheck(y,i) and boxCheck(x,y,i):
            box[x][y] = i
            func(cur+1, tot)
            box[x][y] = 0


func(0,len(zero))

