import heapq

n = int(input())
box = []

for _ in range(n):
    p,d = map(int,input().split())
    heapq.heappush(box,(d,p))

i = 0
result = []
while box:
    cur = heapq.heappop(box)
    if (cur[0] != i):
        i = cur[0]
    
    if (len(result) < i):
        heapq.heappush(result,cur[1])
    elif (len(result) == i):
        if (result[0] < cur[1]):
            heapq.heappop(result)
            heapq.heappush(result,cur[1])
    
print(sum(result))

