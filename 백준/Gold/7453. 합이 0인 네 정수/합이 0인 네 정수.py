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
a_b = {}
for i in range(n):
    for j in range(n):
        num = A[i] + B[j]
        A_B.append(num)
A_B.sort()

c_d = {}
for i in range(n):
    for j in range(n):
        num = C[i] + D[j]
        if num in c_d:
            c_d[num] += 1
        else:
            c_d[num] = 1

def searching(num):
    lt = 0
    rt = len(C_D)
    while lt <= rt:
        mid = (lt+rt)//2
        if C_D[mid] < num:
            lt = mid + 1
        elif C_D[mid] > num:
            rt = mid - 1
        else:
            return c_d[C_D[mid]]
    return 0

ans = 0
for i in A_B:
    if -i in c_d:
        ans += c_d[-i]

print(ans)
