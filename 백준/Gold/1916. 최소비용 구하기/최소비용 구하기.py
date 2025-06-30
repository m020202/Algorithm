import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize
n = int(input())
m = int(input())
box = [[] for _ in range(n+1)]
heap = []
for _ in range(m):
    s,a,v = map(int,input().split())
    box[s].append((v,a))
st,rt = map(int,input().split())
dp = [INF] * (n+1)
def Dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap,(0,start))
    while heap:
        val,now = heapq.heappop(heap)
        if dp[now] < val:
            continue
        for val2,nxt in box[now]:
            next_val = val2 + val
            if dp[nxt] > next_val:
                dp[nxt] = next_val
                heapq.heappush(heap,(next_val,nxt))
Dijkstra(st)
print(dp[rt])