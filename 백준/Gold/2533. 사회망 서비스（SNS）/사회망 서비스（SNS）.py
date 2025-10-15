import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(1000001)
N = int(input())
dic = {i:[] for i in range(1,N+1)}
for _ in range(N-1):
    u,v = map(int,input().split())
    dic[u].append(v)
    dic[v].append(u)

ans = 0
def dfs(prev,cur):
    global ans
    res = 0
    for i in dic[cur]:
        if i == prev:
            continue
        res += dfs(cur,i)
    if res:
        ans += 1
        return 0
    else:
        return 1

dfs(0,1)
print(ans)