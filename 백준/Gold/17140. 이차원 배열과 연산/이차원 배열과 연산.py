import sys
input = sys.stdin.readline

r,c,k = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(3)]
r -= 1
c -= 1

def func():
    global box
    max_len = 0
    new_box = []
    for i in box:
        cur = set(i)
        tmp = [] # (수, 횟수)
        new_i = []
        for j in cur:
            if j != 0:
                tmp.append((j,i.count(j)))
        tmp.sort(key= lambda x : (x[1],x[0]))
        for val,cnt in tmp:
            new_i.append(val)
            new_i.append(cnt)
        new_i = new_i[:100]
        max_len = max(max_len, len(new_i))
        new_box.append(new_i)
    
    for i in new_box:
        if len(i) < max_len:
            i += [0] * (max_len - len(i))
    box = new_box
    return max_len
    
time = 0
rl = 3  # 행 개수
cl = 3  # 열 개수

while True:
    if time > 100:
        print(-1)
        break
    if r < rl and c < cl and box[r][c] == k:
        print(time)
        break
    if rl >= cl:
        cl = func()
    else:
        box = [list(row) for row in zip(*box)]
        rl = func()
        box = [list(row) for row in zip(*box)]

    time += 1