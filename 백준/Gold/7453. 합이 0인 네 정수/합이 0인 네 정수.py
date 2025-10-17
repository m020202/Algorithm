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

a_b = {}
for i in range(n):
    for j in range(n):
        num = A[i] + B[j]
        if num in a_b:
            a_b[num] += 1
        else:
            a_b[num] = 1

ans = 0
for i in range(n):
    for j in range(n):
        cur = C[i] + D[j]
        if -cur in a_b:
            ans += a_b[-cur]

print(ans)
