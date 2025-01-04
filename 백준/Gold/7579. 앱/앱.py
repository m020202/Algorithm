n,m = map(int,input().split())
a = [0] + list(map(int,input().split()))
c = [0] + list(map(int,input().split()))
dp = [[0] * (sum(c) + 1) for _ in range(n+1)]

for i in range(1, n+1):
    cur = a[i]
    val = c[i]
    for j in range(sum(c) + 1):
        if val > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-val] + cur)

for i in range(sum(c) + 1):
    if dp[-1][i] >= m:
        print(i)
        break

