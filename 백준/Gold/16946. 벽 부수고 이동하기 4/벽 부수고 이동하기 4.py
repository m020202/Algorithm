import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
box = [list(map(int,input().rstrip())) for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

# 0으로 이루어진 영역 체크.
ch = [[-1]*m for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 0 and ch[i][j] == -1:
            dq = deque([(i,j)])
            ch[i][j] = cnt
            while dq:
                x,y = dq.popleft()
                for k in range(4):
                    xx = x + dx[k]
                    yy = y + dy[k]
                    if 0<=xx<n and 0<=yy<m:
                        if box[xx][yy] == 0 and ch[xx][yy] == -1:
                            ch[xx][yy] = cnt
                            dq.append((xx,yy))
            cnt += 1

# 각 영역의 크기 체크
value = [0] * (n*m)
for i in range(n):
    for j in range(m):
        if ch[i][j] != -1:
            value[ch[i][j]] += 1

ans = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            num = 1
            tmp = set()
            for k in range(4):
                ii = i + dx[k]
                jj = j + dy[k]
                if 0<=ii<n and 0<=jj<m:
                    if box[ii][jj] == 0 and ch[ii][jj] not in tmp:
                        num += value[ch[ii][jj]]
                        tmp.add(ch[ii][jj])
            ans[i][j] = num%10
for i in ans:
    print(''.join(map(str,i)))