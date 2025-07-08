import sys
from collections import deque
input = sys.stdin.readline
box = list(map(str,input().rstrip()))
box = deque(box)
n = len(box)
txt = list(map(str,input().rstrip()))
m = len(txt)

idx = 0
stack = []
while box:
    cur = box.popleft()
    if cur == txt[idx]:
        stack.append((cur,idx))
        idx += 1
    else:
        if cur == txt[0]:
            stack.append((cur, 0))
            idx = 1
        else:
            stack.append((cur, -1))
            idx = 0
    if idx == m:
        for i in range(m):
            stack.pop()
        idx = stack[-1][1]+1 if stack else 0


if stack:
    for i,j in stack:
        print(i,end='')
else:
    print('FRULA')