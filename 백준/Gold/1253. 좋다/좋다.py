n = int(input())
box = list(map(int,input().split()))
box.sort()

ch = {}
cnt = 0
for i in range(len(box)):
    if box[i] in ch:
        cnt += 1
        continue
    lt = 0
    rt = 1
    while lt < n-1:
        if lt == i:
            lt += 1
            rt = lt + 1
            continue
        if rt == i:
            rt += 1
            if rt == n:
                lt += 1
                rt = lt + 1
                continue
        num = box[lt] + box[rt]
        if num == box[i]:
            cnt += 1
            ch[box[i]] = 1

            break
        elif num < box[i]:
            rt += 1
            if rt == n:
                lt += 1
                rt = lt + 1
        else:
            lt += 1
            rt = lt + 1
print(cnt)

