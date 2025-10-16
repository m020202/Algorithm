import sys,heapq
input = sys.stdin.readline
R,C,M = map(int,input().split())
arr = {}
for _ in range(M):
    r,c,s,d,z = map(int,input().split())
    arr[(r-1,c-1)] = (z,d,s)

ans = 0
def kill(idx):
    global ans
    for i in range(R):
        if (i,idx) in arr:
            ans += arr[(i,idx)][0]
            arr.pop((i,idx))
            return

def moving(i,j,s,d):
    if d == 1 or d == 2: # 위아래
        while s:
            if d == 1:
                if i-s < 0:
                    s -= i
                    d = 2
                    i = 0
                else:
                    i -= s
                    s = 0
            else:
                if i+s >= R:
                    s -= (R-i-1)
                    d = 1
                    i = R-1
                else:
                    i += s
                    s = 0

    elif d == 3 or d == 4: # 좌우
        while s:
            if d == 3:
                if j+s >= C:
                    s -= (C-j-1)
                    d = 4
                    j = C-1
                else:
                    j += s
                    s = 0
            else:
                if j-s < 0:
                    s -= j
                    d = 3
                    j = 0
                else:
                    j -= s
                    s = 0

    return (i,j,d)


def move():
    new_arr = {}
    for k in arr:
        i,j = k
        z,d,s = arr[k]
        ii,jj,dd = moving(i,j,s,d)
        if (ii,jj) not in new_arr or ((ii,jj) in new_arr and new_arr[(ii,jj)][0] < z):
            new_arr[(ii,jj)] = (z,dd,s)
    return new_arr

cur = 0
while cur < C:
    # 땅에 제일 가까운 상어 죽이기
    kill(cur)
    # 상어 이동
    arr = move()
    # 상어맨 한 칸 이동
    cur += 1

print(ans)