import sys
from collections import deque
t = int(input())

for _ in range(t):
    # 입력 받기
    p = input()
    n = int(input())
    arr = input()[1:-1]

    # 배열이 빈 값일 경우
    if n == 0:
        dq = deque([])
    else:
        dq = deque(list(map(int,arr.split(","))))
    tmp = True
    curDir = 0 # 진행 방향, 0->왼쪽부터, 1->오른쪽부터
    for i in p:
        if i == 'R':
            curDir = 1-curDir
        else:
            if len(dq) == 0:
                print('error')
                tmp = False
                break
            if curDir == 0:
                dq.popleft()
            else:
                dq.pop()

    if tmp:
        if curDir == 1:
            dq.reverse()

        result = ','.join(map(str,dq))
        print('[' + result + ']')
