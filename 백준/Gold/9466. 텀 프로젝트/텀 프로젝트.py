import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)
t = int(input())

def checking(s):
    global ans
    if ch[s] == 1:
        if s in stack:
            ans -= (len(stack)-stack.index(s))
    else:
        ch[s] = 1
        stack.append(s)
        return checking(box[s])

for _ in range(t):
    n = int(input())
    box = [0] + list(map(int,input().split()))
    ch = [0] * (n+1)
    ans = n
    for i in range(1,n+1):
        if ch[i] == 0:
            ch[i] = 1
            stack = [i]
            checking(box[i])

    print(ans)