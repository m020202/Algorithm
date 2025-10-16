import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
dic = {i:[] for i in range(1,N+1)}
for _ in range(N-1):
    a,b = map(int,input().split())
    dic[a].append(b)
    dic[b].append(a)

parent = [0] * (N+1)
parent[1] = 1

# 트리 셋팅
dq = deque([(0,1)])
while dq:
    prev,cur = dq.popleft()
    for i in dic[cur]:
        if i != prev:
            parent[i] = cur
            dq.append((cur,i))


def find_father(cur):
    par = cur
    ans = [cur]
    while par != 1:
        par = parent[par]
        ans.append(par)
    return ans

def compare(a,b):
    a_par = find_father(a)
    b_par = find_father(b)
    ans = 1
    idx = -1
    while idx >= -min(len(a_par),len(b_par)):
        if a_par[idx] != b_par[idx]:
            break
        ans = a_par[idx]
        idx -= 1
    return ans

M = int(input())
for _ in range(M):
    a,b = map(int,input().split())
    print(compare(a,b))