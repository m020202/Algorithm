import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)
N = int(input())
box = list(map(int,input().split()))
edge = {i:set() for i in range(N)}
for _ in range(N-1):
    a,b = map(int,input().split())
    edge[a-1].add(b-1)
    edge[b-1].add(a-1)
wo = [0] * N # 내가 우수 마을 아닐 때 최댓값
wx = [0] * N # 내가 우수 마을 일 때 최댓값

def search(cur,status,parent):
    if status:
        if wo[cur] != 0:
            return wo[cur]
        else:
            res = box[cur]
            for i in edge[cur]:
                if parent != i:
                    res += search(i,0,cur)
            wo[cur] = res
            return res
    else:
        if wx[cur] != 0:
            return wx[cur]
        else:
            res = 0
            for i in edge[cur]:
                if parent != i:
                    res += max(search(i,0,cur), search(i,1,cur))
            wx[cur] = res
            return res

print(max(search(0,0,-1), search(0,1,-1)))