import sys
input = sys.stdin.readline
n,l = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(n)]
box.sort()
cur = 0
cnt = 0

for i,j in box:
    j-=1
    if i > cur:
        cur = i

    while cur <= j:
        cur += l
        cnt += 1
print(cnt)