import sys
input = sys.stdin.readline
INF = sys.maxsize
n = int(input())
m = int(input())
box = [[-1] * n for _ in range(n)]
for _ in range(m):
    s,d,w = map(int,input().split())
    s -= 1
    d-= 1
    if box[s][d] == -1:
        box[s][d] = w
    else:
        box[s][d] = min(box[s][d],w)
s,dst = map(int,input().split())
s-=1
dst-=1

# 0: Unseen, 1: Fringe, 2: Tree
status = [0] * n
status[s] = 2

parent = [-1] * n
d = [INF] * n
d[s] = 0

# s의 인접한 V들 fringe로 바꿔주기
for i in range(n):
    if box[s][i] != -1:
        status[i] = 1
        d[i] = box[s][i]
        parent[i] = s

def minFringe():
    min = INF
    idx = -1
    for i in range(n):
        if status[i] == 1:
            if d[i] < min:
                min = d[i]
                idx = i
    return idx

def change(num, w):
    for i in range(n):
        if box[num][i] != -1:
            curWeight = box[num][i] + w
            if status[i] == 0:
                status[i] = 1
                parent[i] = num
                d[i] = curWeight
            elif status[i] == 1:
                if d[i] >= curWeight:
                    parent[i] = num
                    d[i] = curWeight

while True:
    # Fringe가 하나도 없으면 종료
    tmp = True
    for i in status:
        if i == 1:
            tmp = False
    if tmp == True:
        break
    
    idx = minFringe()
    status[idx] = 2
    change(idx, d[idx])

print(d[dst])


    