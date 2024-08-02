from collections import deque
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    time = list(map(int,input().split()))
    time.insert(0,0)
    # 먼저 필요한 건물 리스트
    dic = {}
    # 먼저 필요한 건물 개수
    cnt = [0] * (n+1)
    for i in range(1,n+1):
        dic[i] = []
    for _ in range(k):
        x,y = map(int,input().split())
        dic[x].append(y)
        cnt[y] += 1

    w = int(input())

    # 각 건물마다 최종 건설 시간
    dp = [0] * (n+1)
    dQ = deque()
    for i in range(1,n+1):
        if  cnt[i] == 0:
            dQ.append(i)
            dp[i] = time[i]

    while dQ:
        cur = dQ.popleft()

        for i in dic[cur]:
            cnt[i] -= 1
            dp[i] = max(dp[cur] + time[i], dp[i])
            if cnt[i] == 0:
                dQ.append(i)
        
    print(dp[w])

                
        
