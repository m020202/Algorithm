import sys
INF = sys.maxsize
n = int(input())
box = [tuple(map(int,input().split())) for _ in range(n)]
dp = [[0]*3 for _ in range(n)]
ans = INF

for i in range(3):
    dp = [[INF] * 3 for _ in range(n)]
    dp[0][i] = box[0][i]
    for j in range(1,n):
        dp[j][0] = box[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = box[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = box[j][2] + min(dp[j-1][0], dp[j-1][1])
    
    dp[-1][i] = INF
    ans = min(ans, min(dp[-1]))

print(ans)