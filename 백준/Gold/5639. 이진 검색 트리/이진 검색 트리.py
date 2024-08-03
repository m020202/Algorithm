import sys
sys.setrecursionlimit(65536)
input = sys.stdin.readline

box = []
while True:
    try:
        box.append(int(input()))
    except:
        break

def postOrder(arr):
    if len(arr) == 0:
        return
    mid = arr[0]
    left = []
    right = []
    for i in range(1,len(arr)):
        if arr[i] > mid:
            left = arr[1:i]
            right = arr[i:]
            break
    else:
        left = arr[1:]
    postOrder(left)
    postOrder(right)
    print(mid)
    
postOrder(box)