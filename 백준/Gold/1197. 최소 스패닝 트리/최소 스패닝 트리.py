import heapq
v,e = map(int,input().split())
g = [[] for _ in range(v+1)]
for _ in range(e):
    a,b,c = map(int,input().split())
    g[a].append((b,c))
    g[b].append((a,c))

ch = [0] * (v+1)
ans = 0
heap = []

# v 하나 Tree vertex로 올리기
cur = 1
ch[1] = 1
# fringe 추가
for i in g[1]:
    heapq.heappush(heap,(i[1],i[0]))

while len(heap) > 0:
    weight, cur = heapq.heappop(heap)
    if ch[cur] == 1:
        continue
    ch[cur] = 1
    ans += weight
    # 선정된 Tree vertex의 fringe 추가
    for i in g[cur]:
        heapq.heappush(heap,(i[1],i[0]))

print(ans)