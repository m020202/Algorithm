import sys
n = int(input())
box = [list(map(str,input().split())) for _ in range(n)]
stu = []
for i in range(n):
    for j in range(n):
        if box[i][j] == "S":
            stu.append((i,j))

def checking():
    # S 하나씩 탐색하기
    for x,y in stu:
        # 위 탐색
        for i in range(x,-1,-1):
            if box[i][y] == 'O':
                break
            elif box[i][y] == 'X' or box[i][y] == 'S':
                continue
            else:
                return False
            
        # 아래 탐색
        for i in range(x,n):
            if box[i][y] == 'O':
                break
            elif box[i][y] == 'X' or box[i][y] == 'S':
                continue
            else:
                return False
        
        # 왼 탐색
        for i in range(y,-1,-1):
            if box[x][i] == 'O':
                break
            elif box[x][i] == 'X' or box[x][i] == 'S':
                continue
            else:
                return False

        # 오른 탐색
        for i in range(y,n):
            if box[x][i] == 'O':
                break
            elif box[x][i] == 'X' or box[x][i] == 'S':
                continue
            else:
                return False
    return True

def DFS(cur):
    if cur == 3:
        if checking():
            print("YES")
            sys.exit(0)
    else:
        for i in range(n):
            for j in range(n):
                if box[i][j] == 'X':
                    box[i][j] = 'O'
                    DFS(cur+1)
                    box[i][j] = 'X'

DFS(0)
print("NO")