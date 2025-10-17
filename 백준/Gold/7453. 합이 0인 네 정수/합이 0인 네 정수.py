import sys
input = sys.stdin.readline
n = int(input())
A,B,C,D = [], [], [], []
for _ in range(n):
    a,b,c,d = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

A_B = []
for i in range(n):
    for j in range(n):
        A_B.append(A[i]+B[j])
A_B.sort()

C_D = []
for i in range(n):
    for j in range(n):
        C_D.append(C[i]+D[j])
C_D.sort()

ans = 0
lt,rt = 0,len(C_D)-1
while lt < len(A_B) and rt >= 0:
    mid = A_B[lt] + C_D[rt]
    if mid > 0:
        rt -= 1
    elif mid < 0:
        lt += 1
    else:
        cur = A_B[lt]
        l_cnt = 0
        while lt < len(A_B) and A_B[lt] == cur:
            l_cnt += 1
            lt += 1

        cur = C_D[rt]
        r_cnt = 0
        while rt >= 0 and C_D[rt] == cur:
            r_cnt += 1
            rt -= 1

        ans += (l_cnt*r_cnt)

print(ans)
