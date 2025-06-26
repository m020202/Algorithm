n,s = map(int,input().split())
box = list(map(int,input().split()))

lt = 0
rt = 0
tot = box[lt]
ans = n+1
while True:
    if tot >= s:
        ans = min(ans,rt-lt+1)
        tot -= box[lt]
        lt += 1
    else:
        if rt == n-1:
            break
        rt += 1
        tot += box[rt]
if ans == n+1:
    print(0)
else:
    print(ans)