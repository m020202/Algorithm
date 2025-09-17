import sys, heapq
input = sys.stdin.readline
N,M = map(int,input().split())
dic = {i:{} for i in range(1,N+1)}
for _ in range(M):
    a,b,c = map(int,input().split())
    if b in dic[a]:
        dic[a][b] = max(c,dic[a][b])
        dic[b][a] = max(c,dic[b][a])
    else:
        dic[a][b] = c
        dic[b][a] = c

# 출발지, 도착지
s,d = map(int,input().split())
ch = [0]*(N+1)
ch[s] = sys.maxsize

# 초기 dq 세팅
heap = []
for i in dic[s]:
    ch[i] = dic[s][i]
    heapq.heappush(heap,(-dic[s][i],i))

while heap:
    value,dest = heapq.heappop(heap)
    value = -value
    if dest == d:
        print(value)
        sys.exit()
    else:
        for i in dic[dest]:
            new_value = min(value,dic[dest][i])
            if new_value > ch[i]:
                ch[i] = new_value
                heapq.heappush(heap,(-new_value,i))