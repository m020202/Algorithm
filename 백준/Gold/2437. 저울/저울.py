import sys
input = sys.stdin.readline
n = int(input())
box = list(map(int, input().split()))
box.sort()

cur = 1
for i in box:
    if cur < i:
        break
    cur += i
print(cur)