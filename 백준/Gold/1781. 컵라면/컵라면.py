import heapq

n = int(input())
box = []

for _ in range(n):
    x,y = map(int,input().split())
    heapq.heappush(box,(x,y))

ans = []

while box:
    cur = heapq.heappop(box)

    if len(ans) < cur[0]:
        heapq.heappush(ans,cur[1])
    elif len(ans) == cur[0]:
        if ans[0] < cur[1]:
            heapq.heappop(ans)
            heapq.heappush(ans,cur[1])

print(sum(ans))
    