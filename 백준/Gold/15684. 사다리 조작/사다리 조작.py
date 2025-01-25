import sys
input = sys.stdin.readline
n,m,h = map(int,input().split())
box = [[0] * n for _ in range(h)]
for _ in range(m):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    box[x][y] = 1

# 탐색하기
def searching():
    for i in range(n):
        x,y = 0,i
        while x < h:
            if box[x][y] == 1:
                y += 1
            elif box[x][y-1] == 1:
                y -= 1
            x += 1
        if y != i:
            return False
    return True

# 0일 때
if searching():
    print(0)
    sys.exit()

ans = -1
def checking(cnt):
    global ans
    if cnt == 3:
        return
    else:
        for i in range(h):
            for j in range(n-1):
                if j >= 1 == box[i][j - 1]:
                    continue
                if box[i][j] == 0:
                    box[i][j] = 1
                    if searching():
                        if cnt == 0:
                            print(1)
                            sys.exit()
                        if ans == -1:
                            ans = cnt + 1
                        else:
                            ans = min(ans, cnt + 1)
                    checking(cnt + 1)
                    box[i][j] = 0
checking(0)

print(ans)

