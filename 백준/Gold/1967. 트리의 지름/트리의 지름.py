import sys
input = sys.stdin.readline
sys.setrecursionlimit(65536)
n = int(input())
child = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    child[a].append((b,c))
    
ans = 0
def DFS(root):
    global ans
    if len(child[root]) == 0:
        return 0
    tot = []
    for a,b in child[root]:
        tot.append(b + DFS(a))
    
    if len(tot) == 1:
        ans = max(ans,tot[0])
    else:
        for i in range(len(tot)):
            for j in range(i+1,len(tot)):
                ans = max(ans,tot[i] + tot[j])
    
    return max(tot)

DFS(1)
print(ans)

    