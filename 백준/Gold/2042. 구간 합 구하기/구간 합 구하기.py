import sys
input = sys.stdin.readline
N,M,K = map(int,input().split())
arr = [int(input()) for _ in range(N)]
tree = [0] * 4 * N
box = [tuple(map(int,input().split())) for _ in range(M+K)]
l = 0
# 세그먼트 트리 생성
def init(idx,lt,rt):
    global l
    l = max(idx,l)
    if lt == rt:
        tree[idx] = arr[lt]
        return arr[lt]
    else:
        tree[idx] = init(idx*2,lt,(lt+rt)//2) + init(idx*2+1,(lt+rt)//2+1,rt)
        return tree[idx]
init(1,0,N-1)

# 트리 값 업데이트
def updating(idx,lt,rt,target,past,new):
    if idx > l:
        return
    tree[idx] -= (past - new)
    nxt = (lt+rt)//2
    if target <= nxt:
        return updating(idx*2,lt,nxt,target,past,new)
    else:
        return updating(idx*2+1,nxt+1,rt,target,past,new)

# 부분합 계산
def calc(idx,lt,rt,t_lt,t_rt):
    global res
    if lt == t_lt and rt == t_rt:
        res += tree[idx]
        return
    mid = (lt+rt)//2
    if t_lt > mid:
        return calc(idx*2+1,mid+1,rt,t_lt,t_rt)
    elif t_rt <= mid:
        return calc(idx*2,lt,mid,t_lt,t_rt)
    else:
        calc(idx*2,lt,mid,t_lt,mid)
        calc(idx*2+1,mid+1,rt,mid+1,t_rt)

for a,b,c in box:
    if a == 1:
        updating(1,0,N-1,b-1,arr[b-1],c)
        arr[b-1] = c
    else:
        res = 0
        calc(1,0,N-1,b-1,c-1)
        print(res)

