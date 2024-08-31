import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    box = list(map(str,input()))
    box.pop()
    dQ = deque(box)
    n = int(input())

    k = input()
    if len(k) == 3:
        ac = deque()
    else:
        ac = deque(list(k[1:-2].split(',')))

    tmp = 0
    # 0: 왼 -> 오, 1: 오 -> 왼
    dir = 0
    while dQ:
        cur = dQ.popleft()
        # R -> 순서 뒤집기
        if cur == 'R':
            if dir == 0:
                dir = 1
            else:
                dir = 0
        # D -> 맨 앞 원소 버리기
        else:
            if len(ac) == 0:
                tmp = 1
                break
            if dir == 0:
                ac.popleft()
            else:
                ac.pop()

    if not tmp:
        print("[",end='')
        if dir == 0:
            for i in range(len(ac)):
                if i == len(ac)-1:
                    print(str(ac[i]),end='')
                else:
                    print(str(ac[i])+',', end='')
        if dir == 1:
            for i in range(len(ac)-1,-1,-1):
                if i == 0:
                    print(str(ac[i]),end='')
                else:
                    print(str(ac[i])+',',end='')
        print("]")
    else:
        print("error")

