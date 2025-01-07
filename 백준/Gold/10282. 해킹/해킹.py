import heapq

t = int(input())
for _ in range(t):
    n,d,c = map(int,input().split())
    heap = []
    box = [[] for _ in range(n+1)]
    for _ in range(d):
        a,b,s = map(int,input().split())
        box[b].append((a,s))

    ans = [-1] * (n+1)
    ans[1] = 0
    # 초기 세팅
    for i in box[c]:
        heapq.heappush(heap, (i[1],c,i[0]))

    while heap:
        val,x,y = heapq.heappop(heap)
        if ans[y] == -1 or ans[y] > val:
            ans[y] = val
            for i in box[y]:
                heapq.heappush(heap, (ans[y] + i[1], y, i[0]))
    cnt = 0
    for i in range(1,n+1):
        if ans[i] >= 0:
            cnt += 1
    print(cnt,end=" ")
    print(max(ans))



