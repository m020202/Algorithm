import sys
input = sys.stdin.readline
n = int(input())
box = [tuple(map(int,input().split())) for _ in range(n)]

search = {} # 탐색용
ch = {} # 체크용
for i,j in box:
    search[i] = j
    ch[i] = 0

cnt = 0
for j in range(n):
    i,cur = box[j]
    if ch[i] == 1 or cur == 0:
        continue
    cnt += 1
    for k in range(j+1, n):
        x,y = box[k]
        if y < cur:
            break
        elif y == cur:
            ch[x] = 1

print(cnt)