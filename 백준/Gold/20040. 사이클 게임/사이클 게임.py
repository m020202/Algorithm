# 같은 트리에 속하는 두 경로가 연결되면 이를 사이클로 생각하기 !
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
parent = list(range(n))

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

ans = 0
for i in range(m):
    a,b = map(int,input().split())
    if find(a) == find(b) and ans == 0:
        ans = i + 1
    else:
        union(a,b)

print(ans)