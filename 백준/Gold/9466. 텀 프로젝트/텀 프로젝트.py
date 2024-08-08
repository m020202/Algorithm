import sys
input = sys.stdin.readline
sys.setrecursionlimit(65536)
t = int(input())

def checking(s,stack):
    global ans
    if ch[s] == 1 and s in stack:
        cur = stack.index(s)
        ans -= (len(stack)-cur)
            
    elif ch[s] == 0:
        ch[s] = 1
        stack.append(s)
        return checking(box[s],stack)

for _ in range(t):
    n = int(input())
    box = list(map(int,input().split()))
    box.insert(0,0)
    ch = [0] * (n+1)
    ans = n
    for i in range(1,n+1):
        if ch[i] == 0:
            ch[i] = 1
            checking(box[i],[i])

    print(ans)