def checking(x,y,mx):
    for i in range(x,x+mx):
        for j in range(y,y+mx):
            if not (i<10 and j<10 and box[i][j] == 1):
                return False
    return True

def attach(x,y,k,w):
    for i in range(x,x+k):
        for j in range(y,y+k):
            box[i][j] = w

def glue(num):
    global ans
    for i in range(10):
        for j in range(10):
            if box[i][j] == 1:
                for k in range(1,6):
                    if confetti[k] and checking(i,j,k):
                        attach(i,j,k,0)
                        confetti[k] -= 1
                        glue(num+1)
                        attach(i,j,k,1)
                        confetti[k] += 1
                return
    ans = min(ans,num)


import sys, copy
input = sys.stdin.readline
box = [list(map(int,input().split())) for _ in range(10)]
confetti = [5] * 6
ans = 26
glue(0)
if ans == 26:
    print(-1)
else:
    print(ans)

