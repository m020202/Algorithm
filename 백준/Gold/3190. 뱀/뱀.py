from collections import deque
n = int(input())
k = int(input())
ch = [[0] * n for _ in range(n)]
ch[0][0] = 1

for _ in range(k):
    i,j = map(int,input().split())
    ch[i-1][j-1] = 2
    
l = int(input())
dQ = deque()
for _ in range(l):
    x,c = map(str,input().split())
    dQ.append((x,c))

now = 0
curX = 0
curY = 0
tail = deque()
tail.append((0,0))

def remove():
    global tail, ch
    x,y = tail.popleft()
    ch[x][y] = 0

direct = 0
def move(limit):
    global ch,now,curX,curY,tail
    now += 1
    if direct == 0:
        if 0<=curY+1<n:
            if ch[curX][curY+1] == 0:
                curY += 1
                ch[curX][curY] = 1
                tail.append((curX,curY))
                remove()
            elif ch[curX][curY+1] == 1:
                return False
            else:
                curY += 1
                ch[curX][curY] = 1
                tail.append((curX,curY))
        else:
            return False
    elif direct == 1:
        if 0<=curY-1<n:
            if ch[curX][curY-1] == 0:
                curY -= 1
                ch[curX][curY] = 1
                tail.append((curX,curY))
                remove()
            elif ch[curX][curY-1] == 1:
                return False
            else:
                curY -= 1    
                ch[curX][curY] = 1
                tail.append((curX,curY))                          
        else:
            return False
    elif direct == 2:
        if 0<=curX+1<n:
            if ch[curX+1][curY] == 0:
                curX += 1
                ch[curX][curY] = 1
                tail.append((curX,curY))
                remove()
            elif ch[curX+1][curY] == 1:
                return False
            else:
                curX += 1   
                ch[curX][curY] = 1
                tail.append((curX,curY)) 
        else:
            return False
    else:
        if 0<=curX-1<n:
            if ch[curX-1][curY] == 0:
                curX -= 1
                ch[curX][curY] = 1
                tail.append((curX,curY))
                remove()
            elif ch[curX-1][curY] == 1:
                return False
            else:
                curX -= 1   
                ch[curX][curY] = 1
                tail.append((curX,curY)) 
        else:
            return False 
    
    if (now == limit):
        return True
    return move(limit)

def move2():
    global ch,now,curX,curY,tail
    now += 1
    if direct == 0:
        if 0<=curY+1<n:
            if ch[curX][curY+1] == 0:
                curY += 1
                ch[curX][curY] = 1
                tail.append((curX,curY))
                remove()
            elif ch[curX][curY+1] == 1:
                return False
            else:
                curY += 1
                ch[curX][curY] = 1
                tail.append((curX,curY))
        else:
            return False
    elif direct == 1:
        if 0<=curY-1<n:
            if ch[curX][curY-1] == 0:
                curY -= 1
                ch[curX][curY] = 1
                tail.append((curX,curY))
                remove()
            elif ch[curX][curY-1] == 1:
                return False
            else:
                curY -= 1    
                ch[curX][curY] = 1
                tail.append((curX,curY))                          
        else:
            return False
    elif direct == 2:
        if 0<=curX+1<n:
            if ch[curX+1][curY] == 0:
                curX += 1
                ch[curX][curY] = 1
                tail.append((curX,curY))
                remove()
            elif ch[curX+1][curY] == 1:
                return False
            else:
                curX += 1   
                ch[curX][curY] = 1
                tail.append((curX,curY)) 
        else:
            return False
    else:
        if 0<=curX-1<n:
            if ch[curX-1][curY] == 0:
                curX -= 1
                ch[curX][curY] = 1
                tail.append((curX,curY))
                remove()
            elif ch[curX-1][curY] == 1:
                return False
            else:
                curX -= 1   
                ch[curX][curY] = 1
                tail.append((curX,curY)) 
        else:
            return False 
    
    return move2()


status = False
while dQ:
    cur, dir = dQ.popleft()
    cur = int(cur)
    tmp = move(cur)
    if (tmp == False):
        status = True
        print(now)
        break
    else:
        if dir == 'D':
            if direct == 0:
                direct = 2
            elif direct == 1:
                direct = 3
            elif direct == 2:
                direct = 1
            else:
                direct = 0

        else:
            if direct == 0:
                direct = 3
            elif direct == 1:
                direct = 2
            elif direct == 2:
                direct = 0
            else:
                direct = 1

if status == False:
    move2()
    print(now)

