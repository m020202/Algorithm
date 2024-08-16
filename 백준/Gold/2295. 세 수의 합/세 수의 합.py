import sys
input = sys.stdin.readline
n = int(input())
box = [int(input()) for _ in range(n)]
box.sort()
tmp = set()
for i in range(n):
    for j in range(i,n):
        tmp.add(box[i]+box[j])

for i in range(n-1,-1,-1):
    for j in range(i+1):
        if box[i] - box[j] in tmp:
            print(box[i])
            sys.exit(0)