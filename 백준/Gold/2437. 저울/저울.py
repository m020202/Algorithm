import sys
input = sys.stdin.readline
n = int(input())
box = list(map(int, input().split()))
box.sort()

rt = 0
for i in box:
    if rt + 1 < i:
        break
    rt += i
print(rt+1)