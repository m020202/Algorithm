import sys
input = sys.stdin.readline
n,m = map(int,input().split())
box = list(map(int,input().split()))
tot = 0
ans = 0
remain = [0] * (m+1)
for i in range(n):
    tot += box[i]
    if not tot % m:
        ans += 1
    remain[tot % m] += 1

for i in remain:
    if i > 1:
        ans += (i * (i-1) // 2)

print(ans)

