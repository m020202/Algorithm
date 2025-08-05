import sys, math
input = sys.stdin.readline
N,M,K = map(int,input().split())

# 사전에 수록된 문자열 개수 < K 체크
count = math.factorial(N+M) // math.factorial(N) // math.factorial(M)
if count < K:
    print(-1)
    sys.exit()

# arr[a의 개수][z의 개수]
arr = [[1]*(M+1) for _ in range(N+1)]
for i in range(1,M+1):
    arr[1][i] = i+1
for i in range(1,N+1):
    arr[i][1] = i+1
for i in range(2,N+1):
    for j in range(2,M+1):
        arr[i][j] = arr[i-1][j] + arr[i][j-1]

l = N+M
def dfs(idx,cnt,ans,num):
    if num == 0:
        if len(ans) < N+M:
            ans += 'z'*(N+M-len(ans))
        print(ans)
        sys.exit()
    else:
        cur = arr[num-1][l-idx-num+1]
        if K <= cnt+cur:
            return dfs(idx+1,cnt,ans+'a',num-1)
        else:
            return dfs(idx+1,cnt+cur,ans+'z',num)

dfs(1,0,'',N)



