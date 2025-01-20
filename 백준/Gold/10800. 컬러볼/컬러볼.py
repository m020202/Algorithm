import sys
input = sys.stdin.readline
n = int(input())

# 값들 입력 받고, 인덱스까지 포함해서 튜플로 넣기
box = []
for i in range(n):
    c,s = map(int,input().split())
    box.append((c,s,i))
box.sort(key = lambda x : x[1])

INF = 200001
cnt = [0] * INF
tot = 0
j = 0
ans = [0] * n
for i in range(n):
    while box[j][1] < box[i][1]:
        cnt[box[j][0]] += box[j][1]
        tot += box[j][1]
        j += 1
    ans[box[i][2]] = tot - cnt[box[i][0]]

[print(i) for i in ans]
