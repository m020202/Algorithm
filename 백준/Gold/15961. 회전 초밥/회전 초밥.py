import sys
input = sys.stdin.readline
n,d,k,c = map(int,input().split())
box = [int(input()) for _ in range(n)]

ans = 0
ch = [0] * 3001
a = box[:k] + [c]
for i in a:
    ch[i] += 1
tot = len(set(a))

ans = tot
for i in range(1, n):
    ch[box[i-1]] -= 1
    if (ch[box[i-1]] == 0):
        tot -= 1
    rt = (i + k - 1 + n) % n
    if (ch[box[rt]] == 0):
        ch[box[rt]] = 1
        tot += 1
    else:
        ch[box[rt]] += 1
    ans = max(ans, tot)

print(ans)



