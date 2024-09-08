import heapq

n = int(input())
que = []

for _ in range(n):
    d,w = map(int,input().split())
    heapq.heappush(que,(d,w))

ans = []

while que:
    cur = heapq.heappop(que)

    if cur[0] > len(ans):
        heapq.heappush(ans,cur[1])
    elif cur[0] == len(ans):
        if cur[1] > ans[0]:
            heapq.heappop(ans)
            heapq.heappush(ans,cur[1])
    
print(sum(ans))

    