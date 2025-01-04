import copy
n,m = map(int,input().split())
a = list(map(int,input().split()))
c = list(map(int,input().split()))

# 초기 세팅
if m > max(a):
    ch1 = [-1] * (m+1)
    ch2 = [-1] * (m+1)
else:
    ch1 = [-1] * (max(a) + 1)
    ch2 = [-1] * (max(a) + 1)

ch1[0] = 0
ch2[0] = 0
cur = a[0]
val = c[0]
for i in range(1,cur+1):
    ch1[i] = val

for j in range(1,n):
    cur = a[j]
    val = c[j]

    if j % 2 == 0:
        # ch1 사용
        for i in range(1, cur + 1):
            if ch2[i] > val or ch2[i] == -1:
                ch1[i] = val
            else:
                ch1[i] = ch2[i]

        for i in range(cur + 1, m + 1):
            num = i - cur
            if ch2[num] == -1:
                break
            if ch2[i] == -1:
                ch1[i] = val + ch2[num]
            else:
                ch1[i] = min(ch2[i], val + ch2[num])
    else:
        # ch2 사용
        for i in range(1, cur+1):
            if ch1[i] > val or ch1[i] == -1:
                ch2[i] = val
            else:
                ch2[i] = ch1[i]

        for i in range(cur+1, m+1):
            num = i - cur
            if ch1[num] == -1:
                break
            if ch1[i] == -1:
                ch2[i] = val + ch1[num]
            else:
                ch2[i] = min(ch1[i], val+ch1[num])

if (n-1) % 2 == 0:
    print(ch1[m])
else:
    print(ch2[m])
