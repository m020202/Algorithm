import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
box = []
if m != 0:
    box = list(map(int, input().split()))
    box = set(box)

# 현재 채널에서 + 혹은 -만 사용하여 이동하는 경우
ans = abs(100 - n)

for i in range(1000000):
    if abs(n - i) >= ans:
        continue
    tmp = str(i)
    for j in tmp:
        if int(j) in box:
            break
    else:
        ans = min(len(tmp) + abs(n-i), ans)
print(ans)

