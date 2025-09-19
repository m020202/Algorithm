import sys, copy
input = sys.stdin.readline
N = int(input())
box = [list(map(int,input().split())) for _ in range(N)]

def up(arr):
    ch = [[0]*N for _ in range(N)]
    # 다 한쪽으로 땡겨놓기
    for i in range(N):
        for j in range(1,N):
            if arr[j][i] != 0:
                for k in range(j,0,-1):
                    if arr[k-1][i] == 0:
                        arr[k][i],arr[k-1][i] = arr[k-1][i],arr[k][i]
                        ch[k][i],ch[k-1][i] = ch[k-1][i],ch[k][i]
                    else:
                        break

    for i in range(N):
        for j in range(N-1):
            if arr[j][i] != 0 and arr[j][i] == arr[j+1][i] and ch[j][i] == 0 and ch[j+1][i] == 0:
                arr[j][i] = arr[j][i] * 2
                arr[j+1][i] = 0
                ch[j][i] = 1

    for i in range(N):
        for j in range(1,N):
            if arr[j][i] != 0:
                for k in range(j,0,-1):
                    if arr[k-1][i] == 0:
                        arr[k][i],arr[k-1][i] = arr[k-1][i],arr[k][i]
                        ch[k][i],ch[k-1][i] = ch[k-1][i],ch[k][i]
                    else:
                        break
    return arr

def down(arr):
    ch = [[0]*N for _ in range(N)]
    # 다 한쪽으로 땡겨놓기
    for i in range(N):
        for j in range(N-2,-1,-1):
            if arr[j][i] != 0:
                for k in range(j,N-1):
                    if arr[k+1][i] == 0:
                        arr[k][i],arr[k+1][i] = arr[k+1][i],arr[k][i]
                        ch[k][i],ch[k+1][i] = ch[k+1][i],ch[k][i]
                    else:
                        break

    for i in range(N):
        for j in range(N-1,0,-1):
            if arr[j][i] != 0 and arr[j][i] == arr[j-1][i] and ch[j][i] == 0 and ch[j-1][i] == 0:
                arr[j][i] = arr[j][i] * 2
                arr[j-1][i] = 0
                ch[j][i] = 1

    for i in range(N):
        for j in range(N-2,-1,-1):
            if arr[j][i] != 0:
                for k in range(j,N-1):
                    if arr[k+1][i] == 0:
                        arr[k][i],arr[k+1][i] = arr[k+1][i],arr[k][i]
                        ch[k][i],ch[k+1][i] = ch[k+1][i],ch[k][i]
                    else:
                        break

    return arr

def left(arr):
    ch = [[0] * N for _ in range(N)]

    # 다 한쪽으로 땡겨놓기
    for i in range(N):
        for j in range(1,N):
            if arr[i][j] != 0:
                for k in range(j,0,-1):
                    if arr[i][k-1] == 0:
                        arr[i][k],arr[i][k-1] = arr[i][k-1],arr[i][k]
                        ch[i][k],ch[i][k-1] = ch[i][k-1],ch[i][k]
                    else:
                        break


    for i in range(N):
        for j in range(N-1):
            if arr[i][j] != 0 and arr[i][j] == arr[i][j+1] and ch[i][j] == 0 and ch[i][j+1] == 0:
                arr[i][j] = arr[i][j] * 2
                arr[i][j+1] = 0
                ch[i][j] = 1

    for i in range(N):
        for j in range(1,N):
            if arr[i][j] != 0:
                for k in range(j,-1,-1):
                    if arr[i][k-1] == 0:
                        arr[i][k],arr[i][k-1] = arr[i][k-1],arr[i][k]
                        ch[i][k],ch[i][k-1] = ch[i][k-1],ch[i][k]
                    else:
                        break

    return arr

def right(arr):
    ch = [[0] * N for _ in range(N)]

    # 다 한쪽으로 땡겨놓기
    for i in range(N):
        for j in range(N-2,-1,-1):
            if arr[i][j] != 0:
                for k in range(j,N-1):
                    if arr[i][k+1] == 0:
                        arr[i][k],arr[i][k+1] = arr[i][k+1],arr[i][k]
                        ch[i][k],ch[i][k+1] = ch[i][k+1],ch[i][k]
                    else:
                        break

    for i in range(N):
        for j in range(N-1,0,-1):
            if arr[i][j] != 0 and arr[i][j] == arr[i][j-1] and ch[i][j] == 0 and ch[i][j-1] == 0:
                arr[i][j] = arr[i][j] * 2
                arr[i][j-1] = 0
                ch[i][j] = 1

    for i in range(N):
        for j in range(N-2,-1,-1):
            if arr[i][j] != 0:
                for k in range(j,N-1):
                    if arr[i][k+1] == 0:
                        arr[i][k],arr[i][k+1] = arr[i][k+1],arr[i][k]
                        ch[i][k],ch[i][k+1] = ch[i][k+1],ch[i][k]
                    else:
                        break

    return arr

def find_max(arr):
    res = 0
    for i in arr:
        res = max(res,max(i))
    return res

ans = 0
def func(cnt,cur):
    global ans
    ans = max(ans,find_max(cur))
    if cnt == 5:
        return
    else:
        tmp = copy.deepcopy(cur)
        func(cnt+1,up(tmp))
        tmp = copy.deepcopy(cur)
        func(cnt+1,down(tmp))
        tmp = copy.deepcopy(cur)
        func(cnt+1,left(tmp))
        tmp = copy.deepcopy(cur)
        func(cnt+1,right(tmp))

func(0,box)
print(ans)