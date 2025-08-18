import sys
input = sys.stdin.readline
INF = -sys.maxsize
sys.setrecursionlimit(10**4)
N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
dp = [[0]*M for _ in range(N)]
dp[0][0] = arr[0][0]
for i in range(1,M):
    dp[0][i] = arr[0][i] + dp[0][i-1]

for i in range(1,N):
    tmp = [[0]*3 for _ in range(M)]
    for j in range(M):
        tmp[j][0] = dp[i-1][j]+arr[i][j]

    tmp[0][1] = tmp[0][0]
    for j in range(1,M):
        tmp[j][1] = arr[i][j] + max(tmp[j-1][0],tmp[j-1][1])

    tmp[-1][2] = tmp[-1][0]
    for j in range(M-2,-1,-1):
        tmp[j][2] = arr[i][j] + max(tmp[j+1][0],tmp[j+1][2])

    for j in range(M):
        dp[i][j] = max(tmp[j])

print(dp[N-1][M-1])