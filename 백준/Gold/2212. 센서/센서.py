import math

n = int(input())
k = int(input())
box = list(map(int,input().split()))
box.sort()

ch = []
for i in range(n):
    if (i == n-1):
        break
    num = box[i+1] - box[i]
    ch.append(num)

ch.sort()

ans = sum(ch[:(n-k)])
print(ans)

