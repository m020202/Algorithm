import sys
input = sys.stdin.readline
a = list(input().rstrip())
b = list(input().rstrip())
n = len(a)
m = len(b)
box = [[""] * (m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1, m+1):
        if a[i-1] == b[j-1]:
            box[i][j] = box[i-1][j-1] + a[i-1]
        else:
            box[i][j] = box[i-1][j] if len(box[i-1][j]) > len(box[i][j-1]) else box[i][j-1]
ans = box[-1][-1]
print(len(ans))
if (len(ans) != 0):
    print(ans)