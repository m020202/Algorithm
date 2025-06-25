import sys
from collections import deque
input = sys.stdin.readline
n,k = map(int,input().split())
ch = [-1] * 100001
ch[n] = 0

dq = deque()
dq.append(n)
while dq:
    cur = dq.popleft()
    # +1로 이동
    if cur < 100000:
        tmp = cur + 1
        if ch[tmp] == -1 or ch[tmp] > ch[cur] + 1:
            ch[tmp] = ch[cur] + 1
            dq.append(tmp)
    # -1로 이동
    if cur > 0:
        tmp = cur - 1
        if ch[tmp] == -1 or ch[tmp] > ch[cur] + 1:
            ch[tmp] = ch[cur] + 1
            dq.append(tmp)
    # *2로 이동
    if cur*2 <= 100000:
        tmp = cur * 2
        if ch[tmp] == -1 or ch[tmp] > ch[cur]:
            ch[tmp] = ch[cur]
            dq.append(tmp)

print(ch[k])