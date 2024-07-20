n,k = map(int,input().split())
box = [int(input()) for _ in range(n)]
box.sort()
dp = [0] * (k+1)
dp[0] = 1
for i in box:
    for j in range(i,k+1):
        dp[j] += dp[j-i]

print(dp[-1])