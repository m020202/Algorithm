import sys
input = sys.stdin.readline
l,c = map(int,input().split())
m = set('aeiou')
b1 = [] # 자음 (최소 2개 필요)
b2 = [] # 모음 (최소 1개 필요)
box = list(map(str,input().split()))
while box:
    cur = box.pop()
    if cur in m:
        b2.append(cur)
    else:
        b1.append(cur)

def chooseB1(idx, cur, num, mx): # 자음 선택
    if num == mx:
        resB1.append(cur)
        return
    for i in range(idx, len(b1)):
        chooseB1(i+1,cur+[b1[i]], num+1, mx)

def chooseB2(idx, cur, num, mx): # 모음 선택
    if num == mx:
        resB2.append(cur)
        return
    for i in range(idx, len(b2)):
        chooseB2(i+1,cur+[b2[i]], num+1, mx)

def mix(a,b):
    for i in a:
        for j in b:
            c = i + j
            c.sort()
            result.append(c)

result = []
for i in range(2, l):
    resB1 = []
    resB2 = []
    # 자음 선택
    chooseB1(0,[],0,i)
    # 모음 선택
    chooseB2(0,[],0,l-i)

    mix(resB1, resB2)

result.sort()
for i in result:
    print(''.join(i))





