import sys
input = sys.stdin.readline
N,M = map(int,input().split())
arr = [int(input()) for _ in range(N)]
box = [tuple(map(int,input().split())) for _ in range(M)]
max_tree = [0] * 4 * N
min_tree = [0] * 4 * N
l = 0
def max_init(idx,lt,rt):
    global l
    if lt == rt:
        l = max(l,idx)
        max_tree[idx] = arr[lt]
        return max_tree[idx]
    else:
        mid = (lt+rt)//2
        max_tree[idx] = max(max_init(idx*2,lt,mid), max_init(idx*2+1,mid+1,rt))
        return max_tree[idx]

def min_init(idx,lt,rt):
    if lt == rt:
        min_tree[idx] = arr[lt]
        return min_tree[idx]
    else:
        mid = (lt+rt)//2
        min_tree[idx] = min(min_init(idx*2,lt,mid), min_init(idx*2+1,mid+1,rt))
        return min_tree[idx]

max_init(1,0,N-1)
min_init(1,0,N-1)

def searching(idx,lt,rt,a,b):
    global min_res,max_res
    if lt == a and rt == b:
        min_res = min(min_res,min_tree[idx])
        max_res = max(max_res,max_tree[idx])
    else:
        mid = (lt+rt)//2
        if b <= mid:
            return searching(idx*2,lt,mid,a,b)
        elif a > mid:
            return searching(idx*2+1,mid+1,rt,a,b)
        else:
            searching(idx*2,lt,mid,a,mid)
            searching(idx*2+1,mid+1,rt,mid+1,b)

for a,b in box:
    min_res = sys.maxsize
    max_res = 0
    searching(1,0,N-1,a-1,b-1)
    print(min_res,max_res)
