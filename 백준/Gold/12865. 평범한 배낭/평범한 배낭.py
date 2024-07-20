n,k = map(int,input().split())
box = []
dp = [0] * (k+1)
for _ in range(n):
    w,v = map(int,input().split())
    box.append((w,v))

for w,v in box:
    for i in range(k,w-1,-1):
        dp[i] = max(dp[i], v + dp[i-w])

print(max(dp))