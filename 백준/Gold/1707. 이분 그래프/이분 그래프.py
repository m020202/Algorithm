import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

def bfs(box):
    color = [0] * (v+1)
    dq = deque()
    for i in box:
        if color[i] == 0:
            color[i] = 1
            for j in box[i]:
                dq.append((j,2))

        while dq:
            cur,team = dq.popleft()
            if color[cur] == 3-team:
                return "NO"
            elif color[cur] == 0:
                color[cur] = team
                for k in box[cur]:
                    dq.append((k,3-team))
    return "YES"

for _ in range(n):
    v,e = map(int,input().split())
    box = {}
    for i in range(1,v+1):
        box[i] = []
    for _ in range(e):
        x,y = map(int,input().split())
        box[x].append(y)
        box[y].append(x)
    print(bfs(box))
