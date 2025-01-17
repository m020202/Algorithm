import sys
input = sys.stdin.readline
t = int(input())
INF = sys.maxsize

for _ in range(t):
    k = int(input())
    box = list(map(int,input().split()))
    ch = [[-1] * k for _ in range(k)]
    tmp = [[0] * k for _ in range(k)]
    def dp(i, j):
        global ch, tmp
        if i == j:
            ch[i][i] = box[i]
            return 0

        if ch[i][j] != -1:
            return tmp[i][j]

        # i부터 l까지 합 최소 구하기
        tot = INF
        for k in range(i, j):
            l = dp(i, k) # 왼쪽 합치는데 드는 비용
            r = dp(k + 1, j) # 오른쪽 합치는데 드는 비용
            if tot > l + ch[i][k] + r + ch[k+1][j]:
                tot = l + ch[i][k] + r + ch[k+1][j]
                ch[i][j] = ch[i][k] + ch[k+1][j]
        tmp[i][j] = tot
        return tot
    print(dp(0,k-1))

