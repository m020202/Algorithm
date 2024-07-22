import sys
n = int(input())
dp = [0] * (n+1)
if n == 1:
    print(0)
    sys.exit()
dp[2] = 3
prev = [1]
for i in range(4,n+1):
    if i%2 != 0:
        continue
    ans = 3 * dp[i-2]
    cur = dp[i-4] + prev[-1]
    prev.append(cur)
    ans += (2*cur)
    dp[i] = ans
print(dp[-1])