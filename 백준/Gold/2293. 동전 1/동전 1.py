import sys
input = sys.stdin.readline
n,k = map(int,input().split())
box = [int(input()) for _ in range(n)]
box.sort()
ch = [0] * (k+1)
ch[0] = 1
for i in box:
    for j in range(1,k+1):
        if j >= i:
            ch[j] += ch[j-i]

print(ch[k])