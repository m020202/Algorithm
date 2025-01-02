import sys
t = list(map(int,input().split()))
box = []
for i in t:
    if i == 0:
        break
    box.append(i)

if (len(box) == 0):
    print(0)
    sys.exit(1)

# 첫 번째
dp = []
dp.append((0,box[0],2))

def func(x,cur):
    # 둘이 같을 때
    if x == cur:
        return 1

    if x == 0:
        return 2

    # 둘이 인접할 때
    if cur == 1:
        if x == 2 or x == 4:
            return 3
    elif cur == 4:
        if x == 3 or x == 1:
            return 3
    else:
        if x == cur -1 or x == cur + 1:
            return 3

    # 정 반대일 때
    return 4

for i in range(1, len(box)):
    cur = box[i]
    tmp = [[-1] * 5 for _ in range(5)]
    while dp:
        x,y,val = dp.pop()
        # x 값 바꾸기
        num = func(x, cur)
        if cur == y:
            pass
        elif cur < y:
            if tmp[cur][y] == -1:
                tmp[cur][y] = val + num
            else:
                tmp[cur][y] = min(tmp[cur][y], val + num)
        else:
            if tmp[y][cur] == -1:
                tmp[y][cur] = val + num
            else:
                tmp[y][cur] = min(tmp[y][cur], val + num)
        # y 값 바꾸기
        num = func(y, cur)
        if x == cur:
            pass
        elif x < cur:
            if tmp[x][cur] == -1:
                tmp[x][cur] = val + num
            else:
                tmp[x][cur] = min(tmp[x][cur], val + num)
        else:
            if tmp[cur][x] == -1:
                tmp[cur][x] = val + num
            else:
                tmp[cur][x] = min(tmp[cur][x], val + num)

    for x in range(5):
        for y in range(5):
            if tmp[x][y] != -1:
                dp.append((x,y,tmp[x][y]))

mn = dp[0][-1]

for x,y,val in dp:
    mn = min(mn, val)

print(mn)

