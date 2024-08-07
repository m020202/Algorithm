import sys
input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n):
    cur = list(map(int,input().split()))
    v = cur[0]
    for i in range(1,len(cur),2):
        if cur[i] == -1:
            break
        tree[v].append((cur[i],cur[i+1]))

dist = [-1] * (n+1)
dist[1] = 0
def DFS(s,w):
    global dist
    for i,j in tree[s]:
        if dist[i] == -1:
            dist[i] = w + j
            DFS(i,w+j)
DFS(1,0)
mxIdx = dist.index(max(dist))
dist = [-1] * (n+1)
dist[mxIdx] = 0
DFS(mxIdx,0)

print(max(dist))