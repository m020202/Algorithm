import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    ch = [0] * (N + 1)
    arr.sort(key=lambda x: (x[1], x[0]))
    ans = 0
    for i,j in arr:
        for k in range(i,j+1):
            if ch[k] == 0:
                ch[k] = 1
                ans += 1
                break
    print(ans)