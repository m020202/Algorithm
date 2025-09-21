import sys, copy
input = sys.stdin.readline
N = int(input())
population = [0]+list(map(int,input().split()))
ch = [[0]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    ch[i][i] = 1
    tmp = list(map(int,input().split()))
    for j in range(1,len(tmp)):
        ch[i][tmp[j]] = 1
        ch[tmp[j]][i] = 1

def warshall(arr):
    path = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(1,N+1):
        for j in range(1,N+1):
            if ch[i][j] == 1 and arr[i] == arr[j]:
                path[i][j] = 1

    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                if arr[i] == arr[j] and path[i][k] == 1 and path[k][j] == 1:
                    path[i][j] = 1
    return path

def checking(arr):
    path = warshall(arr)
    arr1 = [i for i in range(1,N+1) if arr[i] == 0]
    arr2 = [i for i in range(1,N+1) if arr[i] == 1]

    cnt1 = 0
    for i in range(len(arr1)):
        cnt1 += population[arr1[i]]
        for j in range(i+1,len(arr1)):
            if path[arr1[i]][arr1[j]] == 0:
                return -1

    cnt2 = 0
    for i in range(len(arr2)):
        cnt2 += population[arr2[i]]
        for j in range(i + 1, len(arr2)):
            if path[arr2[i]][arr2[j]] == 0:
                return -1

    return abs(cnt1-cnt2)

ans = -1
def func(cur,color):
    global ans
    if cur == N+1:
        if sum(color) != -1 and sum(color) != N:
            res = checking(color)
            if res >= 0:
                ans = res if ans == -1 else min(res,ans)
    else:
        color[cur] = 0
        func(cur+1,color)
        color[cur] = 1
        func(cur+1,color)

func(1,[-1]*(N+1))
print(ans)
