from collections import deque

n,m = map(int,input().split())
box = list(map(int,input().split()))
box.sort()
dQ1 = deque()
dQ2 = deque()

for i in box:
    if i < 0:
        dQ1.append(i)
    else:
        dQ2.append(i)

neg = deque()
cur = 0
while dQ1:
    now = dQ1.popleft()
    if(cur > 0):
        cur -= 1
        continue
    neg.append(now)
    cur = m-1

pos = deque()
cur = 0
while dQ2:
    now = dQ2.pop()
    if (cur > 0):
        cur -= 1
        continue
    pos.append(now)
    cur = m-1

ans = 0

if (neg and pos):
    if abs(neg[0]) >= pos[0] or len(pos) == 0:
        ans += abs(neg[0])
        neg.popleft()
    else:
        ans += pos[0]
        pos.popleft()
elif (neg):
    ans += abs(neg[0])
    neg.popleft()
elif (pos):
    ans += pos[0]
    pos.popleft()
    
new = neg + pos
for i in new:
    ans += (abs(i) * 2)

print(ans)