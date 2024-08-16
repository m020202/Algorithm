import sys
input = sys.stdin.readline
n,m = map(int,input().split())
t = [int(input()) for _ in range(n)]
t.sort()
l = t[0]
r = t[-1] * m
ans = r+1
while l <= r:
    mid = (l+r) // 2
    tot = 0
    for i in t:
        tot += (mid // i)
    
    # 수용 가능 인원이 총 인원보다 많거나 같을 때
    if tot >= m:
        ans = min(ans,mid)
        r = mid - 1
    # 수용 가능 인원이 총 인원보다 적
    else:
        l = mid + 1

print(ans)

