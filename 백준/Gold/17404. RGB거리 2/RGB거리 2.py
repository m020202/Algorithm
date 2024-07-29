import sys
INF = sys.maxsize
n = int(input())
box = [tuple(map(int,input().split())) for _ in range(n)]
dp = [[0]*3 for _ in range(n)]
ans = INF

def DP(num,end):
    global ans, dp
    dp[0][num] = box[0][num]
    dp[0][(num+1)%3] = INF
    dp[0][(num+2)%3] = INF

    for i in range(1,n-1):
        # 빨강
        dp[i][0] = box[i][0] + min(dp[i-1][1], dp[i-1][2])
        # 초록
        dp[i][1] = box[i][1] + min(dp[i-1][0], dp[i-1][2])
        # 파랑
        dp[i][2] = box[i][2] + min(dp[i-1][0], dp[i-1][1])
    
    ans = min(ans, box[-1][end] + dp[n-2][(end+1)%3], box[-1][end] + dp[n-2][(end+2)%3])

for i in range(3):
    DP(i,(i+1)%3)
    DP(i,(i+2)%3)
    
print(ans)
