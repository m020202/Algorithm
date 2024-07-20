n,k = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(n)]
box.sort()
dp = [0] * (k+1)

for i in range(n):
    for j in range(k,box[i][0]-1,-1):
        dp[j] = max(dp[j], dp[j-box[i][0]] + box[i][1])

print(max(dp))