import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000+10)

n = int(input())
box = [tuple(map(int,input().split())) for _ in range(n)]
box.sort(key= lambda x : (x[1],x[0]))
ans = 0

def func(idx, cur):
    global ans
    for i in range(idx+1,n):
        if box[i][0] >= box[idx][1]:
            return func(i, cur+1)
    else:
        ans = max(ans, cur)

func(0,1)
print(ans)