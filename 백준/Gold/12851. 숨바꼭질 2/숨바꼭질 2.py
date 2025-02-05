import sys
from collections import deque
input = sys.stdin.readline
n,k = map(int,input().split())

# 각 위치에 도달하는 최단 시간
box = [-1] * 200000
box[n] = 0

# 각 위치 최단 시간 방법 수
tot = [1] * 200000

dq = deque()
dq.append(n)
while dq:
    cur = dq.popleft()
    num = box[cur]

    # 순간 이동
    next = cur * 2
    if next < 200000:
        if box[next] == -1:
            box[next] = num + 1
            dq.append(next)
        elif box[next] > num + 1:
            box[next] = num + 1
            tot[next] = 1
            dq.append(next)
        elif box[next] == num + 1:
            tot[next] += 1
            dq.append(next)

    # 앞으로
    next = cur + 1
    if next < 200000:
        if box[next] == -1:
            box[next] = num + 1
            dq.append(next)
        elif box[next] > num + 1:
            box[next] = num + 1
            tot[next] = 1
            dq.append(next)
        elif box[next] == num + 1:
            tot[next] += 1
            dq.append(next)
    # 뒤로
    next = cur - 1
    if next >= 0:
        if box[next] == -1:
            box[next] = num + 1
            dq.append(next)
        elif box[next] > num + 1:
            box[next] = num + 1
            tot[next] = 1
            dq.append(next)
        elif box[next] == num + 1:
            tot[next] += 1
            dq.append(next)

print(box[k])
print(tot[k])