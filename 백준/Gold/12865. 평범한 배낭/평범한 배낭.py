import sys
input = sys.stdin.readline
n,k = map(int,input().split())
box = [tuple(map(int,input().split())) for _ in range(n)]
arr = [0] * (k+1)

for w,v in box:
    for i in range(k, w-1, -1):
        if arr[i] < v + arr[i-w]:
            arr[i] = arr[i-w] + v

print(max(arr))