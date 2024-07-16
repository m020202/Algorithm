h, w = map(int,input().split())
box = list(map(int,input().split()))

def finding(rt):
    val = box[rt]
    for i in range(rt-1,-1,-1):
        if box[i] >= val:
            return True
    return False

ans = 0
def filling(rt):
    global ans
    val = box[rt]
    for i in range(rt-1,-1,-1):
        if box[i] >= val:
            return
        ans += (val - box[i])
        box[i] = val
        
for i in range(2,w):
    if finding(i):
        filling(i)

def findingV2(lt):
    val = box[lt]
    for i in range(lt+1,w):
        if box[i] >= val:
            return True
    return False

def fillingV2(lt):
    global ans
    val = box[lt]
    for i in range(lt+1,w):
        if box[i] >= val:
            return
        ans += (val - box[i])
        box[i] = val

for i in range(w-3,-1,-1):
    if findingV2(i):
        fillingV2(i)

print(ans)