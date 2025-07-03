import sys, heapq
input = sys.stdin.readline
v,e = map(int,input().split())
box = {}
for i in range(1,v+1):
    box[i] = []
for _ in range(e):
    a,b,c = map(int,input().split())
    box[a].append((b,c))
    box[b].append((a,c))

ch = [0] * (v+1)
ch[1] = 1
heap = []
# 1부터 시작.
for i,j in box[1]:
    heapq.heappush(heap,(j,i))

ans = 0
while heap:
    weight,cur = heapq.heappop(heap)
    if ch[cur] == 1:
        continue
    ch[cur] = 1
    ans += weight
    for i,j in box[cur]:
        heapq.heappush(heap,(j,i))

print(ans)