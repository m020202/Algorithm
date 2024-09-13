import heapq

n,k = map(int,input().split())
box = []

for _ in range(n):
    m,v = map(int,input().split())
    heapq.heappush(box,(m,v))

bag = []

for _ in range(k):
    bag.append(int(input()))

bag.sort()

answer = []
tot = 0
for i in bag:
    while box and box[0][0] <= i:
        heapq.heappush(answer, -heapq.heappop(box)[1])
    
    if answer:
        tot -= heapq.heappop(answer)
    elif not box:
        break

print(tot)