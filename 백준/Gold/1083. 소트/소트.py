import sys,copy
input = sys.stdin.readline

n = int(input())
box = list(map(int,input().split()))
s = int(input())

for i in range(n):
    max_num = max(box[i:min(n, i + s + 1)])
    idx = box.index(max_num)

    for j in range(idx,i,-1):
        box[j],box[j-1] = box[j-1],box[j]
    
    s -= (idx-i)
    if s <= 0:
        break

print(*box)


