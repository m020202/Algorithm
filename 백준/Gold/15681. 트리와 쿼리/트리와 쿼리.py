from collections import deque
import sys
sys.setrecursionlimit(120000)
n,r,q = map(int,input().split())
box = [[] for _ in range(n+1)]
tree = [[] for _ in range(n+1)]
dQ = deque()
for _ in range(n-1):
    u,v = map(int,input().split())
    box[u].append(v)
    box[v].append(u)

ch = [-1] * (n+1)
ch[r] = 0
dQ.append(r)
while dQ:
    cur = dQ.popleft()
    for i in box[cur]:
        if ch[i] == -1:
            tree[cur].append(i)
            ch[i] = 0
            dQ.append(i)

sub = [-1] * (n+1)
def find(cur):
    if sub[cur] != -1:
        return sub[cur]
    ans = 1
    for i in tree[cur]:
        ans += find(i)
    sub[cur] = ans
    return ans
find(r)

for _ in range(q):
    cur = int(input())
    print(sub[cur])