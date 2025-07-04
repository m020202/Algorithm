import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize
n,m = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(n)]

home = []
chicken = []
for i in range(n):
    for j in range(n):
        if box[i][j] == 1:
            home.append((i,j))
        if box[i][j] == 2:
            chicken.append((i,j))

dx = [1,0,-1,0]
dy = [0,1,0,-1]
ans = INF

# 거리 계산 함수
def calc(chosen):
    global ans
    tot = 0
    for i,j in home:
        cur = INF
        for x,y in chosen:
            cur = min(cur, abs(x-i) + abs(y-j))
        tot += cur
    ans = min(ans,tot)

# 치킨집 선택 함수
def choose(chosen, num, idx):
    if num == m:
        calc(chosen)
        return

    for i in range(idx+1, len(chicken)):
        choose(chosen + [chicken[i]], num+1, i)

choose([],0,-1)
print(ans)


