# 0: 빈칸, 1: 집, 2: 치킨집
import sys
INF = sys.maxsize
n,m = map(int,input().split())
box = []
hX = []
hY = []
cX = []
cY = []
for _ in range(n):
    box.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if box[i][j] == 1:
            hX.append(i)
            hY.append(j)
        
        if box[i][j] == 2:
            cX.append(i)
            cY.append(j)
    
ch = [[0] * len(cX) for _ in range(len(hX))]

for i in range(len(hX)):
    for j in range(len(cX)):
        num = abs(hX[i]-cX[j]) + abs(hY[i] - cY[j])
        ch[i][j] = num

array = list(range(len(cX)))
used = [False for _ in range(len(array))]

def checking(ch, arr):
    array = [[INF] * len(cX) for _ in range(len(hX))]
    for i in range(len(hX)):
        for j in arr:
            array[i][j] = ch[i][j]
        
    ans = 0
    for i in array:
        ans += min(i)
    return ans

ans = INF
def back_comb(idx,arr):
    global ans
    if len(arr) == m:
        cur = checking(ch, arr)
        ans = min(ans,cur)
        return

    for i in range(idx+1,len(array)):
        if used[i] == False:
            used[i] = True
            back_comb(i, arr + [array[i]])
            used[i] = False

back_comb(-1,[])
print(ans)