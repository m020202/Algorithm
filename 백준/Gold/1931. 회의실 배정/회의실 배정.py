import heapq,sys
input = sys.stdin.readline
N = int(input())
box = [list(map(int,input().split())) for _ in range(N)]
heap = []
for i,j in box:
    heapq.heappush(heap, (j,i))

cnt = 0
last = 0
while heap:
    j,i = heapq.heappop(heap)
    if i >= last:
        last = j
        cnt += 1

print(cnt)