box = [0]
for _ in range(4):
    box.append(list(map(int,input())))

k = int(input())

ch = [2] * 5

def checking(num, dir):
    global ch
    ch[num] = dir
    curDir = dir
    curStatus = box[num][6]
    for i in range(num-1,0,-1):      
        if box[i][2] == curStatus or curDir == 0:
            ch[i] = 0
            curDir = 0
        else:
            if (curDir == 1):
                ch[i] = -1
            else:
                ch[i] = 1
            curDir = ch[i]
            curStatus = box[i][6]
    
    curDir = dir
    curStatus = box[num][2]
    for i in range(num+1,5):
        if box[i][6] == curStatus or curDir == 0:
            ch[i] = 0
            curDir = 0
        else:
            if (curDir == 1):
                ch[i] = -1
            else:
                ch[i] = 1   
            curDir = ch[i]
            curStatus = box[i][2]

def swap():
    global box
    for i in range(1,5):
        if ch[i] == 1:
            tmp = box[i][-1]
            for j in range(7,0,-1):
                box[i][j] = box[i][j-1]
            box[i][0] = tmp
        elif ch[i] == -1:
            tmp = box[i][0]
            for j in range(7):
                box[i][j] = box[i][j+1]
            box[i][-1] = tmp
        else:
            continue



for _ in range(k):
    num, dir = map(int,input().split())
    checking(num, dir)
    swap()

sum = 0
if box[1][0] == 1:
    sum += 1
if box[2][0] == 1:
    sum += 2
if box[3][0] == 1:
    sum += 4
if box[4][0] == 1:
    sum += 8

print(sum)

