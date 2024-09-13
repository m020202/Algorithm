import sys
input = sys.stdin.readline

r,c,k = map(int,input().split())
r -= 1
c -= 1
box = [list(map(int,input().split())) for _ in range(3)]

# 열에 대한 정렬 수행
def col():
    global rl
    len_mx = 0
    tot = []
    for i in range(cl):
        cur = [0] * rl
        for j in range(rl):
            cur[j] = box[j][i]
        dic = {}
        for j in cur:
            if j != 0:
                dic[j] = 0
        for j in cur:
            if j != 0:
                dic[j] += 1
        
        arr = []
        for k in dic:
            arr.append((dic[k],k))
        arr.sort()
        
        new_box = []
        for cnt,val in arr:
            new_box.append(val)
            new_box.append(cnt)
        len_mx = max(len_mx, len(new_box))
        tot.append(new_box)

    # 행 크기 업데이트
    len_mx = min(len_mx, 100)
    if len_mx > rl:
        add = len_mx - rl
        for _ in range(add):
            box.append([0]*cl)
    elif len_mx < rl:
        for _ in range(rl-len_mx):
            box.pop()
    
    # 값 업데이트 하기
    for i in range(cl):
        if len(tot[i]) > len_mx:
            for j in range(len_mx):
                box[j][i] = tot[i][j]
        else:
            for j in range(len(tot[i])):
                box[j][i] = tot[i][j]
        
            cur = len_mx - len(tot[i])
            for j in range(len(tot[i]),len(tot[i]) + cur):
                box[j][i] = 0
    rl = len_mx

# 행에 대한 정렬 수행
def row():
    global cl
    len_mx = 0
    for i in range(rl):
        cur = box[i]
        dic = {}
        for j in cur:
            if j != 0:
                dic[j] = 0
        for j in cur:
            if j != 0:
                dic[j] += 1
        
        # 원소 형태: (횟수, 수)
        arr = []
        for k in dic:
            arr.append((dic[k],k))
        arr.sort()

        new_box = []
        for cnt,val in arr:
            new_box.append(val)
            new_box.append(cnt)
        box[i] = new_box
        len_mx = max(len_mx, len(new_box))

    len_mx = min(len_mx, 100)
    for i in range(rl):
        if len(box[i]) < len_mx:
            box[i] += [0] * (len_mx - len(box[i]))
        else:
            box[i] = box[i][:100]
    cl = len_mx

tot = 0
rl = 3
cl = 3

while True:
    if tot == 101:
        print(-1)
        break
    if r<rl and c<cl and box[r][c] == k:
        print(tot)
        break
    
    if rl >= cl:
        row()
    else:
        col()
    tot += 1
