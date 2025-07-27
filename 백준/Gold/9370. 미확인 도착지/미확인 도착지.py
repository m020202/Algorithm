import sys
from collections import deque
input = sys.stdin.readline
T = int(input())

def djikstra(a,b,dic):
    # 최단 거리 탐색
    w = [2000000000] * (n + 1)  # 가중치
    w[a] = 0
    dq = deque([(a,0)])
    while dq:
        cur, val = dq.popleft()
        if w[cur] < val:
            continue
        for i, j in dic[cur]:
            if w[i] > val + j:
                w[i] = val + j
                dq.append((i,w[i]))
    return w[b]


for _ in range(T):
    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())
    dic = {i:[] for i in range(1,n+1)}
    num = 0
    for _ in range(m):
        a,b,d = map(int,input().split())
        dic[a].append((b,d))
        dic[b].append((a,d))
        if (a == g and b == h) or (a == h and b == g):
            num = d
    dst = [int(input()) for _ in range(t)]
    dst.sort()
    for i in dst:
        min_val = djikstra(s,i,dic)
        # case 1
        if djikstra(s,g,dic) + num + djikstra(h,i,dic) == min_val:
            print(i,end=' ')
            continue
        # case 2
        if djikstra(s,h,dic) + num + djikstra(g,i,dic) == min_val:
            print(i, end=' ')
            continue
    print()
