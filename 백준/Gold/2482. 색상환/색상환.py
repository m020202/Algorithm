import sys
input = sys.stdin.readline
N = int(input())
K = int(input())
R = 1000000003
tot = 0
dp = [[-1]*(N+1) for _ in range(K+1)]
def func(x,y): # x개 중 y개를 인접 하지 않게 고르는 경우의 수
    if y == 0:
        return 1
    if y == 1:
        dp[y][x] = x
        return x
    if dp[y][x] != -1:
        return dp[y][x]
    res = 0
    for i in range(x-2,y-2,-1):
        res += func(i,y-1)
    dp[y][x] = res
    return res

print((func(N-3,K-1)+func(N-1,K))%R)