n = int(input())
box = list(map(int,input().split()))
mx = max(box)
point = [0] * (mx + 1)
ch = [0] * (mx + 1)

for i in box:
    ch[i] = 1

for i in box:
    for j in range(i * 2, mx+1, i):
        if ch[j] == 1:
            point[i] += 1
            point[j] -= 1


for i in box:
    print(point[i], end=' ')