import sys
input = sys.stdin.readline
n = int(input())
box = list(map(int,input().split()))
if sum(box) % 3 != 0:
    print("NO")
else:
    num = sum(box) // 3
    cnt = 0
    for i in box:
        cnt += (i // 2)
    if cnt >= num:
        print("YES")
    else:
        print("NO")