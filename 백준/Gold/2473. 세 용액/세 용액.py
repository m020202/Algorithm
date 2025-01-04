import sys
n = int(input())
box = list(map(int,input().split()))
box.sort()
ans = sys.maxsize
t = []
for i in range(n-2):
    cur = box[i]
    lt = i + 1
    rt = n - 1
    while lt < rt:
        tmp = box[lt] + box[rt]
        if abs(ans) > abs(cur + tmp):
            ans = cur + tmp
            t = [box[i],box[lt],box[rt]]
        if cur+tmp <= 0:
            lt += 1
        else:
            rt -= 1

for i in t:
    print(i, end=" ")
    