import sys, heapq
input = sys.stdin.readline
n = int(input())
box = [0] + list(map(int,input().split()))
heap = []
for i in range(1,n+1):
    heapq.heappush(heap, (box[i],i))
m = int(input())
for _ in range(m):
    q = list(map(int,input().split()))
    if len(q) == 1:
        cur = heapq.heappop(heap)
        while (box[cur[1]] != cur[0]):
            cur = heapq.heappop(heap)
        print(cur[1])
        heapq.heappush(heap, cur)
    else:
        i,v = q[1],q[2]
        box[i] = v
        heapq.heappush(heap, (v,i))