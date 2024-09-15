import sys
input = sys.stdin.readline
n = int(input())
box = list(map(int,input().split()))
ch = []
tot = 0
for i in range(n):
    cur = box[i]
    if cur in ch:
        ch.remove(box[i])
        ch.append(cur-1)
    else:
        tot += 1
        ch.append(cur-1)
        
print(tot)