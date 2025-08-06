import sys
from collections import deque
import copy
input = sys.stdin.readline
N,K = map(int,input().split())
M = len(str(N))
if M == 1:
    print(-1)
    sys.exit()

def swapping(box,i,j):
    tmp = copy.deepcopy(box)
    tmp[i],tmp[j] = tmp[j],tmp[i]
    return ''.join(map(str,tmp))

ans = -1
dq = deque([(str(N),0)])
dic = {}
dic[str(N)] = {0}
while dq:
    cur,cnt = dq.popleft()
    if cnt == K:
        ans = max(ans,int(cur))
        continue
    if cur[0] == '0':
        continue
    arr = [int(i) for i in str(cur)]
    for i in range(M):
        for j in range(i+1,M):
            new = swapping(arr,i,j)
            if new[0] == '0':
                continue
            if new in dic:
                if cnt+1 in dic[new]:
                    continue
                else:
                    dic[new].add(cnt+1)
            else:
                dic[new] = {cnt+1}
            dq.append((new,cnt+1))

print(ans)


