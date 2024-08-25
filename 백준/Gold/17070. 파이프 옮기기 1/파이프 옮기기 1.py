import sys
from collections import deque
INF = sys.maxsize
input = sys.stdin.readline
n = int(input())
box = [list(map(int,input().split())) for _ in range(n)]
# 오른쪽 방향으로 도착
dp1 = [[0] * n for _ in range(n)]
# 대각선 방향으로 도착
dp2 = [[0] * n for _ in range(n)]
# 아래 방향으로 도착
dp3 = [[0] * n for _ in range(n)]

for i in range(1,n):
    if box[0][i] == 1:
        break
    dp1[0][i] = 1

for i in range(1,n):
    for j in range(2,n):
        if box[i][j] == 1:
            continue
        dp1[i][j] = dp1[i][j-1] + dp2[i][j-1]
        if box[i][j-1] == 0 and box[i-1][j] == 0:
            dp2[i][j] = dp1[i-1][j-1] + dp2[i-1][j-1] + dp3[i-1][j-1]
        dp3[i][j] = dp2[i-1][j] + dp3[i-1][j]

print(dp1[n-1][n-1] + dp2[n-1][n-1] + dp3[n-1][n-1])