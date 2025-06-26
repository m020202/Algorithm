import sys
input = sys.stdin.readline
n,s = map(int,input().split())
box = list(map(int,input().split()))
l = 0
r = 1
ans = n+1
cur = box[0]
while True:
    if cur >= s:
        ans = min(ans, r - l)
        cur -= box[l]
        l += 1
    elif r == n:
        break
    else:
        cur += box[r]
        r += 1

print(0 if ans == n+1 else ans)