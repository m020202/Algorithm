import sys
s = list(map(str,input()))
t = list(map(str,input()))

def dfs(s,t):
    if len(s) == len(t):
        if s == t:
            print(1)
            sys.exit()
        return
    
    if t[-1] == 'B':
        t = t[::-1]
        if t[-1] == 'A':
            print(0)
            sys.exit()
        t.pop()
        dfs(s,t)
    
    else:
        dfs(s,t[:-1])
        if t[0] == 'B':
            k = t[::-1]
            k.pop()
            dfs(s,k)
    
dfs(s,t)
print(0)