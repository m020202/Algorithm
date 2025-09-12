import sys
input = sys.stdin.readline
arr = list(map(str,input().rstrip()))

def PSL(pattern):
    i = 0
    ch = [0]*len(pattern)
    for j in range(1,len(pattern)):
        while i > 0 and pattern[i] != pattern[j]:
            i = ch[i-1]
        if pattern[i] == pattern[j]:
            i += 1
            ch[j] = i
    return ch

ans = 0
for i in range(len(arr)):
    ans = max(ans,max(PSL(arr[i:])))
print(ans)
