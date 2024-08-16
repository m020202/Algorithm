n = int(input())
k = int(input())

def find(x):
    cnt = 0
    for i in range(1,n+1):
        if i > x:
            break
        num = x//i
        num = min(num,n)
        cnt += num
    return cnt

lt = 0
rt = k+1
ans = 0
while lt+1 < rt:
    mid = (lt + rt) // 2
    cnt = find(mid)
    if cnt >= k:
        rt = mid 
    else:
        lt = mid 
    ans = rt

print(ans)




