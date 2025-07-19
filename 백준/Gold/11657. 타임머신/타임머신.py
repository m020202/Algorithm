import sys
input = sys.stdin.readline
INF = sys.maxsize
n,m = map(int,input().split())
edges = {i : [] for i in range(1, n+1)}
for _ in range(m):
    a,b,c = map(int,input().split())
    edges[a].append((b,c))
distance = [INF] * (n+1)

distance[1] = 0
result = True
for i in range(n-1):
    for cur in edges:
        for next,w in edges[cur]:
            if distance[cur] != INF and distance[next] > distance[cur] + w:
                distance[next] = distance[cur] + w
for cur in edges:
    for next, w in edges[cur]:
        if distance[cur] != INF and distance[next] > distance[cur] + w:
            result = False

if result:
    print(*(distance[i] if distance[i] != INF else -1 for i in range(2,n+1)),sep='\n')
else:
    print(-1)
