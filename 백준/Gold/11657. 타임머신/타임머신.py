import sys
input = sys.stdin.readline
INF = sys.maxsize
n,m = map(int,input().split())
edges = [list(map(int,input().split())) for _ in range(m)]
distance = [INF] * (n+1)

def bf(start):
    distance[start] = 0
    for i in range(n):
        for a,b,c in edges:
            if distance[a] != INF and distance[b] > distance[a] + c:
                distance[b] = distance[a] + c
                if i == n-1:
                    return True
    return False

result = bf(1)
if result:
    print("-1")
else:
    print(*(-1 if distance[i] == INF else distance[i] for i in range(2, n + 1)), sep='\n')