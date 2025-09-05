import sys
input = sys.stdin.readline
N = int(input())
chu = list(map(int,input().split()))
M = int(input())
gu = list(map(int,input().split()))

# 측정 가능한 무게 확인
dp = [0] * (sum(chu)+1)
dp[0] = 1
cur = 2
for i in chu:
    for j in range(len(dp)):
        if 0<dp[j]<cur and dp[i+j] == 0:
            dp[i+j] = cur
    cur += 1

for i in gu:
    for j in range(len(dp)):
        if dp[j] > 0 and j+i < len(dp) and dp[j+i] > 0:
            print("Y",end=' ')
            break
    else:
        print("N",end=' ')