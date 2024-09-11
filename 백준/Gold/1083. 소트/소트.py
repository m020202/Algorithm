import sys,copy
input = sys.stdin.readline

n = int(input())
box = list(map(int,input().split()))
srt = copy.deepcopy(box)
ch = [0] * n

def sorting():
    global box,srt,ch
    srt = copy.deepcopy(box)
    srt.sort(reverse=True)
    ch = [0] * n
    for i in range(n):
        cur = srt[i]
        ch[i] = box.index(cur)

s = int(input())

sorting()
cnt = 0
while s > 0 and cnt < n:
    # 숫자의 인덱스
    idx = 0
    # 바꿀 대상
    num = box[cnt]
    c = srt.index(num)
    # 실제 box에서의 위치
    tf = False
    for i in range(c):
        if 0<= ch[i] - cnt <= s:
            idx = ch[i]
            tf = True
            break
    if not tf:
        cnt += 1
        continue
    for i in range(idx,cnt,-1):
        tmp = box[i]
        box[i] = box[i-1]
        box[i-1] = tmp
    
    sorting()
    s -= (idx-cnt)
    cnt += 1

for i in box:
    print(i,end=' ')