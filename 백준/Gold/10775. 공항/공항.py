import sys
input = sys.stdin.readline
g = int(input())
p = int(input())
box = [int(input()) for _ in range(p)]
ch = list(range(g+1))
ans = 0
def find(cur):
    while True:
        if cur == ch[cur]:
            return cur
        ch[cur] = ch[ch[cur]]
        cur = ch[cur]

for i in box:
    cur = find(i)
    if not cur:
        print(ans)
        sys.exit()
    else:
        ans += 1
        ch[cur] = cur-1
        ch[i] = cur-1
print(ans)


