n = int(input())
box = list(map(int,input().split()))
st = 0
en = 0
ch = [0] * 100001
ans = 0
while en < n:
    if ch[box[en]] == 0:
        ch[box[en]] = 1
        en += 1
        ans += en - st
    else:
        while ch[box[en]]:
            ch[box[st]] = 0
            st += 1

print(ans)
