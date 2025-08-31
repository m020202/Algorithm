import sys
input = sys.stdin.readline
arr = list(map(int,input().split()))
d1 = [i for i in range(0,41,2)]
d2 = [10,13,16,19,25,30,35,40]
d3 = [20,20,22,24,25,30,35,40]
d4 = [30,28,27,26,25,30,35,40]

ans = 0
def func(idx, horse, tot):
    global ans
    if idx == len(arr) or not horse:
        ans = max(ans,tot)
        return
    cur = arr[idx]
    for i in range(len(horse)):
        l,x = horse[i]
        x += cur
        if l == "d1":
            if x > 20:
                func(idx+1, horse[:i]+horse[i+1:], tot)
            elif x == 20 and ((l,x) in horse or ("d2",7) in horse or ("d3",7) in horse or ("d4",7) in horse):
                continue
            else:
                if d1[x] == 10:
                    if ("d2", 0) not in horse:
                        func(idx+1, horse[:i]+horse[i+1:]+[("d2",0)], tot+10)
                elif d1[x] == 20:
                    if ("d3", 1) not in horse:
                        func(idx+1, horse[:i]+horse[i+1:]+[("d3",1)], tot+20)
                elif d1[x] == 30:
                    if ("d4", 0) not in horse:
                        func(idx+1, horse[:i]+horse[i+1:]+[("d4",0)], tot+30)
                else:
                    if (l, x) not in horse:
                        func(idx+1, horse[:i]+horse[i+1:]+[(l,x)], tot+d1[x])
        else:
            if (4 <= x < 7) and (("d2", x) in horse or ("d3", x) in horse or ("d4", x) in horse):
                continue
            elif x == 7 and (("d1",20) in horse or ("d2",x) in horse or ("d3",x) in horse or ("d4",x) in horse):
                continue
            elif x > 7:
                func(idx+1,horse[:i]+horse[i+1:],tot)
            else:
                if (l,x) in horse:
                    continue
                if l == "d2":
                    func(idx + 1, horse[:i] + horse[i + 1:] + [(l, x)], tot + d2[x])
                elif l == "d3":
                    func(idx + 1, horse[:i] + horse[i + 1:] + [(l, x)], tot + d3[x])
                elif l == "d4":
                    func(idx + 1, horse[:i] + horse[i + 1:] + [(l, x)], tot + d4[x])

func(0,[("d1",0) for _ in range(5)], 0)
print(ans)