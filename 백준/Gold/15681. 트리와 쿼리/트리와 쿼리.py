import sys
sys.setrecursionlimit(120000)
n,r,q = map(int,input().split())
box = [[] for _ in range(n+1)]
visit = [-1] * (n+1)
for _ in range(n-1):
    u,v = map(int,input().split())
    box[u].append(v)
    box[v].append(u)

def dfs(cur):
    visit[cur] = 1
    for i in box[cur]:
        if visit[i] == -1:
            visit[cur] += dfs(i)
    return visit[cur]

dfs(r)
for _ in range(q):
    now = int(input())
    print(visit[now])