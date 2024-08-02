from collections import deque
t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    time = list(map(int,input().split()))
    time.insert(0,0)
    # 먼저 필요한 건물 리스트
    dic = {}
    # 먼저 필요한 건물 개수
    cnt = [0] * (n+1)
    # 후에 지을 수 있는 건물 리스트
    outDic = {}
    for i in range(1,n+1):
        dic[i] = []
        outDic[i] = []
    for _ in range(k):
        x,y = map(int,input().split())
        dic[y].append(x)
        outDic[x].append(y)
    for i in range(1,n+1):
        cnt[i] = len(dic[i])
    w = int(input())

    # 각 건물마다 최종 건설 시간
    dp = [0] * (n+1)
    dQ = deque()
    for i in range(1,n+1):
        if len(dic[i]) == 0:
            dQ.append(i)

    while dQ:
        cur = dQ.popleft()
        dp[cur] = time[cur]
        if len(dic[cur]) > 0:
            mx = 0
            for i in dic[cur]:
                mx = max(mx, dp[i])
            dp[cur] += mx

        for i in outDic[cur]:
            cnt[i] -= 1
            if cnt[i] == 0:
                dQ.append(i)
        
    print(dp[w])

                
        