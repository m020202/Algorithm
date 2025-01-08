import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
box = [list(map(int,input().split())) for _ in range(n)]
p = list(map(int,input().split()))
for i in range(n):
    box[i][i] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if box[i][j] == 0:
                if box[i][k] != 0 and box[k][j] != 0:
                    box[i][j] = 1
                    box[j][i] = 1

for i in range(m-1):
    cur = p[i] - 1
    next = p[i+1] - 1
    if box[cur][next] == 0:
        print("NO")
        break
else:
    print("YES")