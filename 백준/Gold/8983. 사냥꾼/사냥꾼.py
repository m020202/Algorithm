m,n,l = map(int,input().split())
box1 = list(map(int,input().split()))
box1.sort()
box2 = []
cnt = 0
for _ in range(n):
    x,y = map(int,input().split())
    box2.append((x,y))

for x,y in box2:
    if x < box1[0]:
        if abs(box1[0]-x) + y <= l:
            cnt += 1
        continue
    if x > box1[-1]:
        if abs(box1[-1]-x) + y <= l:
            cnt += 1
        continue
    lt = -1
    rt = m
    while lt + 1 < rt:
        mid = (lt + rt) // 2
        if box1[mid] >= x:
            rt = mid
        else:
            lt = mid
    if rt > 0:
        num = min(abs(box1[rt]-x),abs(box1[rt-1]-x))
    else:
        num = abs(box1[rt]-x)
    if num + y <= l:
        cnt += 1
print(cnt)