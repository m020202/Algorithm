import sys
input = sys.stdin.readline
INF = sys.maxsize

n,m = map(int,input().split())
src = int(input())
src -= 1

box = {}
for i in range(n):
    box[i] = {}

# 0: no, 1: fringe, 2: tree
status = [0] * n

value = [-1] * n

for _ in range(m):
    u,v,w = map(int,input().split())
    u -= 1
    v -= 1
    if v in box[u]:
        box[u][v] = min(box[u][v],  w)
    else:
        box[u][v] = w

status[src] = 2
value[src] = 0

# src와 인접한 V들 fringe로 바꾸기
for i in box[src]:
    status[i] = 1
    value[i] = box[src][i]

while True:
    tmp = False
    mn = INF
    idx = -1
    for i in range(n):
        if status[i] == 1:
            if value[i] < mn:
                mn = value[i]
                idx = i
                tmp = True
    if tmp == False:
        break

    cur = mn
    status[idx] = 2
    for i in box[idx]:
        if status[i] == 1:
            value[i] = min(value[i], cur + box[idx][i])
        elif status[i] == 0:
            status[i] = 1
            value[i] = cur + box[idx][i]

for i in value:
    if i == -1:
        print("INF")
    else:
        print(i)