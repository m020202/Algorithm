import sys
input = sys.stdin.readline

n = int(input())
box = list(map(int,input().split()))
stack = []

ans = [-1] * n
for i in range(n):
    if stack and box[i] > stack[-1][1]:
        while stack:
            if stack[-1][1] < box[i]:
                idx, val = stack.pop()
                ans[idx] = box[i]
            else:
                break
    stack.append((i, box[i]))

print(' '.join(map(str,ans)))



