import sys
input = sys.stdin.readline
INF = sys.maxsize
n = int(input())
matrix = [()]
box = [[0] * (n+1) for _ in range(n+1)]
for _ in range(n):
    r,c = map(int,input().split())
    matrix.append((r,c))

def chain(l,r):
    if l == r:
        return 0
    if box[l][r] != 0:
        return box[l][r]
    mx = INF
    for i in range(l,r):
        cur = chain(l,i) + chain(i+1,r) + matrix[l][0] * matrix[i][1] * matrix[r][1]
        mx = min(mx,cur)
    box[l][r] = mx
    return mx

chain(1,n)
print(box[1][n])

