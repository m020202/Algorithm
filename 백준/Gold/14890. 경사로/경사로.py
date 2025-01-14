import sys
input = sys.stdin.readline
n,l = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(n)]
ans = 0

def checking():
    global ans
    for i in range(n):
        tmp = box[i]
        ch = [0] * n  # 경사로 놓아진 길
        status = True
        for j in range(n - 1):
            if ch[j] == 1 and ch[j+1] == 1:
                continue
            if tmp[j] == tmp[j + 1]:
                continue
            elif tmp[j] == tmp[j + 1] + 1:
                if j + l < n:
                    for k in range(j + 1, j + 1 + l):
                        if tmp[k] != tmp[j + 1] or ch[k] == 1:
                            status = False
                            break
                    else:
                        for k in range(j + 1, j + 1 + l):
                            ch[k] = 1
                else:
                    status = False
            elif tmp[j] + 1 == tmp[j + 1]:
                if j - l + 1 >= 0:
                    for k in range(j - l + 1, j+1):
                        if tmp[k] != tmp[j] or ch[k] == 1:
                            status = False
                            break
                    else:
                        ch[j] = 1
                else:
                    status = False
            else:
                status = False
            if status == False:
                break
        if status == True:
            ans += 1



# 가로 체크
checking()
# 세로 체크
box = list(map(list, zip(*box)))
checking()

print(ans)

