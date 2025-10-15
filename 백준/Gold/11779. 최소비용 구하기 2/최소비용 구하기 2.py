import sys, heapq
input = sys.stdin.readline
n = int(input())
m = int(input())

dic = {i:[] for i in range(1,n+1)} # 각 도시별 이동 가능한 도시 정보
for _ in range(m):
    a,b,c = map(int,input().split())
    dic[a].append((b,c))

s,e = map(int,input().split())

heap = []
heapq.heappush(heap,(0,s,[s]))

ch = [-1]*(n+1)
ch[s] = 0

tot = 0
ans = []
while heap:
    val,cur,arr = heapq.heappop(heap)
    if cur == e:
        print(val)
        print(len(arr))
        print(*arr)
        break
    for nxt,w in dic[cur]:
        if ch[nxt] == -1 or ch[nxt] > val+w:
            ch[nxt] = val+w
            heapq.heappush(heap,(val+w,nxt,arr+[nxt]))

