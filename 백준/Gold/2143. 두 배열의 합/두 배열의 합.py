from collections import deque
t = int(input())
n = int(input())
box1 = list(map(int,input().split()))
box1 = deque(box1)
m = int(input())
box2 = list(map(int,input().split()))
box2 = deque(box2)

ch1 = {}
ch3 = []
while box1:
    now = box1.popleft()
    cnt = now
    ch3.append(cnt)
    if cnt in ch1:
        ch1[cnt] += 1
    else:
        ch1[cnt] = 1
    for i in box1:
        cnt += i
        ch3.append(cnt)
        if cnt in ch1:
            ch1[cnt] += 1
        else:
            ch1[cnt] = 1
ch3.sort()

ch2 = {}
ch4 = []
while box2:
    now = box2.popleft()
    cnt = now
    ch4.append(cnt)
    if cnt in ch2:
        ch2[cnt] += 1
    else:
        ch2[cnt] = 1
    for i in box2:
        cnt += i
        ch4.append(cnt)
        if cnt in ch2:
            ch2[cnt] += 1
        else:
            ch2[cnt] = 1
ch4.sort()

ans = 0

for i in ch3:
    lt = -1
    rt = len(ch4)
    while lt + 1 < rt:
        mid = (lt + rt) // 2
        if i+ch4[mid] == t:
            ans += ch2[ch4[mid]]
            break
        elif i+ch4[mid] < t:
            lt = mid
        else:
            rt = mid

print(ans)