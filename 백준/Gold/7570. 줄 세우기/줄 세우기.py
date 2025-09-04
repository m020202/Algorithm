import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))
dp = [0]*(N+1)
dp[arr[0]] = 1
for i in range(1,N):
    cur = arr[i]
    dp[cur] += (dp[cur-1]+1)

print(N-max(dp))