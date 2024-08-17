import sys 
input = sys.stdin.readline
n,m,l = map(int,input().split())
box = [0] + list(map(int,input().split())) + [l]
box.sort()

lt = 1
rt = l-1
ans = 0
ch = [0] * (len(box)-1)
for i in range(len(box)-1):
    ch[i] = box[i+1] - box[i]

while (lt <= rt):
    mid = (lt + rt) // 2
    cnt = 0
    
    for i in ch:
        cnt += (i-1) // mid
    
    if cnt > m:
        lt = mid + 1
    else:
        rt = mid - 1
        ans = mid
    
print(ans)