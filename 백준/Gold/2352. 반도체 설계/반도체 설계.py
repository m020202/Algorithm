n = int(input())
box = list(map(int,input().split()))
ch = [0] * n
ch[0] = 1
for i in range(n):
    mx = 0
    for j in range(i):
        if box[i] > box[j]:
            mx = max(mx,ch[j])
        ch[i] = mx + 1

print(max(ch))