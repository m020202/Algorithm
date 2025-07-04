import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

n,e = map(int,input().split())
edge = {}
for i in range(1,n+1):
    edge[i] = []
for _ in range(e):
    a,b,c = map(int,input().split())
    edge[a].append((b,c))
    edge[b].append((a,c))

v1,v2 = map(int,input().split())

def dijkstra(start, end):
    heap = []
    ch = [INF] * (n+1)
    ch[start] = 0
    heapq.heappush(heap, (0,start))
    while heap:
        weight,vertex = heapq.heappop(heap)
        if ch[vertex] < weight:
            continue

        for v,w in edge[vertex]:
            if ch[v] > ch[vertex] + w:
                ch[v] = ch[vertex] + w
                heapq.heappush(heap,(ch[v],v))

    return ch[end]

# 1->v1, v1->v2, v2->n
ans = dijkstra(1,v1) + dijkstra(v1,v2) + dijkstra(v2,n)

# # 1->v2, v2->v1, v1->n
ans = min(ans, dijkstra(1,v2) + dijkstra(v2,v1) + dijkstra(v1,n))

if ans >= INF:
    print(-1)
else:
    print(ans)
