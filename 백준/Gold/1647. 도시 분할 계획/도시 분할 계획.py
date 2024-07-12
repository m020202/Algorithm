import heapq
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

ch = [0] * (n+1)
ans = 0
mx = 0
heap = []

# 첫 Tree vertex 선정 후 fringe 추가
ch[1] = 1
for i in graph[1]:
        heapq.heappush(heap, (i[1], i[0]))

while len(heap) > 0:
    w,cur = heapq.heappop(heap)
    if ch[cur] == 1:
        continue
    ch[cur] = 1
    ans += w
    mx = max(mx,w)
    
    # fringe 추가
    for i in graph[cur]:
        heapq.heappush(heap, (i[1], i[0]))


print(ans - mx)