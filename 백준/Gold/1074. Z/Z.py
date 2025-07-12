import sys
input = sys.stdin.readline
n,r,c = map(int,input().split())
num = 2**n
k = 2**(n-1)
size = k*k # 면적 크기

def func(dep,x,y,cnt):
    if dep==1:
        dx = [0, 0, 1, 1]
        dy = [0, 1, 0, 1]
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if xx == r and yy == c:
                print(cnt + i)
                return
    else:
        off_x = (r-x)//dep
        new_x = (off_x*dep) + x
        off_y = (c-y)//dep
        new_y = (off_y*dep) + y
        new_cnt = (off_x*2 + off_y) * (dep**2) + cnt
        return func(dep//2,new_x,new_y,new_cnt)

func(k, 0, 0, 0)

