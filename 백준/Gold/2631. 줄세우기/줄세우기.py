import sys
input = sys.stdin.readline
n = int(input())
box = [int(input()) for _ in range(n)]

dp = [0] * n
dp[0] = 1
for i in range(1,n):
    num = 0
    for j in range(i):
        if box[j] < box[i]:
            num = max(num, dp[j])
    dp[i] = num + 1

print(n - max(dp))