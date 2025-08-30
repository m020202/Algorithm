import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
arr = [A[0]]

def searching(num):
    lt = 0
    rt = len(arr)-1
    res = -sys.maxsize
    idx = -1
    while lt <= rt:
        mid = (lt+rt)//2
        if arr[mid] > num:
            rt = mid - 1
        elif arr[mid] < num:
            if res < arr[mid]:
                res = arr[mid]
                idx = mid
            lt = mid + 1
        else:
            return mid
    return idx+1

ans = 1
for i in range(1,N):
    cur = A[i]
    if arr[-1] < cur:
        arr.append(cur)
        ans += 1
    elif arr[-1] > cur:
        idx = searching(cur)
        arr[idx] = cur

print(ans)