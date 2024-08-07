import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
tree = [[] for _ in range(n+1)]
dist = [-1] * (n+1)
dist[1] = 0

for _ in range(n-1):
    a,b,c = map(int,input().split())
    tree[a].append((b,c))
    tree[b].append((a,c))

def DFS(s,w):
    for a,b in tree[s]:
        if dist[a] == -1:
            dist[a] = w + b
            DFS(a, w + b)
    
DFS(1,0)
mx = dist.index(max(dist))
dist = [-1] * (n+1)
dist[mx] = 0
DFS(mx,0)
print(max(dist))