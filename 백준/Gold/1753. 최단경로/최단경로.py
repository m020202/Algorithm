import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize
n,e = map(int,input().split())
k = int(input())

# 각 정점별 갈 수 있는 경로 정의
dic = {}
for i in range(1,n+1):
    dic[i] = []
for _ in range(e):
    u,v,w = map(int,input().split())
    dic[u].append((v,w))

ans = [INF] * (n+1)
ans[k] = 0

heap = []
heapq.heappush(heap,(0,k))
while heap:
    curW, curV = heapq.heappop(heap)
    if ans[curV] < curW:
        continue
    for v,w in dic[curV]:
        if ans[v] > w + ans[curV]:
            ans[v] = w + ans[curV]
            heapq.heappush(heap,(ans[v],v))

for i in range(1,n+1):
    if ans[i] == INF:
        print("INF")
    else:
        print(ans[i])



