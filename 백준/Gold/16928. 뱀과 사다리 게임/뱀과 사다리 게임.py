import sys
from collections import deque
input = sys.stdin.readline
ans = [103] * 101
ans[1] = 0
n,m = map(int,input().split())
dic = [0] * 101
for i in range(n+m):
    x, y = map(int, input().split())
    dic[x] = y

# 초기 값 세팅
dq = deque()
for i in range(1, 7):
    if dic[1+i] != 0:
        if ans[dic[1+i]] > 1:
            ans[dic[1+i]] = 1
            dq.append((dic[1+i], 1))
    else:
        ans[1+i] = 1
        dq.append((1+i,1))


while dq:
    cur, cnt = dq.popleft()
    for i in range(1, 7):
        if cur+i > 100:
            break
        if dic[cur+i] != 0:
            if ans[dic[cur+i]] > cnt + 1:
                ans[dic[cur+i]] = cnt + 1
                dq.append((dic[cur+i], cnt + 1))
        else:
            if ans[cur+i] > cnt + 1:
                ans[cur+i] = cnt + 1
                dq.append((cur+i, cnt + 1))

print(ans[100])