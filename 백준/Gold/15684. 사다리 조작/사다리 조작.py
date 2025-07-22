import sys
input = sys.stdin.readline
n,m,h = map(int,input().split())
ch = [[0]* n for _ in range(h+1)]
dic = {i : {} for i in range(1,h+1)}
for _ in range(m):
    a,b = map(int,input().split())
    dic[a][b] = True
    ch[a][b] = 1

def checking():
    for i in range(1,n+1):
        cur = i
        for j in range(1,h+1):
            if cur in dic[j]:
                cur += 1
            elif cur-1 in dic[j]:
                cur -= 1
        if cur != i:
            return False
    return True

# 0인 경우
if checking():
    print(0)
    sys.exit()

# 1, 2, 3인 경우
is3 = False
def dfs(cur,l,k):
    global is3
    if cur == 3:
        if checking():
            is3 = True
    else:
        if cur == 1:
            if checking():
                print(1)
                sys.exit()
        if cur == 2:
            if checking():
                print(2)
                sys.exit()

        for i in range(k+1,n):
            if ch[l][i] == 0:
                ch[l][i] = 1
                dic[l][i] = True
                dfs(cur+1,l,i)
                ch[l][i] = 0
                dic[l].pop(i)

        for i in range(l+1,h+1):
            for j in range(1,n):
                if ch[i][j] == 0:
                    ch[i][j] = 1
                    dic[i][j] = True
                    dfs(cur+1,i,j)
                    ch[i][j] = 0
                    dic[i].pop(j)

dfs(0,1,0)
print(3 if is3 else -1)
