import sys
input = sys.stdin.readline
N,K = map(int,input().split())
num = list(map(int,input().rstrip()))
ans = []
for i in num:
    while K and ans and ans[-1] < i:
        ans.pop()
        K -= 1
    ans.append(i)

if K:
    print(''.join(map(str,ans[:-K])))
else:
    print(''.join(map(str,ans)))