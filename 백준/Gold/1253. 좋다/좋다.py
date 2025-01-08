import sys
input = sys.stdin.readline
n = int(input())
box = list(map(int,input().split()))
box.sort()

dic = {}
ch = {}
for i in box:
    if i in dic.keys():
        dic[i] += 1
    else:
        dic[i] = 1
        ch[i] = 0

s = set(box)
ans = 0
for i in range(n):
    for j in range(i+1, n):
        if box[i] == 0 and box[j] == 0:
            if dic[0] < 3:
                continue
        elif box[i] == 0 and box[j] != 0:
            if dic[box[j]] == 1:
                continue
        elif box[i] != 0 and box[j] == 0:
            if dic[box[i]] == 1:
                continue
        cur = box[i] + box[j]
        if cur in s and ch[cur] == 0:
            ch[cur] = 1
            ans += dic[cur]

print(ans)

