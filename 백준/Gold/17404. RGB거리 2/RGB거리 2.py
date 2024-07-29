import sys
INF = sys.maxsize
n = int(input())
box = [tuple(map(int,input().split())) for _ in range(n)]
dp = [[0]*3 for _ in range(n)]
ans = INF

# 0 1
dp[0][0] = box[0][0]
dp[0][1] = INF
dp[0][2] = INF
for i in range(1,n-1):
    # 빨강
    dp[i][0] = box[i][0] + min(dp[i-1][1], dp[i-1][2])
    # 초록
    dp[i][1] = box[i][1] + min(dp[i-1][0], dp[i-1][2])
    # 파랑
    dp[i][2] = box[i][2] + min(dp[i-1][0], dp[i-1][1])

ans = min(ans, box[-1][1] + dp[n-2][0], box[-1][1] + dp[n-2][2])

# 0 2
dp[0][0] = box[0][0]
dp[0][1] = INF
dp[0][2] = INF
for i in range(1,n-1):
    # 빨강
    dp[i][0] = box[i][0] + min(dp[i-1][1], dp[i-1][2])
    # 초록
    dp[i][1] = box[i][1] + min(dp[i-1][0], dp[i-1][2])
    # 파랑
    dp[i][2] = box[i][2] + min(dp[i-1][0], dp[i-1][1])

ans = min(ans, box[-1][2] + dp[n-2][0], box[-1][2] + dp[n-2][1])

# 1 0
dp[0][1] = box[0][1]
dp[0][0] = INF
dp[0][2] = INF
for i in range(1,n-1):
    # 빨강
    dp[i][0] = box[i][0] + min(dp[i-1][1], dp[i-1][2])
    # 초록
    dp[i][1] = box[i][1] + min(dp[i-1][0], dp[i-1][2])
    # 파랑
    dp[i][2] = box[i][2] + min(dp[i-1][0], dp[i-1][1])

ans = min(ans, box[-1][0] + dp[n-2][1], box[-1][0] + dp[n-2][2])
# 1 2
dp[0][1] = box[0][1]
dp[0][0] = INF
dp[0][2] = INF
for i in range(1,n-1):
    # 빨강
    dp[i][0] = box[i][0] + min(dp[i-1][1], dp[i-1][2])
    # 초록
    dp[i][1] = box[i][1] + min(dp[i-1][0], dp[i-1][2])
    # 파랑
    dp[i][2] = box[i][2] + min(dp[i-1][0], dp[i-1][1])

ans = min(ans, box[-1][2] + dp[n-2][0], box[-1][2] + dp[n-2][1])
# 2 0
dp[0][2] = box[0][2]
dp[0][0] = INF
dp[0][1] = INF
for i in range(1,n-1):
    # 빨강
    dp[i][0] = box[i][0] + min(dp[i-1][1], dp[i-1][2])
    # 초록
    dp[i][1] = box[i][1] + min(dp[i-1][0], dp[i-1][2])
    # 파랑
    dp[i][2] = box[i][2] + min(dp[i-1][0], dp[i-1][1])

ans = min(ans, box[-1][0] + dp[n-2][1], box[-1][0] + dp[n-2][2])
# 2 1
dp[0][2] = box[0][2]
dp[0][0] = INF
dp[0][1] = INF
for i in range(1,n-1):
    # 빨강
    dp[i][0] = box[i][0] + min(dp[i-1][1], dp[i-1][2])
    # 초록
    dp[i][1] = box[i][1] + min(dp[i-1][0], dp[i-1][2])
    # 파랑
    dp[i][2] = box[i][2] + min(dp[i-1][0], dp[i-1][1])

ans = min(ans, box[-1][1] + dp[n-2][0], box[-1][1] + dp[n-2][2])

print(ans)