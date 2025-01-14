import sys
input = sys.stdin.readline
n = int(input())
box = list(map(int,input().split()))

ans = 0
idx = -1
for i in range(n):
    x,y = i,box[i]
    tmp = 0
    for j in range(i):
        xx,yy = j, box[j]
        h = (y - yy) / (x - xx)
        y_in = yy - h*xx
        for k in range(j+1, i):
            if (k*h+y_in) <= box[k]:
                break
        else:
            tmp += 1

    for j in range(n-1, i, -1):
        xx, yy = j, box[j]
        h = (yy - y) / (xx - x)
        y_in = yy - h * xx
        for k in range(j-1, i, -1):
            if (k*h+y_in) <= box[k]:
                break
        else:
            tmp += 1

    if ans<tmp:
        idx = i
        ans = tmp

print(ans)

