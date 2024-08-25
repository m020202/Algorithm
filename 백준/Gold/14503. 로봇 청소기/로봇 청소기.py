n,m = map(int,input().split())
r,c,d = map(int,input().split())
box = []


for _ in range(n):
    spot = list(map(int,input().split()))
    box.append(spot)

def DFS(r,c,d,cnt):
    if box[r][c] == 0:
        box[r][c] = 2
        cnt+=1
    
    
    for _ in range(4):
        d = (d+3)%4
        if d == 0:
            if box[r-1][c] == 0:
                return DFS(r-1,c,d,cnt)
        elif d == 1:
            if box[r][c+1] == 0:
                return DFS(r,c+1,d,cnt)
        elif d == 2:
            if box[r+1][c] == 0:
                return DFS(r+1,c,d,cnt)
        elif d == 3:
            if box[r][c-1] == 0:
                return DFS(r,c-1,d,cnt)
    
    if d == 0:
        if box[r+1][c] != 1:
            return DFS(r+1,c,d,cnt)
        else:
            return cnt
    elif d == 1:
        if box[r][c-1] != 1:
            return DFS(r,c-1,d,cnt)
        else:
            return cnt
    elif d == 2:
        if box[r-1][c] != 1:
            return DFS(r-1,c,d,cnt)
        else:
            return cnt
    elif d == 3:
        if box[r][c+1] != 1:
            return DFS(r,c+1,d,cnt)
        else:
            return cnt
    
            
print(DFS(r,c,d,0))




        
