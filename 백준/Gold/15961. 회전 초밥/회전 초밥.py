import sys
input = sys.stdin.readline
n,d,k,c = map(int,input().split())
box = [int(input()) for _ in range(n)]

ans = 0
ch = [0] * 3001
visited = [0] * n

lt = 0
rt = k - 1
while visited[lt] == 0:
    # lt = 0일 때
    if (lt == 0):
        a = box[lt:rt + 1] + [c]
        for i in a:
            ch[i] += 1
        s = set(a)
        ans = len(s)
    visited[lt] = 1
    ch[box[lt]] -= 1
    if ch[box[lt]] == 0:
        s.remove(box[lt])
    lt = (lt + 1 + n) % n
    rt = (rt + 1 + n) % n
    ch[box[rt]] += 1
    s.add(box[rt])
    ans = max(ans, len(s))

print(ans)



