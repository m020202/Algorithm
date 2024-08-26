s = list(map(str,input()))
t = list(map(str,input()))

while True:
    if len(s) == len(t):
        if (s == t):
            print(1)
        else:
            print(0)
        break
    if t[-1] == 'A':
        t.pop()
        
    else:
        t.pop()
        t = t[::-1]